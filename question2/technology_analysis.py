"""Reproduce Question 2: published technology comparisons and explicit scale experiments.
Python 3.9+, numpy and matplotlib. This is not an optimized or hourly reliable mix.
"""
from pathlib import Path
import csv, json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
BG='#F3F3E9'; INK='#16332F'; MUTED='#60716A'; GREEN='#007D69'; ORANGE='#BD532F'; BLUE='#6577BE'; GOLD='#B28A37'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.parse_math':False,'figure.facecolor':BG,'axes.facecolor':BG,
 'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'axes.spines.top':False,
 'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#C7D3C4','svg.fonttype':'none','savefig.facecolor':BG})
SOURCES={
 'WEO2025':{'url':'https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf','pages':'417, 423, 429, 453–456','basis':'Published scenarios and regional modeled costs; Annex A CC BY-NC-SA 4.0; Annex B CC BY 4.0'},
 'Lazard2026':{'url':'https://www.lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf','pages':'7, 11 and appendix','basis':'Unsubsidized modeled generation costs; 60% debt at 8%, 40% equity at 12%; nuclear based on Vogtle'},
 'IRENA2026':{'url':'https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025','mirror':'https://tethys-engineering.pnnl.gov/sites/default/files/publications/Dardour-Zamora-2026.pdf','pages':'13–18, 141, 153–156','basis':'2025 USD; commissioned renewable project cost estimates; emerging technology estimates have a different evidence base'},
 'NETL2025':{'url':'https://netl.doe.gov/projects/files/CostandPerformanceBaselineFossilEnergyPlantsVolume1BituminousCoalNaturalGastoElectricity_052125.pdf','pages':'12–18; PDF pages 34–40','basis':'2023 USD; modeled US Midwest plants, 85% utilization; gas $3.42/MMBtu; CO2 transport/storage included'},
 'Nuclear2026':{'url':'https://www.iea.org/reports/global-energy-review-2026/technology-nuclear','basis':'2025 capacity additions and retirements'},
 'GeothermalPotential':{'url':'https://www.iea.org/reports/the-future-of-geothermal-energy/executive-summary','basis':'2024 conditional low-cost case, not a forecast'},
 'Fervo2026':{'url':'https://fervoenergy.com/fervo-energy-declares-commercial-operation-at-cape-station-ahead-of-schedule-leading-the-race-for-next-generation-geothermal-energy/','date':'2026-10-01','basis':'Company reports first 33 MW unit commercial; remaining phase I units not yet commercial'},
 'SMR':{'url':'https://www.iea.org/reports/the-path-to-a-new-era-for-nuclear-energy/executive-summary','basis':'2025 report: 40/120/190 GW in different 2050 cases, included within nuclear, not additional'},
 'OPG':{'url':'https://www.opg.com/wp-content/uploads/2026/03/2025-Q4-OPG-PR-MDA-FS-FINAL.pdf','basis':'First Darlington SMR budget C$7.7bn including shared infrastructure, interest, escalation and contingency'},
 'FusionDOE':{'url':'https://www.energy.gov/articles/energy-department-releases-finalized-fusion-science-and-technology-roadmap-accelerate','date':'2026-06-09','basis':'Development roadmap; commercial electricity is a goal'},
 'CFS':{'url':'https://www.cfs.energy/technology/arc/','basis':'Company target: 400 MW early 2030s; no commercial operating cost'},
 'Helion':{'url':'https://www.helionenergy.com/orion','basis':'Company target: at least 50 MW and initial operations in 2028'},
 'Grids':{'url':'https://www.iea.org/reports/electricity-2026/grids','basis':'Project times: renewables 1–5 years, grids 5–15; scope and permitting matter'}
}
def csvout(name,rows):
 with (ROOT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def clean(ax,axis='x'):
 ax.set_axisbelow(True);ax.grid(axis=axis,color='#D6DFD2',lw=.7);ax.tick_params(axis='y',length=0)
def save(fig,name,title,sub,foot):
 fig.suptitle(title,x=.045,y=.975,ha='left',fontsize=22,fontweight='bold')
 fig.text(.045,.9,sub,ha='left',va='top',fontsize=11,color=MUTED)
 fig.text(.045,.028,foot,ha='left',va='bottom',fontsize=8.5,color=MUTED,linespacing=1.5)
 for ext in ['png','svg']:fig.savefig(FIG/(name+'.'+ext),dpi=180)
 plt.close(fig)
def crf(r,n): return r*(1+r)**n/((1+r)**n-1)

# Two different populations: do not splice averages and ranges into one ranking.
lazard=[('Onshore wind',37,99),('Utility solar',40,98),('Gas combined cycle',51,129),('Solar + storage',61,156),
 ('Conventional geothermal*',67,111),('Coal*',72,177),('Offshore wind',105,167),('New US nuclear**',175,255)]
costs=[{'technology':n,'low_USD_MWh':lo,'high_USD_MWh':hi,'source':'Lazard2026','evidence':'modeled range'} for n,lo,hi in lazard]
csvout('new_build_cost_ranges.csv',costs)
irena=[('Onshore wind',33,976,.36),('Solar PV',44,667,.16),('Hydro',62,2079,.43),('Offshore wind',78,2931,.41),
 ('Bioenergy',86,3606,.78),('Conventional geothermal',89,5997,.85),('Concentrated solar',115,2418,.22)]
csvout('commissioned_renewable_costs.csv',[{'technology':n,'USD2025_MWh':c,'USD2025_kW':k,'capacity_factor':f,'source':'IRENA2026'} for n,c,k,f in irena])
fig,ax=plt.subplots(figsize=(12,8));fig.subplots_adjust(left=.29,right=.92,top=.78,bottom=.24)
for i,(n,lo,hi) in enumerate(lazard):
 col=GREEN if i<2 else BLUE if i in [3,4,6] else ORANGE
 ax.plot([lo,hi],[i,i],color=col,lw=10,solid_capstyle='butt');ax.text(lo-4,i,str(lo),ha='right',va='center');ax.text(hi+4,i,str(hi),va='center')
ax.set_yticks(range(len(lazard)),[r[0] for r in lazard]);ax.invert_yaxis();ax.set_xlim(0,280);clean(ax)
ax.set_xlabel('Generation cost · US dollars per MWh')
save(fig,'01_costs','Solar and wind have the lowest starting costs',
 'These prices buy different patterns of output. Storage and networks must be sized for the same service before choosing a mix.',
 'Source: Lazard LCOE+ v19, July 2026, p. 7. Modeled, unsubsidized new-build ranges; not household electricity prices.\n*Geothermal and coal use older estimates adjusted for inflation. **Nuclear reflects Vogtle 3/4, not every country or existing reactors.\nSolar + storage is not a continuous-power guarantee. Financing: 60% debt at 8%, 40% equity at 12%.')

# Generation in TWh: 2024, 2050 STEPS, 2050 NZE. Solar is PV; wind includes offshore.
gen=[('Solar PV',2073,20374,35509),('Wind',2533,10991,23250),('Hydro',4448,6383,7398),('Fission',2835,5531,6853),
 ('Bioenergy',760,1575,2917),('Concentrated solar',20,245,1209),('Geothermal',100,452,825),('Marine',1,86,112),
 ('Gas without capture',6785,7516,205),('Coal without capture',10797,4569,0),('Oil without capture',757,128,0),
 ('Fossil fuels with capture',1,53,986),('Hydrogen/ammonia generation',0,86,839)]
totals=[31229,58081,80175]
gen.append(('Other / rounding residual',*[totals[j]-sum(r[j+1] for r in gen) for j in range(3)]))
grows=[]
for n,a,b,c in gen:
 grows.append({'technology':n,'generation_2024_TWh':a,'STEPS_2050_TWh':b,'NZE_2050_TWh':c,
  'STEPS_share_percent':b/58081*100,'NZE_share_percent':c/80175*100,'source':'WEO2025 A.3b/c'})
csvout('generation_by_technology.csv',grows)
assert all(sum(r[j+1] for r in gen)==totals[j] for j in range(3))
fig,ax=plt.subplots(figsize=(13,8));fig.subplots_adjust(left=.19,right=.91,top=.76,bottom=.22)
y=np.arange(8)
for j,col,label in [(2,GREEN,'2050 stated policies · 58,081 TWh total'),(3,ORANGE,'2050 net zero · 80,175 TWh total')]:
 vals=[r[j]/1000 for r in gen[:8]];offset=-.17 if j==2 else .17
 ax.barh(y+offset,vals,height=.29,color=col,label=label)
 for i,v in enumerate(vals):ax.text(v+.35,y[i]+offset,f'{v:.2f}' if v<1 else f'{v:.1f}',va='center',fontsize=10)
ax.set_yticks(y,[r[0] for r in gen[:8]]);ax.invert_yaxis();ax.set_xlim(0,42);clean(ax)
ax.set_xlabel('Annual generation · thousand TWh');ax.legend(frameon=False,loc='lower right',fontsize=10)
save(fig,'02_supply_scale','Solar and wind can supply most of the electricity',
 'Together: 54% in the policy case and 73% in the net-zero case. Fission and hydro remain major sources.',
 'Source: IEA WEO 2025, Tables A.3b/c (CC BY-NC-SA 4.0); adaptation. Conditional scenarios, not technical maxima or our optimized mix.\nChart shows eight sources; full data include fossil generation and other sources. SMRs are inside fission; advanced geothermal is inside geothermal.\nThe high-electrification case also replaces fossil output: adding enough for demand growth alone is insufficient.')

capacity=[]
for n,cf in [('Solar',.20),('Onshore wind',.35),('Offshore wind',.45),('Hydro',.45),('Fission',.85),('Geothermal',.85)]:
 capacity.append({'technology':n,'annual_generation_TWh':1000,'assumed_capacity_factor':cf,'electrical_capacity_GW':1000/(8.76*cf),'evidence':'explicit illustration; no hourly matching'})
csvout('equal_output_capacity.csv',capacity)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.21,right=.91,top=.76,bottom=.24)
ax.barh(range(6),[r['electrical_capacity_GW'] for r in capacity],color=[GOLD,BLUE,BLUE,GREEN,ORANGE,GREEN],height=.55)
ax.set_yticks(range(6),[r['technology'] for r in capacity]);ax.invert_yaxis();ax.set_xlim(0,760);clean(ax);ax.set_xlabel('Installed electrical capacity · GW')
for i,r in enumerate(capacity):ax.text(r['electrical_capacity_GW']+10,i,f"{r['electrical_capacity_GW']:.0f} GW at {r['assumed_capacity_factor']:.0%} average output",va='center',fontsize=10)
save(fig,'03_equal_output','The same annual energy needs very different fleets',
 'Each bar produces 1,000 TWh/year: 1.7% of a 60,000 TWh world, or 1.25% of an 80,000 TWh world.',
 'Our calculation: capacity = 1,000 TWh ÷ (8.76 × average output fraction). Fractions shown are assumptions, not universal technology constants.\nSolar capacity is on an AC electrical basis in this illustration. Do not compare directly with a DC module shipment figure.\nThis does not price storage, transmission or spare capacity, and it does not establish equal hourly reliability.')

