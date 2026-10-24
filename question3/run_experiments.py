"""Reproduce the checked hourly experiments. Run from this directory or anywhere.

python run_experiments.py [--workers 2] [--only case_id ...]
Results are written individually so completed work survives interruption.
"""
from pathlib import Path
import argparse, json, hashlib, time, traceback
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed
from ocean_model_checked import solve, serializable

ROOT=Path(__file__).resolve().parent

def cases():
    jobs=[]
    def add(name,site='scotland',year=None,**settings):
        jobs.append(dict(id=name,site=site,year=year,**settings))
    add('original_2023_reliability_check',year='2023',float_price=None,tidal_price=None)
    # Correct the stated floating-wind price to $74/MWh using a common 2022–24 reference profile.
    for price in [None,140,120,100,90]:
        add('scotland_3yr_'+('no_tidal' if price is None else 'tidal_'+str(price)),
            float_price=74,tidal_price=price,exclude_tidal=price is None)
    add('scotland_3yr_tidal100_ldes50',float_price=74,tidal_price=100,ldes_energy_multiplier=2)
    add('scotland_3yr_tidal100_battery_only',float_price=74,tidal_price=100,allow=['batt'])
    add('scotland_3yr_marine30',float_price=74,tidal_price=140,min_marine_generation_share=.3)
    add('scotland_3yr_tidal100_wave80',float_price=74,tidal_price=100,wave_price=80)
    add('scotland_3yr_nuclear_allowed',float_price=74,tidal_price=100,allow=['batt','ldes','nuc'])
    add('scotland_3yr_firm100',float_price=74,tidal_price=100,allow=['batt','ldes','nuc'],firm_price=100)
    for cf in [30,40]:
        add('scotland_3yr_tidalcf'+str(cf),site='scotland_tcf'+str(cf),float_price=74,tidal_price=100)
    for price in [None,100]:
        add('scotland_2010_'+('no_tidal' if price is None else 'tidal100'),
            site='scotland_2010',float_price=74,tidal_price=price,exclude_tidal=price is None)
    for price in [None,100,90]:
        add('hawaii_3yr_'+('no_otec' if price is None else 'otec'+str(price)),
            site='hawaii',float_price=74,otec_price=price,exclude_otec=price is None)
    return jobs

def _run(job):
    path=ROOT/'inputs'/('profiles_'+job['site']+'.csv')
    cf=pd.read_csv(path,index_col=0,parse_dates=True)
    if job.get('year'): cf=cf.loc[job['year']]
    assert cf.index.is_unique and cf.index.is_monotonic_increasing
    assert (cf.index.to_series().diff().dropna()==pd.Timedelta(hours=1)).all()
    costs=dict(json.loads((ROOT/'inputs/costs.json').read_text())['2035'])
    reference_site='hawaii' if job['site']=='hawaii' else 'scotland'
    reference=pd.read_csv(ROOT/'inputs'/('profiles_'+reference_site+'.csv'),index_col=0)
    # Supplied OTEC profile exceeds one. Treat installed capacity as a hard AC
    # rating in checked cases; preserve the original file without modification.
    clipping={name:int((cf[name]>1).sum()) for name in cf if (cf[name]>1).any()}
    cf=cf.clip(upper=1.0); reference=reference.clip(upper=1.0)
    applied={}
    for field,tech in [('float_price','offwind_floating'),('tidal_price','tidal'),('wave_price','wave'),('otec_price','otec')]:
        if job.get(field) is not None and tech in cf:
            costs[tech]=job[field]*reference[tech].mean()*8.76
            applied[tech]={'reference_lcoe_usd_mwh':job[field],'reference_2022_2024_mean':float(reference[tech].mean()),'fixed_usd_kw_year':costs[tech]}
    if job.get('ldes_energy_multiplier'): costs['ldes_E']*=job['ldes_energy_multiplier']
    if job.get('firm_price'):
        costs['nuc_fix']=(job['firm_price']-costs['nuc_var'])*.9*8.76
    if job.get('exclude_tidal'):cf=cf.drop(columns='tidal')
    if job.get('exclude_otec'):cf=cf.drop(columns='otec')
    kw={'allow':job.get('allow',['batt','ldes'])}
    if job['site']=='hawaii':kw['cap_max']={'onwind':.3}
    if job.get('min_marine_generation_share') is not None:
        kw['min_marine_generation_share']=job['min_marine_generation_share']
    result=solve(cf,costs,**kw)
    out=serializable(result)
    out.update(job=job,costs=costs,price_calibration=applied,clipped_hours=clipping,profile_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
               hours=len(cf),profile_means=cf.mean().to_dict(),
               note='Exploratory isolated 1 GW flat-load case requiring every hour served. Only optimal solver results establish modeled service. Perfect foresight. No grid, reserves, explicit outages or resource limits.')
    dest=ROOT/'experiments';dest.mkdir(exist_ok=True)
    (dest/(job['id']+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    return job['id'],out.get('cost_usd_mwh'),out['status'],out.get('seconds')


def run(job):
    """Record failed validation without accepting partial solver output.

    Each worker returns an outcome, so one assertion does not discard unrelated
    completed cases or stop collection of the remaining submitted jobs.
    """
    started=time.time()
    try:
        return _run(job)
    except AssertionError as error:
        path=ROOT/'inputs'/('profiles_'+job['site']+'.csv')
        frames=traceback.extract_tb(error.__traceback__)
        out={
            'status':'failed_validation',
            'message':'An input, physical or accounting assertion failed; no solution accepted.',
            'validation_error':{
                'type':type(error).__name__,
                'detail':str(error),
                'frames':[{'file':Path(frame.filename).name,'line':frame.lineno,
                           'function':frame.name} for frame in frames]},
            'job':job,
            'profile_sha256':hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None,
            'seconds':round(time.time()-started,2),
            'note':'No cost, capacity, generation or service claim is valid for this failed case. Residual acceptance criteria have not been relaxed.'}
        dest=ROOT/'experiments';dest.mkdir(exist_ok=True)
        (dest/(job['id']+'.json')).write_text(json.dumps(out,indent=2)+'\n')
        return job['id'],None,out['status'],out['seconds']


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--only',nargs='*');args=parser.parse_args()
    jobs=cases()
    (ROOT/'experiment_jobs.json').write_text(json.dumps(jobs,indent=2)+'\n')
    if args.only:jobs=[j for j in jobs if j['id'] in args.only]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for result in as_completed([pool.submit(run,j) for j in jobs]):print(result.result(),flush=True)
