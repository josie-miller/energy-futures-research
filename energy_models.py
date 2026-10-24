"""Reproduce the Energy Futures calculations and seven research figures.

Python 3.9+, numpy, matplotlib. Run: python energy_models.py
Inputs are source transcriptions or explicitly labelled design assumptions.
This is a scale/cost sensitivity model, not hourly grid optimization.
"""
from pathlib import Path
import csv
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

OUT = Path(__file__).resolve().parent
CHARTS = OUT / 'charts'
CHARTS.mkdir(exist_ok=True)
BG, INK, MUTED = '#F3F3E9', '#16332F', '#60716A'
GREEN, BLUE, ORANGE, GOLD, PURPLE = '#007D69', '#6577BE', '#BD532F', '#B28A37', '#8A688E'
COLORS = [GOLD, BLUE, GREEN, '#569DAD', PURPLE]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.color':INK,
 'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,
 'axes.facecolor':BG,'figure.facecolor':BG,'axes.edgecolor':'#CCD6CB',
 'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,
 'svg.fonttype':'none','savefig.facecolor':BG})

SOURCES = {
 'weo': {'url':'https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf',
  'pages':'423, 429, 437; 2024 fleet capacity on page 423',
  'title':'IEA World Energy Outlook 2025, Annex A', 'license':'Annex A: CC BY-NC-SA 4.0'},
 'lazard':{'url':'https://lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf','pages':'7 and associated notes','title':'Lazard LCOE+ v19, July 2026'},
 'irena':{'url':'https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025',
  'pages':'153–156','title':'IRENA Renewable Power Generation Costs in 2025, published 2026'},
 'nasa_mars':{'url':'https://www.nasa.gov/wp-content/uploads/2025/02/iparch07-wp-mars-surface-power.pdf',
  'pages':'2 and 6','title':'NASA Mars Surface Power, February 2025'},
 'leo':{'url':'https://www.nasa.gov/wp-content/uploads/2023/05/162182main-sts-116-press-kit.pdf','title':'NASA STS-116 press kit; representative 35-minute eclipse'},
 'moon':{'url':'https://www.nasa.gov/lunar-surface-technology/','title':'NASA Lunar Surface Technology; approximately 14-day night'},
 'mars_day':{'url':'https://science.nasa.gov/mars/facts/','title':'NASA Mars facts; 24.6-hour sol'}
}
def save(fig, name, title, subtitle, foot):
 fig.suptitle(title, x=.04, y=.97, ha='left', fontsize=23, fontweight='bold')
 fig.text(.04,.905,subtitle,ha='left',va='top',fontsize=11,color=MUTED)
 fig.text(.04,.035,foot,ha='left',va='bottom',fontsize=8.5,color=MUTED,linespacing=1.5)
 fig.savefig(CHARTS/(name+'.png'),dpi=180)
 fig.savefig(CHARTS/(name+'.svg'))
 plt.close(fig)
def csvout(name, rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def clean(ax):
 ax.set_axisbelow(True);ax.grid(axis='x',color='#D9E0D6',linewidth=.7)
 ax.tick_params(axis='y',length=0)
 ax.xaxis.set_major_formatter(FuncFormatter(lambda x,p:f'{x:,.0f}'))

# Published scenario values. Do not splice the revised July 2026 demand baseline into WEO.
demand = [
 {'case':'2024 actual','generation_TWh':31229,'electricity_demand_TWh':27290},
 {'case':'2050 stated policies','generation_TWh':58081,'electricity_demand_TWh':49657},
 {'case':'2050 current policies','generation_TWh':59426,'electricity_demand_TWh':50667},
 {'case':'2050 net-zero pathway','generation_TWh':80175,'electricity_demand_TWh':None},
]
regions = [('China',9102,16131),('India',1644,4803),('Southeast Asia',1317,3197),
 ('European Union',2437,4178),('United States',4102,5647),('Africa',753,2197)]
regions.append(('Rest of world',27290-sum(x[1] for x in regions),49657-sum(x[2] for x in regions)))
regional=[{'region':n,'demand_2024_TWh':a,'demand_2050_TWh':b,'increase_TWh':b-a} for n,a,b in regions]
assert sum(x['increase_TWh'] for x in regional)==22367
fig,axs=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1,1.05]})
fig.subplots_adjust(left=.19,right=.94,top=.78,bottom=.22,wspace=.78)
ax=axs[0];y=np.arange(4)
ax.barh(y,[x['generation_TWh']/1000 for x in demand],color=[MUTED,GREEN,BLUE,ORANGE],height=.54)
ax.set_yticks(y,[x['case'].replace('2050 ','2050\n') for x in demand]);ax.invert_yaxis();ax.set_xlim(0,98)
for i,r in enumerate(demand):ax.text(r['generation_TWh']/1000+1,i,f"{r['generation_TWh']/1000:.1f}",va='center',fontweight='bold')
ax.set_xlabel('Generation · thousand TWh/year');clean(ax)
ax=axs[1];y=np.arange(len(regional));ax.barh(y,[r['increase_TWh'] for r in regional],color=GREEN,height=.6)
ax.set_yticks(y,[r['region'] for r in regional]);ax.invert_yaxis();ax.set_xlim(0,8500)
for i,r in enumerate(regional):ax.text(r['increase_TWh']+90,i,f"{r['increase_TWh']:,}",va='center',fontsize=10)
ax.set_xlabel('Added demand, 2024–2050 · TWh/year');clean(ax)
save(fig,'01_demand','Build for much more electricity','Left: published world generation cases. Right: where demand grows in the stated-policies case.',
 'Source: IEA World Energy Outlook 2025, Annex A, pp. 423, 429, 437 (CC BY-NC-SA 4.0); adapted calculations.\nGeneration includes more than end-user demand. Policy cases and the net-zero pathway have different assumptions; this is not a probability range.')