fleet=[('Solar PV',1625,2164,16209,24201),('Wind',1016,1131,3985,8001),('Fission',415,420,784,1079),('Hydro',1410,1437,2236,2616)]
build=[]
fig,axs=plt.subplots(2,2,figsize=(12,8));fig.subplots_adjust(left=.11,right=.92,top=.74,bottom=.23,hspace=.65,wspace=.36)
for ax,(n,old,base,step,nze) in zip(axs.flat,fleet):
 values=[base-old,(step-base)/26,(nze-base)/26]
 build.append({'technology':n,'net_increase_2024_GW':values[0],'STEPS_average_net_GW_per_year':values[1],'NZE_average_net_GW_per_year':values[2],'source':'WEO2025 same capacity series'})
 ax.barh(range(3),values,color=[MUTED,GREEN,ORANGE],height=.5);ax.set_yticks(range(3),['2024','Policy case','Net-zero case']);ax.invert_yaxis()
 for i,v in enumerate(values):ax.text(v+max(values)*.025,i,f'{v:.0f}',va='center')
 ax.set_xlim(0,max(values)*1.23);ax.set_title(n,loc='left',fontweight='bold');clean(ax);ax.set_xlabel('Net GW added per year',fontsize=10)
csvout('construction_scale.csv',build)
save(fig,'04_build_rates','The construction challenge differs by technology',
 'One historical year compared with average fleet growth needed over 2024–2050. Each panel has its own scale.',
 'Source: IEA WEO 2025, Tables A.3b/c (CC BY-NC-SA 4.0); calculations use the same capacity definitions within each technology.\nThese are NET fleet changes, not gross construction. Replacements, repowering and retirements increase the build requirement.\nA 26-year average is not a forecast for each year; 2024 is a reference year, not a permanent production limit.')

