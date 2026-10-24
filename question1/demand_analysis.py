"""Question 1: sourced demand comparisons and transparent calculations.

Run with Python 3.9+, numpy and matplotlib. Outputs are written beside this file.
This script compares published scenarios; it does not claim an independent forecast.
"""
from pathlib import Path
import csv
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT=Path(__file__).resolve().parent
FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
BG='#F3F3E9'; INK='#16332F'; MUTED='#60716A'; GREEN='#007D69'; ORANGE='#BD532F'; BLUE='#6577BE'; GOLD='#B28A37'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'figure.facecolor':BG,'axes.facecolor':BG,
 'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,
 'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,
 'axes.edgecolor':'#C7D3C4','svg.fonttype':'none','savefig.facecolor':BG})

WEO='https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf'
ELEC='https://iea.blob.core.windows.net/assets/1c696cc3-e251-46a9-8d4d-9edb2a4e806a/Electrification.pdf'
SOURCES={
 'WEO2025':{'url':WEO,'title':'IEA World Energy Outlook 2025','date':'2025-11-12','tables':'A.1a-c, A.2a-c, A.3a-c, A.5b, A.16–17',
 'boundary':'TFC includes non-energy uses; generation is gross','license':'Annex A: CC BY-NC-SA 4.0'},
 'ElectricityFeb2026':{'url':'https://www.iea.org/reports/electricity-2026/demand','date':'2026-02-06','boundary':'Electricity demand; February baseline'},
 'ElectricityJul2026':{'url':'https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary','date':'2026-07-23','boundary':'Electricity consumption; revised July baseline'},
 'ElectrificationSep2026':{'url':ELEC,'date':'2026-09-22','pages':'27, 29, 50–51','boundary':'Final energy consumption excludes non-energy uses'},
 'DNV2026':{'url':'https://www.dnv.com/energy-transition-outlook/2026/','date':'2026','boundary':'Published electricity-demand growth; full data not obtained'},
 'AI2026':{'url':'https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary%C2%A0','date':'2026','boundary':'Data-centre facility electricity; subset of total demand'},
 'GER2026':{'url':'https://www.iea.org/reports/global-energy-review-2026/key-findings','date':'2026','boundary':'Annual growth in total energy and electricity'}
}
def writecsv(name,rows):
 with (ROOT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def cagr(a,b,n):return (b/a)**(1/n)-1
def clean(ax,axis='x'):
 ax.set_axisbelow(True);ax.grid(axis=axis,color='#D6DFD2',lw=.7);ax.tick_params(axis='y',length=0)
def save(fig,name,title,sub,foot):
 fig.suptitle(title,x=.055,y=.975,ha='left',fontsize=23,fontweight='bold')
 fig.text(.055,.902,sub,ha='left',va='top',fontsize=11,color=MUTED)
 fig.text(.055,.032,foot,ha='left',va='bottom',fontsize=8.5,color=MUTED,linespacing=1.5)
 for ext in ['png','svg']:fig.savefig(FIG/(name+'.'+ext),dpi=180)
 plt.close(fig)

years=[2024,2035,2040,2050]
scenarios={
 'STEPS':{'label':'Stated policies','generation_TWh':[31229,44274,49114,58081],
  'final_consumption_EJ':[453,504,516,541],'final_electricity_EJ':[95,130,144,169],
  'primary_energy_EJ':[654,708,717,747]},
 'CPS':{'label':'Current policies','generation_TWh':[31229,45109,50488,59426],
  'final_consumption_EJ':[453,523,549,599],'final_electricity_EJ':[95,131,145,172],
  'primary_energy_EJ':[654,744,777,838]},
 'NZE':{'label':'Net-zero pathway','generation_TWh':[31229,48118,60301,80175],
  'final_consumption_EJ':[453,408,380,352],'final_electricity_EJ':[95,133,156,192],
  'primary_energy_EJ':[654,571,551,570]}
}
scenario_rows=[]
for key,s in scenarios.items():
 for i,yr in enumerate(years):
  scenario_rows.append({'scenario':key,'year':yr,**{k:s[k][i] for k in ['generation_TWh','final_consumption_EJ','final_electricity_EJ','primary_energy_EJ']},'source':'WEO2025'})
writecsv('published_scenarios.csv',scenario_rows)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.1,right=.93,top=.76,bottom=.22)
for key,col,style in [('CPS',MUTED,':'),('STEPS',GREEN,'-'),('NZE',ORANGE,'-')]:
 s=scenarios[key];ax.plot(years,np.array(s['generation_TWh'])/1000,marker='o',lw=3 if key!='CPS' else 2,ls=style,color=col,
  label=f"{s['label']}: {s['generation_TWh'][-1]/1000:.1f} in 2050")