csvout('published_demand.csv',demand);csvout('regional_growth.csv',regional)

costs=[('Onshore wind',37,99),('Utility solar',40,98),('Gas combined cycle',51,129),
 ('Solar + storage',61,156),('Geothermal*',67,111),('Offshore wind',105,167),('New US nuclear**',175,255)]
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.24,right=.91,top=.78,bottom=.24)
for i,(n,lo,hi) in enumerate(costs):
 col=GREEN if i in [0,1] else BLUE if i in [3,4,5] else ORANGE
 ax.plot([lo,hi],[i,i],color=col,lw=12,solid_capstyle='butt')
 ax.text(lo-4,i,f'{lo}',va='center',ha='right',fontsize=11);ax.text(hi+4,i,f'{hi}',va='center',fontsize=11)
ax.set_yticks(range(len(costs)),[x[0] for x in costs]);ax.invert_yaxis();ax.set_xlim(0,280);ax.set_xlabel('Unsubsidized generation cost · US dollars per MWh');clean(ax)
save(fig,'02_generation_cost','Solar and wind start cheap. Reliability costs more.','These ranges price generation. They do not buy the same hours of service.',
 'Source: Lazard LCOE+ v19, July 2026, p. 7. Solar + storage is not a guarantee of continuous supply.\n*Geothermal uses older estimates adjusted for inflation. **US nuclear is based on Vogtle 3 & 4; it does not describe all countries or existing reactors.\nCommon financing basis: 60% debt at 8%, 40% equity at 12%. Network, reliability and emissions differences still need a system comparison.')
csvout('generation_costs.csv',[{'technology':n,'low_USD_MWh':lo,'high_USD_MWh':hi,'source':'Lazard 2026 p7'} for n,lo,hi in costs])

# Our candidate is a transparent annual energy budget; shares are not optimized results.
# Capacity factor = average output / rated power. Capacity here is gross AC-equivalent.
candidate=[]
for name,share,cf,base in [('Solar',.45,.18,2164),('Wind',.30,.35,1131),('Fission',.15,.85,420),('Hydro',.08,.40,1437),('Geothermal',.02,.85,15)]:
 energy=80000*share;cap=energy/(8.76*cf)
 candidate.append({'technology':name,'share_assumed':share,'generation_TWh':energy,'capacity_factor_assumed':cf,
  'capacity_2050_GW':cap,'capacity_2024_GW_WEO':base,'net_addition_GW_per_year_2024_2050':(cap-base)/26})
assert abs(sum(x['generation_TWh'] for x in candidate)-80000)<1e-9
for r in candidate:assert abs(r['capacity_2050_GW']*8.76*r['capacity_factor_assumed']-r['generation_TWh'])<1e-7
fig,axs=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1.15,1]})
fig.subplots_adjust(left=.13,right=.92,top=.77,bottom=.24,wspace=.6)
ax=axs[0];y=np.arange(5);ax.barh(y,[r['generation_TWh']/1000 for r in candidate],color=COLORS,height=.58)
ax.set_yticks(y,[r['technology'] for r in candidate]);ax.invert_yaxis();ax.set_xlim(0,46)
for i,r in enumerate(candidate):ax.text(r['generation_TWh']/1000+.6,i,f"{r['generation_TWh']/1000:g}  ({r['share_assumed']:.0%})",va='center',fontsize=10)
ax.set_xlabel('Annual generation · thousand TWh');clean(ax)
ax=axs[1];ax.barh(y,[r['net_addition_GW_per_year_2024_2050'] for r in candidate],color=COLORS,height=.58)
ax.set_yticks(y,[r['technology'] for r in candidate]);ax.invert_yaxis();ax.set_xlim(0,990)
for i,r in enumerate(candidate):ax.text(r['net_addition_GW_per_year_2024_2050']+12,i,f"{r['net_addition_GW_per_year_2024_2050']:.1f}",va='center',fontsize=10)
ax.set_xlabel('Average net capacity increase · GW/year');clean(ax)
save(fig,'03_candidate_build','A concrete design to test: 80,000 TWh per year','Our proposed starting shares—not a forecast or a proven cheapest mix. Wave and fusion are not required for this budget.',
 'Assumed average output: solar 18%, wind 35%, fission 85%, hydro 40%, geothermal 85% of rated power.\nNet additions use the 2024 fleet in IEA WEO 2025 and 26 years to 2050. Replacing retired plants increases gross construction.\nThis balances annual generation only. Storage losses, unused output, hourly reliability, location and costs require a regional model.')