# Nuclear economics: an explicitly assumed completed asset value, not overnight cost.
nuclear=[]
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.12,right=.9,top=.76,bottom=.24)
rates=np.linspace(.03,.12,91)
for cap,col in [(6000,GREEN),(12000,ORANGE)]:
 vals=[cap*crf(r,60)/(8.76*.85)+30 for r in rates]
 ax.plot(rates*100,vals,color=col,lw=3,label=f'${cap:,}/kW completed capital cost')
 for r,v in zip(rates,vals):nuclear.append({'completed_capital_USD_kW':cap,'real_financing_rate':float(r),'life_years':60,'capacity_factor':.85,'operating_USD_MWh':30,'modeled_USD_MWh':float(v)})
ax.axhline(100,color=MUTED,ls='--',lw=1);ax.text(11.8,103,'$100/MWh comparison line',ha='right',fontsize=10)
ax.set_xlabel('Real financing rate · %');ax.set_ylabel('Modeled generation cost · $/MWh');ax.set_ylim(0,250);clean(ax,'y');ax.legend(frameon=False,loc='upper left')
save(fig,'05_nuclear_financing','Nuclear economics depend on the project and financing',
 'An illustrative plant: 60-year life, 85% average output and $30/MWh for fuel, operations and other running costs.',
 'Our sensitivity model, not a quoted project price or a match to Lazard financing. Capital value is measured when the plant enters service.\nConstruction financing, overruns and other provisions must be included in that completed capital value; they are not free.\nAt 7% real financing, doubling completed cost from $6,000 to $12,000/kW raises modeled cost from about $87 to $145/MWh.')