ax.set_xlim(2023,2051);ax.set_ylim(0,90);ax.set_xticks([2024,2030,2035,2040,2050]);ax.set_xlabel('Year')
ax.set_ylabel('Electricity generation · thousand TWh/year');clean(ax,'y');ax.legend(frameon=False,loc='upper left',fontsize=11)
ax.annotate('31.2 in 2024',xy=(2024,31.229),xytext=(2025,20),arrowprops={'arrowstyle':'-','color':MUTED},fontsize=12)
save(fig,'01_electricity_outlook','Plan for 60,000–80,000 TWh of electricity in 2050',
 '2050 requires about 58,000–80,000 TWh/year across these IEA pathways. This is a comparison range, not a probability interval.',
 'Source: IEA World Energy Outlook 2025, Tables A.3a–c (CC BY-NC-SA 4.0); adaptation. Lines join published milestone values.\nCurrent/stated policies describe conditional outcomes. Net zero is a goal-driven pathway. All series use the same 2024 baseline and gross-generation boundary.')

# Same report and accounting boundary for the comparison of total consumption with electricity.
cases=[('2024',453,95),('2050\nCurrent policies',599,172),('2050\nStated policies',541,169),('2050\nNet-zero pathway',352,192)]
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.12,right=.93,top=.76,bottom=.24)
xs=np.arange(4)
ax.bar(xs,[r[2] for r in cases],width=.55,color=GREEN,label='Electricity delivered to end users')
ax.bar(xs,[r[1]-r[2] for r in cases],bottom=[r[2] for r in cases],width=.55,color='#B9C3B4',label='Other fuels and heat, including non-energy uses')
for i,(label,total,elec) in enumerate(cases):
 ax.text(i,total+10,f'{total} EJ',ha='center',fontweight='bold')
 ax.text(i,elec/2,f'{elec} EJ',ha='center',va='center',color='white',fontweight='bold')
ax.set_xticks(xs,[r[0] for r in cases]);ax.set_ylim(0,700);ax.set_ylabel('Final consumption · exajoules per year');clean(ax,'y');ax.legend(frameon=False,loc='lower left',bbox_to_anchor=(0,1.01),fontsize=10)
save(fig,'02_energy_vs_electricity','More electricity does not mean more total energy',
 'Efficient electric equipment can provide more useful services while using less purchased energy.',
 'Source: IEA WEO 2025, Tables A.2a–c (CC BY-NC-SA 4.0); adapted from rounded EJ values. 1 EJ = 277.8 TWh.\nThis uses total final consumption, including non-energy uses such as feedstocks. Electricity is final end-use electricity, not total generation.\nThe cases also differ in efficiency and other policies; the chart does not isolate electrification as the only cause.')

sectors=[('Buildings',49,86,73),('Industry',40,58,78),('Transport',2,18,37),('Other',4,7,4)]
sector_rows=[{'sector':n,'electricity_2024_EJ':a,'electricity_2050_STEPS_EJ':b,'electricity_2050_NZE_EJ':c,
 'STEPS_added_TWh':(b-a)/.0036,'NZE_added_TWh':(c-a)/.0036,'source':'WEO2025 rounded A.2 tables; Other is residual'} for n,a,b,c in sectors]
assert sum(r[1] for r in sectors)==95 and sum(r[2] for r in sectors)==169 and sum(r[3] for r in sectors)==192
writecsv('sector_electricity.csv',sector_rows)
fig,ax=plt.subplots(figsize=(12,7));fig.subplots_adjust(left=.14,right=.93,top=.75,bottom=.24)
y=np.arange(4)
for j,(label,col) in enumerate([('2024',MUTED),('2050 stated policies',GREEN),('2050 net-zero pathway',ORANGE)]):
 vals=[r[j+1]/3.6 for r in sectors]
 ax.barh(y+(j-1)*.22,vals,height=.2,color=col,label=label)
 for i,v in enumerate(vals):ax.text(v+.25,y[i]+(j-1)*.22,f'{v:.1f}',va='center',fontsize=10)
ax.set_yticks(y,[r[0] for r in sectors]);ax.invert_yaxis();ax.set_xlim(0,29);ax.set_xlabel('Final electricity use · thousand TWh/year');clean(ax);ax.legend(frameon=False,loc='lower right',fontsize=10)
save(fig,'03_sector_demand','Buildings, industry and transport all shape the answer',
 'Buildings lead the policy case; faster electrification adds much more industrial and transport electricity.',
 'Source: IEA WEO 2025, Tables A.2a–c (CC BY-NC-SA 4.0); rounded EJ values converted to TWh. Other is the residual.\nData centres are included in buildings. Electricity used to make fuels is outside this final-end-use ledger. Do not add it twice.')