csvout('candidate_build.csv',candidate)

rate,life,opex=.07,20,.04
crf=rate*(1+rate)**life/((1+rate)**life-1)
def wave_cost(capex,cf,annual_opex=opex):return capex*(crf+annual_opex)/(8.76*cf)
threshold=100*8.76*.4/(crf+opex)
wave=[]
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.10,right=.87,top=.78,bottom=.24)
xs=np.arange(1000,8001,100)
for cf,col in [(.25,ORANGE),(.40,GREEN),(.55,BLUE)]:
 vals=wave_cost(xs,cf);ax.plot(xs,vals,color=col,lw=3,label=f'{cf:.0%} average output')
 for x,v in zip(xs,vals):wave.append({'installed_USD_kW':int(x),'net_capacity_factor':cf,'modeled_USD_MWh':float(v)})
ax.axhline(100,color=MUTED,ls='--',lw=1.3);ax.text(7900,108,'$100/MWh test target',ha='right',fontsize=10)
ax.scatter([threshold],[100],color=GREEN,s=65,zorder=5)
ax.annotate(f'At 40% output:\ninstalled cost must be about\n${threshold:,.0f}/kW or less',xy=(threshold,100),xytext=(1200,280),arrowprops={'arrowstyle':'->','color':GREEN},fontsize=11,color=GREEN)
ax.set_xlim(1000,8000);ax.set_ylim(0,520);ax.set_xlabel('All-in installed cost · US dollars per kW');ax.set_ylabel('Modeled generation cost · US dollars per MWh');clean(ax);ax.legend(loc='upper left',frameon=False)
save(fig,'04_wave_threshold','Ocean energy needs a cost target, not a promise','Our sensitivity model: lower installation cost and more usable output must overcome marine maintenance costs.',
 'Assumptions: 7% real financing rate, 20-year life, annual operating costs = 4% of installed cost, net output after downtime.\nThe $100/MWh line is our test target, not a quoted market price. All-in cost must include installation, moorings, electrical works and provisions.\nNo customer backup or storage is included. Early projects may face much higher financing costs; test these assumptions before scaling.')
csvout('wave_cost_sensitivity.csv',wave)

storage=[]
for hours in [4,12,72,336]:
 nominal=100*hours/(.8*.95)
 storage.append({'load_MW':100,'hours':hours,'battery_nameplate_MWh':nominal,'illustrative_capital_USD_million':nominal*1000*300/1e6})
fig,ax=plt.subplots(figsize=(12,6.5));fig.subplots_adjust(left=.15,right=.89,top=.76,bottom=.25)
ax.barh(range(4),[r['battery_nameplate_MWh']/1000 for r in storage],color=[GREEN,BLUE,ORANGE,PURPLE],height=.56)
ax.set_yticks(range(4),['4 hours','12 hours','3 days','14 days']);ax.invert_yaxis();ax.set_xlim(0,55)
for i,r in enumerate(storage):ax.text(r['battery_nameplate_MWh']/1000+.5,i,f"{r['battery_nameplate_MWh']/1000:.2f} GWh",va='center')
ax.set_xlabel('Battery nameplate capacity · GWh');clean(ax)
save(fig,'05_storage_duration','Three days need 18× the storage of four hours','Same 100 MW continuous load. No generation during the stated gap. Other ways to cover the gap may be cheaper.',
 'Our calculation: battery capacity = load × hours ÷ (80% usable fraction × 95% discharge efficiency).\nThis is stored energy, not a complete storage design. Charging supply, battery power, losses, degradation and replacements must also be priced.')
csvout('earth_storage.csv',storage)