csvout('nuclear_financing.csv',nuclear)

storage=[]
for cycles in [350,52,10]:
 asset_cost=140*(crf(.07,15)+.02)*1000/(.8*.95*cycles)
 storage.append({'full_cycles_per_year':cycles,'installed_USD_kWh':140,'real_rate':.07,'life_years':15,'annual_opex_fraction':.02,
  'usable_fraction':.8,'discharge_efficiency':.95,'round_trip_efficiency':.88,'charging_USD_MWh':40,
  'asset_USD_per_delivered_MWh':asset_cost,'charging_USD_per_delivered_MWh':40/.88,'total_USD_per_delivered_MWh':asset_cost+40/.88})
csvout('storage_use_frequency.csv',storage)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.12,right=.92,top=.76,bottom=.24)
ax.bar(range(3),[r['total_USD_per_delivered_MWh'] for r in storage],width=.48,color=[GREEN,BLUE,ORANGE])
ax.set_xticks(range(3),['350 cycles/year\nAlmost daily','52 cycles/year\nAbout weekly','10 cycles/year\nRare use']);ax.set_ylabel('Cost per MWh discharged from storage · $');ax.set_ylim(0,2850);clean(ax,'y')
for i,r in enumerate(storage):ax.text(i,r['total_USD_per_delivered_MWh']+60,f"${r['total_USD_per_delivered_MWh']:,.0f}",ha='center',fontweight='bold')
save(fig,'06_storage','A battery used rarely is expensive per unit delivered',
 'Same assumed battery cost and lifetime. The cost is spread over very different amounts of discharged electricity.',
 'Illustration using IRENA’s $140/kWh 2025 global four-hour battery cost anchor; other values are our assumptions: 7% real finance, 15 years,\n2% annual operating cost, 80% usable energy, 95% discharge efficiency, 88% round-trip efficiency and $40/MWh charging electricity.\nThis is a cost of stored electricity, not the cost of an entire renewable portfolio. It excludes degradation/augmentation and does not size multi-day storage.')