regions=[('China',9102,16131),('India',1644,4803),('Southeast Asia',1317,3197),('European Union',2437,4178),('United States',4102,5647),('Africa',753,2197)]
regions.append(('Rest of world',27290-sum(r[1] for r in regions),49657-sum(r[2] for r in regions)))
regional=[{'region':n,'demand_2024_TWh':a,'demand_2050_TWh':b,'added_TWh':b-a,'annual_growth_percent':100*cagr(a,b,26),'source':'WEO2025 Table A.16, stated policies'} for n,a,b in regions]
assert sum(r['added_TWh'] for r in regional)==22367
writecsv('regional_demand.csv',regional)
fig,axs=plt.subplots(1,2,figsize=(13,7),gridspec_kw={'width_ratios':[1.45,1]});fig.subplots_adjust(left=.19,right=.91,top=.76,bottom=.21,wspace=.55)
y=np.arange(7);ax=axs[0];ax.barh(y,[r['added_TWh'] for r in regional],color=GREEN,height=.57)
ax.set_yticks(y,[r['region'] for r in regional]);ax.invert_yaxis();ax.set_xlim(0,8800)
for i,r in enumerate(regional):ax.text(r['added_TWh']+100,i,f"{r['added_TWh']:,}",va='center',fontsize=10)
ax.set_xlabel('Additional TWh/year in 2050');clean(ax);ax.xaxis.set_major_formatter(FuncFormatter(lambda x,p:f'{x:,.0f}'))
ax=axs[1];ax.barh(y,[r['annual_growth_percent'] for r in regional],color=BLUE,height=.57)
ax.set_yticks(y,['']*7);ax.invert_yaxis();ax.set_xlim(0,5.4)
for i,r in enumerate(regional):ax.text(r['annual_growth_percent']+.06,i,f"{r['annual_growth_percent']:.1f}%",va='center',fontsize=10)
ax.set_xlabel('Average annual growth, 2024–2050');ax.xaxis.set_major_formatter(FuncFormatter(lambda x,p:f'{x:g}%'));clean(ax)
save(fig,'04_regional_growth','China adds the most; India and Africa grow faster',
 'Compare both the size of the increase and its growth rate. These regions do not overlap.',
 'Source: IEA WEO 2025, Table A.16 (CC BY-NC-SA 4.0); calculations. Stated-policies scenario only.\nWorld electricity demand rises from 27,290 to 49,657 TWh/year. The chart uses demand, not generation.')

base_demand=27290; pop0=8091; pop1=9572; target=49657
population_only=base_demand*pop1/pop0
decomp={'base_demand_TWh':base_demand,'population_only_2050_TWh':population_only,'STEPS_2050_TWh':target,
 'population_growth_percent':100*(pop1/pop0-1),'demand_growth_percent':100*(target/base_demand-1),
 'per_capita_2024_kWh':base_demand/(pop0/1000),'per_capita_2050_kWh':target/(pop1/1000),
 'other_growth_TWh':target-population_only}
fig,ax=plt.subplots(figsize=(12,6.5));fig.subplots_adjust(left=.24,right=.92,top=.75,bottom=.24)
vals=[base_demand,population_only,target]; labels=['2024 actual','2050 with only\npopulation growth','2050 stated policies']
ax.barh(range(3),np.array(vals)/1000,color=[MUTED,BLUE,GREEN],height=.5)
ax.set_yticks(range(3),labels);ax.invert_yaxis();ax.set_xlim(0,60);ax.set_xlabel('Electricity demand · thousand TWh/year');clean(ax)
for i,v in enumerate(vals):ax.text(v/1000+.7,i,f'{v/1000:.1f}',va='center',fontweight='bold')
save(fig,'05_population','Population growth explains only part of the increase',
 'In the stated-policies case, population grows 18%, while electricity demand grows 82%.',
 'Calculation using IEA WEO 2025 population (8.091 → 9.572 billion) and demand (27,290 → 49,657 TWh).\nThe middle bar holds electricity per person constant. The remaining difference combines income, industry, electrification, efficiency and other changes.\nThis is an accounting illustration, not a causal estimate of each driver. WEO Annex A: CC BY-NC-SA 4.0.')

# Explicit service-based load experiment, not an observed or forecast EV fleet.
fleet=10_000_000; km=12000; kwh_km=.18
ev_energy_TWh=fleet*km*kwh_km/1e9; daily_GWh=ev_energy_TWh*1000/365
ev={'cars_assumed':fleet,'annual_km_per_car_assumed':km,'charger_kWh_per_km_assumed':kwh_km,
 'annual_electricity_TWh':ev_energy_TWh,'daily_GWh':daily_GWh,'four_hour_power_GW':daily_GWh/4,'ten_hour_power_GW':daily_GWh/10}
