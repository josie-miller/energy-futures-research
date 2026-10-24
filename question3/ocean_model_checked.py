"""Transparent hourly experiment, not a validated regional power-system forecast.

Capacities: GW generation/power, GWh storage energy. Fixed costs: USD/kW-year
or USD/kWh-year. Variable costs: USD/MWh. Hourly demand: GW.
Generation is explicit, so discarded potential output cannot satisfy a marine
generation-share constraint. All demand must be served by default.
"""
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
import time
from types import SimpleNamespace
import highspy


def optimize(c, A_ub, b_ub, A_eq, b_eq, bounds):
    """Current HiGHS simplex solver, with one thread per process.

    The primal solution, objective and physical residuals are retained/checked.
    Single-thread operation avoids monopolizing a shared research workstation.
    """
    A=sp.vstack([A_ub,A_eq],format='csc')
    lp=highspy.HighsLp();lp.num_col_=len(c);lp.num_row_=A.shape[0]
    lp.col_cost_=c;lp.col_lower_=[b[0] for b in bounds]
    lp.col_upper_=[b[1] if b[1] is not None else highspy.kHighsInf for b in bounds]
    lp.row_lower_=np.r_[np.full(len(b_ub),-highspy.kHighsInf),b_eq]
    lp.row_upper_=np.r_[b_ub,b_eq]
    lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=A.indptr;lp.a_matrix_.index_=A.indices;lp.a_matrix_.value_=A.data
    h=highspy.Highs()
    for key,value in [('output_flag',False),('threads',1),('solver','simplex'),
                      ('time_limit',600.)]:
        assert h.setOptionValue(key,value)==highspy.HighsStatus.kOk,(key,value)
    h.passModel(lp);h.run();status=h.getModelStatus()
    return SimpleNamespace(success=status==highspy.HighsModelStatus.kOptimal,
                           message=h.modelStatusToString(status),x=np.asarray(h.getSolution().col_value),
                           fun=h.getInfo().objective_function_value)