space=[]
for label,h,kind in [('Earth orbit: 35 min',35/60,'Representative low-Earth-orbit eclipse'),('Mars: 12.3 h night',12.3,'Approximate half-sol'),('Mars: 72 h no solar',72,'Analyst stress case, not a weather forecast'),('Moon: 14 d night',336,'Illustrative non-polar site')]:
 kwh=100*h/(.8*.95);tonnes=kwh/.2/1000
 space.append({'case':label,'dark_hours':h,'load_kW':100,'battery_kWh':kwh,'battery_tonnes_at_200Wh_kg':tonnes,'basis':kind})
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.26,right=.89,top=.78,bottom=.25)
values=[r['battery_tonnes_at_200Wh_kg'] for r in space]
ax.scatter(values,np.arange(4),s=150,c=[GREEN,BLUE,ORANGE,PURPLE],zorder=3)
for i,v in enumerate(values):
 ax.plot([.2,v],[i,i],color='#BBC8BA',lw=2,zorder=1);ax.text(v*1.18,i,f'{v:.2f} t',va='center',fontweight='bold')
ax.set_xscale('log');ax.set_xlim(.2,600);ax.set_yticks(range(4),[r['case'] for r in space]);ax.invert_yaxis()
ax.set_xticks([.2,1,10,100],['0.2','1','10','100']);ax.set_xlabel('Battery mass · tonnes (log scale: each major step is ×10)');ax.grid(axis='x',color='#D9E0D6');ax.tick_params(axis='y',length=0)
save(fig,'06_space_storage','100 kW. Four very different storage requirements.','Battery-only darkness comparison. This is not a complete solar-versus-reactor mass comparison.',
 'Assumptions: 200 Wh/kg battery pack, 80% usable fraction, 95% discharge efficiency, zero solar during each gap.\nExcludes arrays, charging hardware, thermal protection, degradation and spares. Lunar poles require site-specific illumination.\nDarkness examples: NASA STS-116 press kit, Lunar Surface Technology, Mars facts. The 72-hour Mars case is our selected stress test.')
csvout('space_storage.csv',space)

missions=[{'mission':'2009 DRA 5','solar_t':22.5,'fission_low_t':6,'fission_high_t':8,'load_note':'26 kW cargo / ~35 kW crew'},
 {'mission':'2016 EMC','solar_t':11.7,'fission_low_t':9,'fission_high_t':9,'load_note':'26 kW cargo / 31 kW crew'},
 {'mission':'2020 POD','solar_t':11.22,'fission_low_t':7.93,'fission_high_t':7.93,'load_note':'9 kW cargo / 9 kW crew'}]
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.24,right=.9,top=.77,bottom=.25)
for i,m in enumerate(missions):
 ax.barh(i-.15,m['solar_t'],height=.26,color=GOLD,label='Solar system' if i==0 else '')
 mid=(m['fission_low_t']+m['fission_high_t'])/2
 ax.barh(i+.15,mid,height=.26,color=GREEN,label='Fission system' if i==0 else '')
 if m['fission_high_t']!=m['fission_low_t']:ax.errorbar(mid,i+.15,xerr=(m['fission_high_t']-m['fission_low_t'])/2,color=INK,capsize=5)
 ax.text(m['solar_t']+.4,i-.15,f"{m['solar_t']:g} t",va='center')
 lab=f"{m['fission_low_t']:g}–{m['fission_high_t']:g} t" if i==0 else f"{mid:g} t"
 ax.text(m['fission_high_t']+.4,i+.15,lab,va='center')
ax.set_yticks(range(3),[m['mission']+'\n'+m['load_note'] for m in missions]);ax.invert_yaxis();ax.set_xlim(0,26);ax.set_xlabel('Study estimate of power-system mass · tonnes');clean(ax);ax.legend(loc='lower right',frameon=False)
save(fig,'07_nasa_mars','NASA’s Mars studies support fission for essential power','Three historical mission designs—not three prices for the same mission, and not flight-demonstrated reactor systems.',
 'Source: NASA, Mars Surface Power, February 2025, p. 6. Each pair uses the mission assumptions of that study.\nNASA selected fission as primary surface power for initial crewed Mars missions (p. 2). Hardware still has to be developed and demonstrated.\nDo not scale these masses directly to our separate 100 kW example.')
csvout('nasa_mars_mass.csv',missions)

results={'as_of':'2026-10-24','sources':SOURCES,'published_generation':demand,'regional_growth':regional,
 'candidate':candidate,'wave_assumptions':{'real_rate':rate,'life_years':life,'annual_opex_fraction':opex,'crf':crf,
 'target_USD_MWh':100,'capex_threshold_at_40pct_USD_kW':threshold,
 'cost_at_4000_and_40pct':wave_cost(4000,.4),'cost_at_4000_40pct_8pct_opex':wave_cost(4000,.4,.08)},
 'space':space,'earth_storage':storage,'nasa_mars':missions,
 'limitations':['No hourly dispatch or reliability optimization','Candidate shares are analyst-selected',
 'No plant retirement schedule','No spatial transmission model','Battery examples exclude complete mission hardware']}
(OUT/'energy_model_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'figures':7,'wave_capex_target':threshold,'candidate':candidate,'space':space},indent=2))