fig,axs=plt.subplots(1,2,figsize=(12,6),gridspec_kw={'width_ratios':[1.4,1]});fig.subplots_adjust(left=.10,right=.93,top=.73,bottom=.26,wspace=.43)
hours=np.arange(25);four=np.array([daily_GWh/4 if 18<=h<22 else 0 for h in hours]);ten=np.array([daily_GWh/10 if 0<=h<10 else 0 for h in hours])
ax=axs[0];ax.step(hours,four,where='post',color=ORANGE,lw=3,label='All charging within 4 hours');ax.step(hours,ten,where='post',color=GREEN,lw=3,label='Spread across 10 hours')
ax.set_xlim(0,24);ax.set_ylim(0,18);ax.set_xticks([0,6,12,18,24],['00:00','06:00','12:00','18:00','24:00']);ax.set_xlabel('Time of day');ax.set_ylabel('Charging power · GW');clean(ax,'y')
ax=axs[1];ax.bar([0,1],[daily_GWh/4,daily_GWh/10],color=[ORANGE,GREEN],width=.5)
ax.set_xticks([0,1],['4-hour window','10-hour window']);ax.set_ylim(0,18);ax.set_ylabel('Peak charging power · GW');clean(ax,'y')
for i,v in enumerate([daily_GWh/4,daily_GWh/10]):ax.text(i,v+.4,f'{v:.1f} GW',ha='center',fontweight='bold')
save(fig,'06_timing','Same yearly energy. Very different peak power.',
 'Illustration: 10 million electric cars use 21.6 TWh/year in both charging schedules.',
 'Assumptions: 12,000 km/car/year, 0.18 kWh/km measured at the charger, identical daily mileage, evenly spread charging within each window.\nSchedules are illustrations, not forecasts or guaranteed achievable flexibility. Other grid demand is not shown; these are not total-system peaks.')

growth=[]
for key,s in scenarios.items():
 growth.append({'scenario':key,'generation_2024_TWh':31229,'generation_2050_TWh':s['generation_TWh'][-1],
 'generation_cagr_percent':100*cagr(31229,s['generation_TWh'][-1],26),
 'generation_added_TWh_per_year_average':(s['generation_TWh'][-1]-31229)/26,
 'final_consumption_cagr_percent':100*cagr(453,s['final_consumption_EJ'][-1],26)})
writecsv('calculated_growth.csv',growth)
anchors=[{'source':'ElectricityFeb2026','year':2025,'electricity_demand_TWh':28200,'status':'historical estimate in February edition'},
 {'source':'ElectricityFeb2026','year':2030,'electricity_demand_TWh':33600,'status':'published forecast, February baseline'},
 {'source':'ElectricityJul2026','year':2025,'electricity_demand_TWh':28600,'status':'revised historical estimate'},
 {'source':'ElectricityJul2026','year':2027,'electricity_demand_TWh':30700,'status':'published forecast'}]
writecsv('near_term_anchors.csv',anchors)
sens=[]
for yr in range(2025,2051):
 for g in [.02,.03,.04]:sens.append({'year':yr,'assumed_growth_percent':100*g,'electricity_consumption_TWh':28600*(1+g)**(yr-2025),'status':'illustration, not forecast'})
writecsv('growth_sensitivity.csv',sens)
result={'as_of':'2026-10-24','sources':SOURCES,'years':years,'scenarios':scenarios,'growth':growth,
 'regions':regional,'sectors':sector_rows,'population':decomp,'ev_timing':ev,'near_term':anchors,
 'latest_electrification_report':{'historical_average_added_TWh_per_year_2015_2025':750,
 'STEPS_average_added_TWh_per_year_2025_2035':925,'HES_average_added_TWh_per_year_2025_2035':1400,
 'HES_electrification_percent_2035':35,'notes':'Rounded source numbers; goal-driven HES, not a prediction'},
 'peak':{'sum_of_system_peaks_2024_GW':4750,'projected_growth_to_2035_approx_percent':40,
 'notes':'WEO pp.240–241; sum of local system peaks, not simultaneous world demand'},
 'data_centres':{'IEA_2025_TWh':485,'IEA_2030_TWh':950,'note':'IEA 2026 AI report; embedded in sector and world totals'},
 'limitations':['Published-scenario comparison, not independent calibrated forecast','No regional hourly demand dataset or adequacy model',
 'No source-vintage splicing','Generation scenarios include their own transformation and system assumptions',
 'TFC includes non-energy uses; TFEC excludes them','EV and population examples are explicit illustrations']}
(ROOT/'demand_results.json').write_text(json.dumps(result,indent=2)+'\n')
assert abs((ev['four_hour_power_GW']*4)-(ev['ten_hour_power_GW']*10))<1e-9
assert all(r['final_electricity_EJ']<=r['final_consumption_EJ'] for r in scenario_rows)
assert len(scenario_rows)==12
print(json.dumps({'figures':6,'population':decomp,'growth':growth,'ev_timing':ev},indent=2))