frontier=[]
for name,cap in [('SMR policy case',40),('SMR stronger-support case',120),('SMR lower-cost case',190)]:
 frontier.append({'case':name,'capacity_GW':cap,'capacity_factor_assumed':.85,'TWh_calculated':cap*8.76*.85,'status':'IEA capacity scenario; our energy conversion; subset of fission'})
frontier.append({'case':'Geothermal low-cost potential','capacity_GW':800,'capacity_factor_assumed':None,'TWh_calculated':6000,'status':'IEA conditional market-potential study; approximate; not a WEO scenario increment'})
fusion={'share_of_80000_assumed':.01,'TWh_target':800,'capacity_factor_assumed':.85,'required_GW':800/(8.76*.85)}
fusion['required_400MW_plants_rounded_up']=math.ceil(fusion['required_GW']/.4)
fusion['annual_net_GW_if_built_2035_2050']=fusion['required_GW']/15
csvout('emerging_scale_cases.csv',frontier)
netl=[{'configuration':n,'no_capture_USD2023_MWh':a,'capture_95pct_USD2023_MWh':b,'capture_premium_percent':100*(b/a-1),
 'source':'NETL2025 ES-6; includes CO2 transport/storage; 85% CF; gas $3.42/MMBtu'} for n,a,b in [('F-class',47,84.3),('H-class 1x1',44.5,81.5),('H-class 2x1',41.9,77.8)]]
csvout('gas_carbon_capture.csv',netl)
regional_nuclear=[{'region':n,'2024_modeled_USD_MWh':v,'source':'WEO2025 B.4b; repeat-build assumption, not completed project audit'} for n,v in [('United States',110),('European Union',165),('China',70),('India',75)]]
csvout('regional_nuclear_costs.csv',regional_nuclear)
result={'as_of':'2026-10-24','sources':SOURCES,'generation':grows,'totals':totals,'equal_output':capacity,'construction':build,
 'lazard':costs,'irena':irena,'regional_nuclear':regional_nuclear,'storage':storage,'frontier':frontier,'fusion_scale_illustration':fusion,
 'netl':netl,'solar_wind_shares':{'STEPS':(20374+10991)/58081,'NZE':(35509+23250)/80175},
 'old_candidate_review':{'nuclear_15pct_of_80000_TWh':12000,'required_nuclear_GW_at_85pct':12000/(8.76*.85),
 'average_net_nuclear_GW_year':(12000/(8.76*.85)-420)/26,'geothermal_2pct_of_80000_TWh':1600},
 'limitations':['No optimal mix or hourly reliability result','Scenario output is not a maximum or probability','Costs have different years, regions and evidence bases',
 'Construction comparisons use net fleet changes; gross builds must replace retirements','No invented fusion commercial price or required output','No additive double count of SMRs, advanced geothermal or storage']}
(ROOT/'technology_results.json').write_text(json.dumps(result,indent=2)+'\n')
for r in capacity: assert math.isclose(r['electrical_capacity_GW']*8.76*r['assumed_capacity_factor'],1000)
assert all(r['capture_95pct_USD2023_MWh']>r['no_capture_USD2023_MWh'] for r in netl)
assert all(storage[i]['total_USD_per_delivered_MWh']<storage[i+1]['total_USD_per_delivered_MWh'] for i in range(2))
print(json.dumps({'figures':6,'solar_wind_shares':result['solar_wind_shares'],'fusion_scale':fusion,'old_candidate_review':result['old_candidate_review'],'storage':storage},indent=2))