def solve_explicit(cf, costs, demand=1.0, allow=("batt", "ldes", "nuc"),
          rte_b=0.94**2, rte_l=0.63**2, nuclear_availability=0.90,
          max_unserved_fraction=0.0, voll=5000., min_marine_generation_share=None,
          marine=("tidal", "wave", "otec"), cap_max=None, fix_caps=None):
    """Minimize annualized costs with cyclic storage and perfect foresight.

    The marine share is of dispatched primary generation (including electricity
    sent into storage), not final customer supply. Nuclear availability must be
    an hourly series to represent actual outages; its scalar default is only a
    simplified sensitivity case. No transmission, reserves or build limits are
    implied. These need explicit additional data.
    """
    techs = list(cf.columns)
    profile = np.asarray(cf, dtype=float)
    T, K = profile.shape
    D = np.broadcast_to(np.asarray(demand, dtype=float), (T,)).copy()
    av = np.broadcast_to(np.asarray(nuclear_availability, dtype=float), (T,))
    assert T > 0 and K > 0 and np.isfinite(profile).all()
    assert ((profile >= 0) & (profile <= 1)).all()
    assert np.isfinite(D).all() and (D > 0).all()
    assert np.isfinite(av).all() and ((av >= 0) & (av <= 1)).all()
    assert 0 < rte_b <= 1 and 0 < rte_l <= 1
    assert 0 <= max_unserved_fraction <= 1
    if min_marine_generation_share is not None:
        assert 0 <= min_marine_generation_share <= 1
    names = techs + ['batt_E', 'batt_P', 'ldes_E', 'ldes_P', 'nuc']
    nC = len(names)
    hours = ['bc', 'bd', 'bs', 'lc', 'ld', 'ls', 'nu', 'un']
    n = nC + (K + len(hours))*T
    g_indices = [nC+j*T+np.arange(T) for j in range(K)]
    h_indices = {h:nC+K*T+i*T+np.arange(T) for i,h in enumerate(hours)}
    gi = lambda j: g_indices[j]
    hi = lambda h: h_indices[h]
    c = np.zeros(n)
    ny = T/8760.
    for i, name in enumerate(names):
        c[i] = costs['nuc_fix'] if name == 'nuc' else costs[name]
        assert c[i] >= 0
    c[hi('nu')] = costs['nuc_var']/1000/ny
    c[hi('un')] = voll/1000/ny
    ur, uc, uv, ub = [], [], [], []
    def upper(cols, vals, rhs):
        row = len(ub)
        ur.extend([row]*len(cols)); uc.extend(cols); uv.extend(vals); ub.append(rhs)
    for j in range(K):
        for t in range(T):
            upper([int(gi(j)[t]), j], [1., -profile[t,j]], 0.)
    for h, cap in [('bs','batt_E'),('bc','batt_P'),('bd','batt_P'),
                   ('ls','ldes_E'),('lc','ldes_P'),('ld','ldes_P'),('nu','nuc')]:
        jj=names.index(cap); ix=hi(h)
        for t in range(T):
            upper([int(ix[t]), jj], [1., -av[t] if h == 'nu' else -1.], 0.)
    if max_unserved_fraction > 0:
        upper(hi('un').tolist(), [1.]*T, max_unserved_fraction*D.sum())
    if min_marine_generation_share is not None:
        f = min_marine_generation_share
        cols, vals = [], []
        for j, name in enumerate(techs):
            cols.extend(gi(j).tolist()); vals.extend([f-(1 if name in marine else 0)]*T)
        cols.extend(hi('nu').tolist()); vals.extend([f]*T)
        upper(cols, vals, 0.)
    er, ec, ev, eb = [], [], [], []
    def equal(cols, vals, rhs):
        row=len(eb)
        er.extend([row]*len(cols)); ec.extend(cols); ev.extend(vals); eb.append(rhs)
    gens = [gi(j) for j in range(K)]
    hh = {h:hi(h) for h in hours}
    for t in range(T):
        cols=[int(g[t]) for g in gens]; vals=[1.]*K
        for h, sign in [('bd',1),('bc',-1),('ld',1),('lc',-1),('nu',1),('un',1)]:
            cols.append(int(hh[h][t]));vals.append(sign)
        equal(cols, vals, D[t])
    for s, ch, dis, eta in [('bs','bc','bd',rte_b**.5),('ls','lc','ld',rte_l**.5)]:
        for t in range(T):
            equal([int(hh[s][t]),int(hh[s][(t-1)%T]),int(hh[ch][t]),int(hh[dis][t])],
                  [1.,-1.,-eta,1/eta],0.)
    Aeq=sp.csr_matrix((ev,(er,ec)),shape=(len(eb),n))
    Aub=sp.csr_matrix((uv,(ur,uc)),shape=(len(ub),n))
    bounds=[(0,None)]*n
    for kind, asset in [('batt',['batt_E','batt_P']),('ldes',['ldes_E','ldes_P']),('nuc',['nuc'])]:
        if kind not in allow:
            for name in asset: bounds[names.index(name)]=(0,0)
    if max_unserved_fraction == 0:
        for j in hi('un'): bounds[j]=(0,0)
    for name, value in (cap_max or {}).items(): bounds[names.index(name)]=(0,value)
    for name, value in (fix_caps or {}).items(): bounds[names.index(name)]=(value,value)
    started=time.time()
    res=optimize(c,Aub,ub,Aeq,eb,bounds)
    if not res.success:
        return {'status':'failed','message':res.message,'seconds':time.time()-started}
    x=res.x; caps={name:max(0.,float(x[i])) for i,name in enumerate(names)}
    hv={h:x[hi(h)] for h in hours}
    generation={name:x[gi(j)] for j,name in enumerate(techs)}
    energy={name:float(g.sum()) for name,g in generation.items()}
    energy['nuclear']=float(hv['nu'].sum())
    primary=sum(energy.values())
    potential=float((profile*np.array([caps[name] for name in techs])).sum())
    used=sum(energy[name] for name in techs)
    losses=float((hv['bc']+hv['lc']-hv['bd']-hv['ld']).sum())
    gap=primary-(D.sum()-hv['un'].sum()+losses)
    eq_error=float(np.max(np.abs(Aeq@x-np.array(eb))))
    ub_error=float(max(0.,np.max(Aub@x-np.array(ub))))
    assert eq_error < 2e-5 and ub_error < 2e-5 and abs(gap) < 1e-4
    assert hv['un'].sum() <= max_unserved_fraction*D.sum()+1e-5
    return {'status':'ok','cost_usd_mwh':float(res.fun*1000/(D.sum()/ny)),
            'caps':caps,'generation_GWh':energy,
            'primary_generation_share':{k:(v/primary if primary > 0 else None) for k,v in energy.items()},
            'demand_GWh':float(D.sum()),'unserved_GWh':float(hv['un'].sum()),
            'storage_loss_GWh':losses,'discarded_potential_GWh':potential-used,
            'max_equation_error_GW':eq_error,'max_constraint_error':ub_error,
            'energy_balance_error_GWh':float(gap),'seconds':round(time.time()-started,2),
            'hourly':hv,'generation_hourly':generation}


