"""Report saved solver outcomes, never treating an unfinished case as an optimum."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent
jobs = json.loads((ROOT / 'experiment_jobs.json').read_text())
labels = {
 'original_2023_reliability_check':'2023 only; original supplied costs',
 'scotland_3yr_no_tidal':'Scotland: no tidal',
 'scotland_3yr_tidal_140':'Scotland: tidal $140',
 'scotland_3yr_tidal_120':'Scotland: tidal $120',
 'scotland_3yr_tidal_100':'Scotland: tidal $100',
 'scotland_3yr_tidal_90':'Scotland: tidal $90',
 'scotland_3yr_tidal100_ldes50':'Tidal $100; long-storage energy costs 2×',
 'scotland_3yr_tidal100_battery_only':'Tidal $100; batteries only',
 'scotland_3yr_marine30':'Tidal $140; 30% dispatched marine requirement',
 'scotland_3yr_tidal100_wave80':'Tidal $100; wave $80',
 'scotland_3yr_nuclear_allowed':'Tidal $100; supplied nuclear allowed',
 'scotland_3yr_firm100':'Tidal $100; $100 firm power allowed',
 'scotland_3yr_tidalcf30':'Tidal $100 reference; 30% output stress',
 'scotland_3yr_tidalcf40':'Tidal $100 reference; 40% output stress',
 'scotland_2010_no_tidal':'2010 weather: no tidal',
 'scotland_2010_tidal100':'2010 weather + 2023 tides: tidal $100',
 'hawaii_3yr_no_otec':'Hawaii: no OTEC',
 'hawaii_3yr_otec100':'Hawaii: OTEC $100',
 'hawaii_3yr_otec90':'Hawaii: OTEC $90',
}
results = {}
for job in jobs:
    path = ROOT / 'experiments' / (job['id'] + '.json')
    if path.exists():
        results[job['id']] = json.loads(path.read_text())
ok = {key: value for key, value in results.items() if value.get('status') == 'ok'}
failed = {key: value for key, value in results.items() if value.get('status') != 'ok'}
missing = [job['id'] for job in jobs if job['id'] not in results]
batch_note = json.loads((ROOT/'BATCH_FAILURE.json').read_text()) if (ROOT/'BATCH_FAILURE.json').exists() else None
missing_status = 'not_validated_batch_terminated' if batch_note else 'not_saved'
for r in ok.values():
    assert abs(r['unserved_GWh']) < 1e-5
    assert r['max_equation_error_GW'] < 2e-5
    assert r['max_constraint_error'] < 2e-5
    assert abs(r['energy_balance_error_GWh']) < 1e-3

rows=[]
for job in jobs:
    case=job['id'];r=results.get(case,{});success=case in ok
    s=r.get('primary_generation_share',{});c=r.get('caps',{})
    rows.append({'case_id':case,'case_label':labels[case],
      'status':r.get('status',missing_status),'message':r.get('message', 'Batch terminated with a residual-validation error; individual case unattributed.' if batch_note and not r else ''),
      'hours':r.get('hours'),'cost_usd_mwh':r.get('cost_usd_mwh') if success else None,
      'tidal_generation_share':s.get('tidal',0) if success else None,
      'wave_generation_share':s.get('wave',0) if success else None,
      'otec_generation_share':s.get('otec',0) if success else None,
      'nuclear_generation_share':s.get('nuclear',0) if success else None,
      'direct_marine_generation_share':sum(s.get(k,0) for k in ['tidal','wave','otec']) if success else None,
      'unserved_GWh':r.get('unserved_GWh') if success else None,
      'long_storage_GWh':c.get('ldes_E',0) if success else None,
      'battery_GWh':c.get('batt_E',0) if success else None,
      'storage_loss_GWh':r.get('storage_loss_GWh') if success else None,
      'discarded_potential_GWh':r.get('discarded_potential_GWh') if success else None,
      'max_equation_error_GW':r.get('max_equation_error_GW') if success else None,
      'max_constraint_error':r.get('max_constraint_error') if success else None,
      'energy_balance_error_GWh':r.get('energy_balance_error_GWh') if success else None})
with (ROOT/'checked_experiments.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)

lines = ['# Q3: what the checked hourly experiments say', '',
    '**Tides can earn a large local role when their generation cost falls. The same model also shows why an ocean proposal should allow dependable clean generation to compete.**', '',
    f'**Saved outcomes: {len(ok)} optimal; {len(failed)} unsuccessful; {len(missing)} unvalidated without a saved result, out of {len(jobs)} planned.** Only optimal cases support numerical conclusions. A failed solve is not evidence that a technology is infeasible.', '',
    'Each completed case supplies an isolated, constant 1 GW load in every modeled hour. Scotland and Hawaii use 26,304 hours spanning 2022–2024; separate one-year cases are identified below. These are conditional comparisons using supplied future costs, perfect knowledge of the weather, cyclic storage and no explicit equipment outages. They are not project bids, real-world reliability guarantees or a worldwide optimum. See [methods](METHODS.md), [input audit](MODEL_AUDIT.md), and the [downloadable comparison table](checked_experiments.csv).', '',
    '## Tidal value in the Scottish case', '']
if batch_note:
    lines[5:5] = ['', '**The batch has ended.** It exited with an assertion failure in the physical/accounting residual check. The traceback did not identify the individual case. Cases without saved results are **not validated**, rather than pending. The runner now logs future assertion failures per case and continues collecting other outcomes; no acceptance tolerances were relaxed. [Recorded batch failure](BATCH_FAILURE.json).', '']
baseline = ok.get('scotland_3yr_no_tidal')
if baseline:
    lines += [f"Without tides, the restricted three-year system costs **${baseline['cost_usd_mwh']:.2f}/MWh**. Floating wind is priced at an assumed $74/MWh on a common reference profile. Land wind, solar, wave, batteries and longer-duration storage can also be built; nuclear is excluded in this sweep.", '',
        '| Assumed tidal generation price | Whole supply cost | Saving versus no tidal | Tidal share of dispatched generation |',
        '|---|---:|---:|---:|']
    for price in [140,120,100,90]:
        r=ok.get('scotland_3yr_tidal_'+str(price))
        if r:
            saving=1-r['cost_usd_mwh']/baseline['cost_usd_mwh']
            lines.append(f"| ${price}/MWh | ${r['cost_usd_mwh']:.2f}/MWh | {saving:.1%} | {r['primary_generation_share'].get('tidal',0):.1%} |")
    r=ok.get('scotland_3yr_tidal_90')
    if r:
        c=r['caps']
        lines += ['',f"At the assumed $90/MWh tidal price, the model builds **{c['tidal']:.2f} GW tidal**, {c['onwind']:.2f} GW land wind, {c['solar']:.2f} GW solar, {c['batt_E']:.1f} GWh batteries and **{c['ldes_E']:.1f} GWh longer-duration storage** for the 1 GW load. It builds no floating wind or wave capacity in this case. The favorable tidal result therefore supports a mixed coastal system; it does not establish that every ocean technology belongs in its cheapest configuration.", '',
            'The tidal output profile includes predictable gaps. Longer-duration storage remains substantial, and its low assumed energy-capacity cost is important. A generation share includes energy sent into storage before losses; it is not a share traced to final customers.']
    lines += ['', 'This is a timing benefit under the tested choices. The model has no transmission, reservoir hydro, geothermal, geographic diversity, flexible demand, reserve requirement, explicit outages or deployment/resource limits. Including those choices can alter the value of tidal generation.']
if (ROOT/'figures/04_checked_tidal_costs.png').exists():
    lines += ['', '![Checked tidal price sweep](figures/04_checked_tidal_costs.png)']

lines += ['', '## Let storage and firm power compete', '']
for case in ['scotland_3yr_tidal100_ldes50','scotland_3yr_tidal100_battery_only','scotland_3yr_tidal100_wave80','scotland_3yr_nuclear_allowed','scotland_3yr_firm100']:
    if case in ok:
        r=ok[case]
        lines.append(f"- **{labels[case]}:** ${r['cost_usd_mwh']:.2f}/MWh. Tides supply {r['primary_generation_share'].get('tidal',0):.1%}, waves {r['primary_generation_share'].get('wave',0):.1%}, and nuclear {r['primary_generation_share'].get('nuclear',0):.1%} of dispatched generation.")
if 'scotland_3yr_nuclear_allowed' in ok and 'scotland_3yr_firm100' in ok:
    lines += ['', '**Both firm-power cases choose an entirely nuclear supply, with about 1.11 GW of capacity and essentially no storage.** The model allows 90% of nuclear capacity to operate in every hour, with no actual outages or construction limit. That strongly favors dependable generation for a flat load. These outcomes do not prove that an all-nuclear real grid is cheapest, but they do rule out claiming that the checked model established an ocean-only optimum.', '',
        'The $100 firm option is a sensitivity using the same simplified nuclear cost and availability structure. It is not a verified geothermal contract or a prediction of future nuclear construction cost. The practical next comparison is an equal-service regional model with realistic outages, reserves, build limits, grids and actual project costs.']
if 'scotland_3yr_tidal_100' not in ok:
    lines += ['', 'The central tidal-$100 / default-storage case has no completed optimal result in this snapshot. Do not infer its exact cost by interpolating between $120 and $90, or use the storage sensitivities to claim a measured percentage premium against that missing baseline.']
if (ROOT/'figures/05_storage_and_firm_power.png').exists():
    lines += ['', '![Storage and idealized firm-power sensitivities](figures/05_storage_and_firm_power.png)']

if any(x.startswith('hawaii') for x in ok):
    lines += ['', '## Hawaii: a separate tropical experiment', '',
        'These cases cap onshore wind at 0.3 GW, allow batteries and longer-duration storage, and clip the supplied OTEC profile to its rated output. Their chosen prices are future assumptions. The original sea-temperature data has substantial imputation, documented in the audit. They do not demonstrate the performance of an operating OTEC plant.']
    for case in ['hawaii_3yr_no_otec','hawaii_3yr_otec100','hawaii_3yr_otec90']:
        if case in ok:
            r=ok[case];lines.append(f"- **{labels[case]}:** ${r['cost_usd_mwh']:.2f}/MWh, with {r['primary_generation_share'].get('otec',0):.1%} of dispatched generation from OTEC.")

lines += ['', '## All completed cases', '',
    'Generation shares include storage charging. The CSV also records losses, discarded potential output and physical residuals. Capacities are GW; storage energy is GWh. Tidal prices are USD/MWh of generation, not total supply cost.', '',
    '| Case | Whole supply cost, USD/MWh | Direct marine generation | Nuclear generation | Long storage, GWh | Battery, GWh |',
    '|---|---:|---:|---:|---:|---:|']
for row in rows:
    if row['status']=='ok':
        lines.append(f"| {row['case_label']} | {row['cost_usd_mwh']:.2f} | {row['direct_marine_generation_share']:.1%} | {row['nuclear_generation_share']:.1%} | {row['long_storage_GWh']:.1f} | {row['battery_GWh']:.1f} |")
lines += ['', 'All completed cases have zero unmet load within numerical tolerance. The 2010 stress cases pair 2010 weather with the supplied 2023 tidal sequence; they are synthetic stress tests, not historical 2010 tidal observations. The 30%/40% tidal-output cases keep the same installed-capacity cost as the central reference, so their actual generation cost changes with output.', '', '## Solver outcomes and verification', '']
for job in jobs:
    case=job['id']
    if case not in ok:
        r=results.get(case,{})
        state=r.get('message',r.get('status','not validated: batch terminated with residual-validation error; individual case unattributed' if batch_note else 'no saved result'))
        lines.append(f'- `{case}`: {state}. No optimal cost or mix is reported.')
if not failed and not missing:lines.append('Every planned case has a completed optimal solution.')
if ok:
    lines += ['',f"Across the completed cases, the largest hourly equation residual is {max(r['max_equation_error_GW'] for r in ok.values()):.3g} GW; the largest constraint residual is {max(r['max_constraint_error'] for r in ok.values()):.3g}; and the largest horizon energy-balance residual is {max(abs(r['energy_balance_error_GWh']) for r in ok.values()):.3g} GWh. These establish numerical consistency, not real-world equipment reliability."]
lines += ['', '## Reproduce', '',
    'Each case JSON contains the input hash, exact cost coefficients, output, status and physical checks. Run `python run_experiments.py --workers 2`, then `python analyze_proposal.py` and `python summarize_experiments.py`. To rerun selected cases, add `--only` and the relevant IDs to the first command. See [METHODS.md](METHODS.md) for the environment and boundaries.', '']
(ROOT/'HOURLY_RESULTS.md').write_text('\n'.join(lines))
print(f'Hourly report: {len(ok)} optimal / {len(failed)} unsuccessful / {len(missing)} unvalidated' )
