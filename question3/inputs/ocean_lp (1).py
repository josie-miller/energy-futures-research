import numpy as np, pandas as pd, scipy.sparse as sp, time, json, sys
from scipy.optimize import linprog
def ann(capex, life, fom_frac, r=0.07): crf=r*(1+r)**life/((1+r)**life-1); return capex*(crf+fom_frac)

def lc2fix(lcoe, cf): return lcoe*cf*8.76   # $/MWh at reference CF -> $/kW-yr

def solve(cf, costs, demand=1.0, techs=None, allow=("batt","ldes","nuc"), voll=5000., min_ocean=None, ocean_set=("tidal","wave","otec"),
          fix_caps=None, cap_max=None, eta_b=0.94, eta_l=0.63, nuc_av=0.90, verbose=False):
    T=len(cf); ny=T/8760.; techs=techs or list(cf.columns); K=len(techs)
    CF=cf[techs].values
    names=list(techs)+["batt_E","batt_P","ldes_E","ldes_P","nuc"]; nC=len(names)
    H=["bc","bd","bs","lc","ld","ls","nu","un"]; nH=len(H)
    N=nC+nH*T; idx=lambda h,t: nC+H.index(h)*T+t
    c=np.zeros(N)
    for i,n in enumerate(techs): c[i]=costs[n]
    c[K]=costs['batt_E']; c[K+1]=costs['batt_P']; c[K+2]=costs['ldes_E']; c[K+3]=costs['ldes_P']; c[K+4]=costs['nuc_fix']
    c[idx('nu',0):idx('nu',0)+T]=costs['nuc_var']/1000/ny   # GW*h * $/MWh -> $k? keep units: cap in GW, cost $/kW-yr => $M/yr per GW*1000... normalise below
    c[idx('un',0):idx('un',0)+T]=voll/1000/ny
    # units: capacity in GW, fixed cost $/kW-yr*1e6 kW/GW => $M/yr = costs*1 ; hourly GWh*$/MWh*1000 MWh/GWh => $k -> /1000 => $M
    rows=[];cols=[];vals=[]; bu=[]; r=0
    ar=np.arange(T)
    # balance: -(sum cf cap + bd - bc + ld - lc + nu + un) <= -D
    for i in range(K):
        rows+=list(r+ar); cols+=[i]*T; vals+=list(-CF[:,i])
    for h,s in (("bd",-1),("bc",1),("ld",-1),("lc",1),("nu",-1),("un",-1)):
        rows+=list(r+ar); cols+=list(idx(h,0)+ar); vals+=[s]*T
    bu+=[-demand]*T; r+=T
    def bound(h,capcol,mult=1.0):
        nonlocal r
        rows.extend(r+ar); cols.extend(idx(h,0)+ar); vals.extend([1.0]*T)
        rows.extend(r+ar); cols.extend([capcol]*T); vals.extend([-mult]*T); bu.extend([0.0]*T); r+=T
    bound("bs",K); bound("bc",K+1); bound("bd",K+1); bound("ls",K+2); bound("lc",K+3); bound("ld",K+3); bound("nu",K+4,nuc_av)
    A_ub=sp.csr_matrix((vals,(rows,cols)),shape=(r,N))
    # storage dynamics (cyclic)
    rows=[];cols=[];vals=[]; re=0
    prev=np.roll(ar,1)
    for s_,c_,d_,eta in (("bs","bc","bd",eta_b),("ls","lc","ld",eta_l)):
        rows+=list(re+ar); cols+=list(idx(s_,0)+ar); vals+=[1.0]*T
        rows+=list(re+ar); cols+=list(idx(s_,0)+prev); vals+=[-1.0]*T
        rows+=list(re+ar); cols+=list(idx(c_,0)+ar); vals+=[-eta]*T
        rows+=list(re+ar); cols+=list(idx(d_,0)+ar); vals+=[1/eta]*T
        re+=T
    A_eq=sp.csr_matrix((vals,(rows,cols)),shape=(re,N)); b_eq=np.zeros(re)
    if min_ocean:
        oc=[techs.index(o) for o in ocean_set if o in techs]
        row=np.zeros(N); row[oc]=-CF[:,oc].sum(0)
        A_ub=sp.vstack([A_ub,sp.csr_matrix(row)]); bu.append(-min_ocean*demand*T)
    bnds=[(0,None)]*N
    if "batt" not in allow: bnds[K]=bnds[K+1]=(0,0)
    if "ldes" not in allow: bnds[K+2]=bnds[K+3]=(0,0)
    if "nuc" not in allow: bnds[K+4]=(0,0)
    if fix_caps:
        for n,v_ in fix_caps.items(): j=names.index(n); bnds[j]=(v_,v_)
    if cap_max:
        for n,v_ in cap_max.items(): j=names.index(n); bnds[j]=(0,v_)
    t0=time.time()
    res=linprog(c,A_ub=A_ub,b_ub=np.array(bu),A_eq=A_eq,b_eq=b_eq,bounds=bnds,method="highs",options={"presolve":True})
    if res.status!=0: return {"status":res.message}
    x=res.x; caps={n:x[i] for i,n in enumerate(names)}
    hv={h:x[idx(h,0):idx(h,0)+T] for h in H}
    avail=CF*np.array([caps[n] for n in techs])
    use=demand+hv['bc']+hv['lc']-hv['bd']-hv['ld']-hv['nu']-hv['un']
    tot=avail.sum(1); share_h=np.where(tot>0,np.clip(use/np.maximum(tot,1e-9),0,1),0)
    deliv=(avail*share_h[:,None]).sum(0)/T   # GW avg delivered (incl. energy routed via storage)
    gen={n:deliv[i]/demand for i,n in enumerate(techs)}; gen['nuclear']=hv['nu'].mean()/demand; gen['unserved']=hv['un'].mean()/demand
    curt=1-(avail*share_h[:,None]).sum()/max(avail.sum(),1e-9)
    cost=res.fun  # $M per year for 1 GW avg load -> $/MWh = cost*1e6/(8760*1000)
    return {"status":"ok","cost_usd_mwh":cost*1e6/(demand*8.76e6),"caps_GW":caps,"energy_share":gen,"curtail":curt,"secs":round(time.time()-t0,1),
            "hourly":hv}

def brief(o):
    if o.get('status')!='ok': return {"status":str(o.get('status'))}
    return dict(status="ok",cost=o['cost_usd_mwh'], caps={k:float(v) for k,v in o['caps_GW'].items()},
                share={k:float(v) for k,v in o['energy_share'].items()}, curt=float(o['curtail']), secs=o['secs'])
def run(job):
    site,year,cost_key,overrides,kw,label=job
    cf=pd.read_csv(f"ocean_model/profiles_{site}.csv",index_col=0,parse_dates=True)
    cf=cf.loc[year] if year else cf
    costs=dict(json.load(open("ocean_model/costs.json"))[cost_key]); costs.update(overrides)
    o=solve(cf,costs,**kw); b=brief(o); b.update(label=label,site=site,year=year,cost_key=cost_key,overrides=overrides,kw={k:(list(v) if isinstance(v,(tuple,list)) else v) for k,v in kw.items()})
    return b
if __name__=="__main__":
    import multiprocessing as mp
    jobs=json.load(open(sys.argv[1])); nproc=int(sys.argv[3]) if len(sys.argv)>3 else 5
    with mp.Pool(nproc) as p: res=p.map(run,[tuple(j) for j in jobs],chunksize=1)
    json.dump(res,open(sys.argv[2],"w"),indent=1)
    print("done",len(res))