def serializable(result):
    return {k:v for k,v in result.items() if k not in ['hourly','generation_hourly']}


def solve(cf, costs, demand=1.0, allow=("batt","ldes","nuc"),
          rte_b=.94**2, rte_l=.63**2, nuclear_availability=.9,
          max_unserved_fraction=0., voll=5000., min_marine_generation_share=None,
          marine=("tidal","wave","otec"), cap_max=None, fix_caps=None):
    """Smaller equivalent cost formulation when no generation-share rule applies.

    Renewable curtailment is implicit in the hourly balance inequality. The
    accounting convention allocates used renewable output pro rata across
    available technologies each hour. This attribution is not a unique dispatch.
    Use the explicit formulation for rules about dispatched marine generation.
    """
    if min_marine_generation_share is not None:
        return solve_explicit(cf,costs,demand,allow,rte_b,rte_l,nuclear_availability,
             max_unserved_fraction,voll,min_marine_generation_share,marine,cap_max,fix_caps)
    CF=np.asarray(cf,dtype=float);T,K=CF.shape; techs=list(cf.columns);ny=T/8760.
    D=np.broadcast_to(np.asarray(demand,dtype=float),(T,)); av=np.broadcast_to(np.asarray(nuclear_availability,dtype=float),(T,))
    assert np.isfinite(CF).all() and ((CF>=0)&(CF<=1)).all()
    assert (D>0).all() and np.isfinite(D).all() and ((av>=0)&(av<=1)).all()
    assert 0<rte_b<=1 and 0<rte_l<=1 and 0<=max_unserved_fraction<=1
    names=techs+['batt_E','batt_P','ldes_E','ldes_P','nuc'];nC=len(names)
    H=['bc','bd','bs','lc','ld','ls','nu','un'];N=nC+len(H)*T;ar=np.arange(T)
    ix={h:nC+i*T+ar for i,h in enumerate(H)}
    c=np.zeros(N)
    for i,name in enumerate(names):c[i]=costs['nuc_fix'] if name=='nuc' else costs[name]
    assert (c>=0).all()
    c[ix['nu']]=costs['nuc_var']/1000/ny;c[ix['un']]=voll/1000/ny
    rows=[];cols=[];vals=[];bu=[];r=0
    for i in range(K):
        rows.extend(ar);cols.extend([i]*T);vals.extend(-CF[:,i])
    for h,s in [('bd',-1),('bc',1),('ld',-1),('lc',1),('nu',-1),('un',-1)]:
        rows.extend(ar);cols.extend(ix[h]);vals.extend([s]*T)
    bu.extend(-D);r+=T
    for h,cap in [('bs','batt_E'),('bc','batt_P'),('bd','batt_P'),('ls','ldes_E'),('lc','ldes_P'),('ld','ldes_P'),('nu','nuc')]:
        rows.extend(r+ar);cols.extend(ix[h]);vals.extend([1.]*T)
        rows.extend(r+ar);cols.extend([names.index(cap)]*T);vals.extend(-av if h=='nu' else [-1.]*T)
        bu.extend([0.]*T);r+=T
    if max_unserved_fraction>0:
        rows.extend([r]*T);cols.extend(ix['un']);vals.extend([1.]*T);bu.append(max_unserved_fraction*D.sum());r+=1
    Aub=sp.csr_matrix((vals,(rows,cols)),shape=(r,N))
    rows=[];cols=[];vals=[];r=0;prev=np.roll(ar,1)
    for s,ch,dis,eta in [('bs','bc','bd',rte_b**.5),('ls','lc','ld',rte_l**.5)]:
        for indices,coef in [(ix[s],1.),(ix[s][prev],-1.),(ix[ch],-eta),(ix[dis],1/eta)]:
            rows.extend(r+ar);cols.extend(indices);vals.extend([coef]*T)
        r+=T
    Aeq=sp.csr_matrix((vals,(rows,cols)),shape=(r,N))
    bounds=[(0,None)]*N
    for kind,assets in [('batt',['batt_E','batt_P']),('ldes',['ldes_E','ldes_P']),('nuc',['nuc'])]:
        if kind not in allow:
            for name in assets:bounds[names.index(name)]=(0,0)
    if max_unserved_fraction==0:
        for i in ix['un']:bounds[i]=(0,0)
    for name,v in (cap_max or {}).items():bounds[names.index(name)]=(0,v)
    for name,v in (fix_caps or {}).items():bounds[names.index(name)]=(v,v)
    started=time.time()
    res=optimize(c,Aub,bu,Aeq,np.zeros(r),bounds)
    if not res.success:return {'status':'failed','message':res.message,'seconds':round(time.time()-started,2)}
    x=res.x;hv={h:x[ix[h]] for h in H};caps={name:max(0.,float(x[i])) for i,name in enumerate(names)}
    available=CF*np.array([caps[n] for n in techs])
    use=D+hv['bc']+hv['lc']-hv['bd']-hv['ld']-hv['nu']-hv['un']
    ratio=np.clip(use/np.maximum(available.sum(1),1e-9),0,1)
    generation={name:available[:,i]*ratio for i,name in enumerate(techs)}
    energy={name:float(v.sum()) for name,v in generation.items()};energy['nuclear']=float(hv['nu'].sum())
    primary=sum(energy.values());losses=float((hv['bc']+hv['lc']-hv['bd']-hv['ld']).sum())
    gap=primary-(D.sum()-hv['un'].sum()+losses)
    eq_error=float(np.max(np.abs(Aeq@x)));ub_error=float(max(0.,np.max(Aub@x-np.asarray(bu))))
    assert eq_error<2e-5 and ub_error<2e-5 and abs(gap)<1e-3
    assert hv['un'].sum()<=max_unserved_fraction*D.sum()+1e-5
    return {'status':'ok','cost_usd_mwh':float(res.fun*1000/(D.sum()/ny)),
        'caps':caps,'generation_GWh':energy,'primary_generation_share':{k:(v/primary if primary>0 else None) for k,v in energy.items()},
        'demand_GWh':float(D.sum()),'unserved_GWh':float(hv['un'].sum()),'storage_loss_GWh':losses,
        'discarded_potential_GWh':float(available.sum()-sum(energy[n] for n in techs)),
        'max_equation_error_GW':eq_error,'max_constraint_error':ub_error,'energy_balance_error_GWh':float(gap),
        'seconds':round(time.time()-started,2),'hourly':hv,'generation_hourly':generation,
        'attribution':'Used renewable generation attributed pro rata to available output each hour; not unique dispatch.'}
