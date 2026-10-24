"""Small physical/accounting checks, independent of the research conclusions."""
import pandas as pd
from ocean_model_checked import solve

c={'solar':43.8,'tidal':87.6,'batt_E':1.,'batt_P':1.,'ldes_E':1.,
   'ldes_P':1.,'nuc_fix':1000.,'nuc_var':12.}
r=solve(pd.DataFrame({'solar':[.5]*24}),c,allow=())
assert abs(r['caps']['solar']-2)<1e-7 and abs(r['cost_usd_mwh']-10)<1e-7
assert r['unserved_GWh']==0 and r['storage_loss_GWh']==0
r=solve(pd.DataFrame({'solar':[1.,0.]}),c,allow=('batt',),rte_b=.81)
assert abs(r['caps']['solar']-(1+1/.81))<1e-7
assert abs(r['caps']['batt_E']-1/.9)<1e-7
assert abs(r['storage_loss_GWh']-(1/.81-1))<1e-7
r=solve(pd.DataFrame({'solar':[0.,0.]}),c,allow=())
assert r['status']=='failed'
r=solve(pd.DataFrame({'solar':[0.,0.]}),c,allow=(),max_unserved_fraction=1)
assert abs(r['unserved_GWh']-2)<1e-7 and abs(r['cost_usd_mwh']-5000)<1e-6
r=solve(pd.DataFrame({'solar':[1.]*24,'tidal':[1.]*24}),c,allow=(),min_marine_generation_share=.3)
assert abs(r['primary_generation_share']['tidal']-.3)<1e-7
assert abs(r['generation_GWh']['tidal']-7.2)<1e-7
print('Passed: capacity/cost units, storage losses, strict reliability, explicit unmet load, dispatched marine share.')
