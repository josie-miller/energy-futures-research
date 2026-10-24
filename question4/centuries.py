"""Reproduce Q4 scenarios, unit checks, CSV tables and publication graphics.

No web requests, climate simulation, cost optimization or demand forecast.
Run: python question4/centuries.py
"""
from pathlib import Path
import json, csv, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT/'inputs.json').read_text())
FIG = ROOT/'figures'; FIG.mkdir(exist_ok=True)
C = ['#7a9e7e', '#126e91', '#e8a941', '#b14b62']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
    'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,
    'axes.edgecolor':'#bac5c9','text.color':'#233840','axes.labelcolor':'#233840',
    'xtick.color':'#48616b','ytick.color':'#48616b','svg.fonttype':'none',
    'savefig.facecolor':'white','figure.facecolor':'white'})
def save(fig, name):
    fig.savefig(FIG/(name+'.png'), dpi=170, bbox_inches='tight')
    fig.savefig(FIG/(name+'.svg'), bbox_inches='tight'); plt.close(fig)
def heading(fig, title, subtitle):
    fig.suptitle(title, x=.08, y=.98, ha='left', fontsize=19, fontweight='bold')
    fig.text(.08,.91,subtitle,fontsize=10.5,color='#536a74')
def foot(fig, text): fig.text(.08,.02,text,fontsize=9,color='#536a74')
def table(name, rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def demand(year, rate, start=None):
    return (P['start_TWh'] if start is None else start)*(1+rate)**(year-P['start_year'])

def blue_demand(year):
    y=np.asarray(year)
    return P['start_TWh']*(1+P['blue_growth_to_2100'])**(np.minimum(y,2100)-2050)*(1+P['blue_growth_after_2100'])**np.maximum(y-2100,0)

area = 4*math.pi*P['earth_radius_m']**2
rows=[]
for g in P['annual_growth_rates']:
    for y in P['years']:
        e=demand(y,g)
        rows.append({'year':y,'growth_per_year':g,'generation_TWh':e,
            'mean_electric_TW':e/8760,'multiple_2024':e/P['baseline_2024_TWh'],
            'next_year_extra_TWh':e*g,
            'selected_new_heat_W_m2':e/8760*1e12*P['new_heat_electricity_fraction']/P['thermal_conversion_efficiency']/area})
table('demand_scenarios.csv',rows)
ref=round(float(blue_demand(2100)))
portfolio=[]
future=[]
for year, techs in P['future_portfolios'].items():
    total=sum(t['TWh'] for t in techs)
    for t in techs:
        e=t['TWh'];gw=e/(8.76*t['cf']) if t['cf'] else None
        row={**t,'year':int(year),'share':e/total,'capacity_GW':gw,
            'replacement_GW_year':gw/t['life_years'] if gw else None,
            'growth_GW_year':gw*P['reference_rate'] if gw else None,
            'gross_build_GW_year':gw*(1/t['life_years']+P['reference_rate']) if gw else None}
        future.append(row)
        if year=='2100':portfolio.append(row)
table('proposed_2100_mix.csv',portfolio)
table('blue_planet_mix.csv',future)
blue=[]
for y in P['years']:
    e=float(blue_demand(y))
    mix=P['portfolio_2050_TWh'] if y==2050 else {t['id']:t['TWh'] for t in P['future_portfolios'].get(str(y),[])}
    ocean=sum(mix.get(k,0) for k in P['ocean_ids']) if mix else None
    blue.append({'year':y,'generation_TWh':e,'mean_electric_TW':e/8760,
        'ocean_TWh':ocean,'ocean_share':ocean/sum(mix.values()) if mix else None,
        'following_year_growth':P['blue_growth_to_2100'] if y<2100 else P['blue_growth_after_2100']})
table('blue_planet_growth.csv',blue)
physical=[]
for y in [2100,2200]:
    mix={t['id']:t['TWh'] for t in P['future_portfolios'][str(y)]}
    wind=mix['offshore_wind']/8760
    # TWh/year / (8760h * W/m2) to area:1TWh=1e12Wh; divide1e6 forkm2.
    fpv_area=mix['fpv']*1e6/(8760*P['fpv_average_power_W_m2'])
    physical.append({'year':y,'offshore_average_TW':wind,'offshore_installed_TW':wind/P['offshore_cf'],
        'wind_area_low_km2':wind*1e6/6,'wind_area_high_km2':wind*1e6/1.5,
        'wind_area_low_pct_ocean':wind*1e6/6/P['ocean_area_km2']*100,
        'wind_area_high_pct_ocean':wind*1e6/1.5/P['ocean_area_km2']*100,
        'fpv_area_km2':fpv_area,'fpv_area_pct_ocean':fpv_area/P['ocean_area_km2']*100,
        'otec_average_TW':mix['otec']/8760,'otec_installed_TW':mix['otec']/8760/P['otec_cf'],
        'fission_fusion_heat_W_m2':(mix['fission']+mix['fusion'])/8760*1e12/P['nuclear_heat_conversion_efficiency']/area})
table('blue_planet_scale_checks.csv',physical)
benchmarks=[]
for g in P['annual_growth_rates']:
    for flux in P['flux_benchmarks_W_m2']:
        power=flux*area/1e12*P['thermal_conversion_efficiency']/P['new_heat_electricity_fraction']
        year=P['start_year']+math.log(power/(P['start_TWh']/8760))/math.log1p(g)
        benchmarks.append({'growth_per_year':g,'benchmark_W_m2':flux,'electric_TW_at_benchmark':power,'crossing_year_if_unchanged':year})
table('heat_benchmarks.csv',benchmarks)
space=[]
for power_gw in [1,1000,1000000]:
    watts=power_gw*1e9
    r={'electrical_power_GW':power_gw,
       'collector_1au_km2':watts/(P['solar_flux_1au_W_m2']*P['space_panel_efficiency'])/1e6,
       'collector_mars_orbit_km2':watts/(P['solar_flux_mars_W_m2']*P['space_panel_efficiency'])/1e6}
    for temp in P['radiator_temperatures_K']:
        r[f'radiator_{temp}K_emitting_km2']=watts/(P['radiator_emissivity']*P['sigma_W_m2_K4']*temp**4)/1e6
    r['collector_mass_t_at_assumed_areal_mass']=r['collector_1au_km2']*1e6*P['collector_areal_mass_kg_m2']/1000
    space.append(r)
table('space_hardware.csv',space)
S=P['future_services']
services=[{'service':'500 Mt/year hydrogen','electricity_TWh':S['hydrogen_Mt_year']*1e9*S['hydrogen_kWh_kg']/1e9},
    {'service':'10 Gt/year carbon removal','electricity_TWh':S['carbon_removal_Gt_year']*1e9*S['carbon_removal_electric_MWh_t']/1e6},
    {'service':'1 TW continuous computing','electricity_TWh':S['computing_TW_continuous']*8760},
    {'service':'1 billion m³/day desalination','electricity_TWh':S['water_m3_day']*365*S['water_kWh_m3']/1e9}]
for s in services:s['fraction_reference_2100_generation']=s['electricity_TWh']/ref
table('illustrative_services.csv',services)
out={'as_of':P['as_of'],'sources':json.loads((ROOT/'sources.json').read_text()),
    'blue_planet_growth':blue,'blue_planet_mix':future,'blue_planet_scale_checks':physical,'demand':rows,'portfolio_2100':portfolio,'heat_benchmarks':benchmarks,'space':space,'services':services,
    'earth_surface_m2':area,'lunar_night_1GW_delivered_GWh':P['lunar_night_hours'],
    'lunar_night_1GW_ideal_battery_t':1e9*P['lunar_night_hours']/P['battery_Wh_kg']/1000,
    'one_billionth_sun_electric_TW':P['sun_luminosity_W']*1e-9*P['space_panel_efficiency']/1e12,
    'one_billionth_sun_collector_km2':P['sun_luminosity_W']*1e-9/P['solar_flux_1au_W_m2']/1e6,
    'one_billionth_sun_multiple_2024_electricity':P['sun_luminosity_W']*1e-9*P['space_panel_efficiency']/1e12/(P['baseline_2024_TWh']/8760),
    'reference_2200_extra_TWh_year':float(blue_demand(2200))*.01,
    'reference_2200_extra_offshore_GW_equivalent':float(blue_demand(2200))*.01/(8.76*.45),
    'seawater_flow_1GW_m3_s_at1C':1e9/(1025*3990),
    'ocean_1pct_fpv_TWh_year':P['ocean_area_km2']*.01*1e6*P['fpv_average_power_W_m2']*8760/1e12}

# Unit and conservation checks, independent of figure appearance.
assert abs(sum(x['share'] for x in portfolio)-1)<1e-12
assert abs(sum(x['TWh'] for x in portfolio)-ref)<1e-7
assert abs(demand(2050,.03)-80000)<1e-9
assert abs(space[1]['collector_1au_km2']/space[0]['collector_1au_km2']-1000)<1e-9
assert abs(space[0]['radiator_300K_emitting_km2']/space[0]['radiator_600K_emitting_km2']-16)<1e-9
assert abs(services[0]['electricity_TWh']-27500)<1e-9
assert abs(services[3]['electricity_TWh']-1095)<1e-9
assert all(math.isclose(demand(2200,g,60000)/demand(2200,g),.75,rel_tol=1e-12) for g in P['annual_growth_rates'])
(ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')

fig,ax=plt.subplots(figsize=(13,6.5));fig.subplots_adjust(left=.11,right=.85,top=.79,bottom=.19)
heading(fig,'A small growth rate becomes a different civilization',
    'Electricity-generation experiments from 80,000 TWh in 2050. These are assumptions, not forecasts.')
years=np.arange(2050,2301)
for g,color in zip(P['annual_growth_rates'],C):
    ys=demand(years,g);ax.plot(years,ys,color=color,lw=2.6,label=f'{g:.1%} per year')
    ax.text(2304,ys[-1],f'{g:.1%}\n{ys[-1]/8760:,.0f} TW',color=color,va='center',fontsize=10)
ax.plot(years,blue_demand(years),color='#111f28',lw=3.5,ls='--',label='Blue Planet: 2% → 1%')
ax.set_yscale('log');ax.set_ylim(60000,2e8);ax.set_xlim(2050,2300)
ax.set_yticks([80000,1e6,1e7,1e8],['80,000','1 million','10 million','100 million'])
ax.set_xticks([2050,2100,2200,2300]);ax.set_ylabel('Annual electricity generation, TWh (log scale)')
ax.grid(axis='y',alpha=.15);ax.legend(frameon=False,loc='upper left',ncols=2)
foot(fig,'Start from the 60,000 TWh case instead and every curve is 25% lower. TW labels show average electric power.\nRates already summarize efficiency and changing services; constant growth is not a prediction that it persists.')
save(fig,'01_centuries_of_growth')

fig,ax=plt.subplots(figsize=(13,6.7));fig.subplots_adjust(left=.10,right=.77,top=.78,bottom=.20)
heading(fig,'Blue Planet: the ocean becomes a major collecting surface',
    '15% in our 2050 proposal; 46% and 64% in the designed 2100/2200 scenarios. Not a forecast.')
groups=[('offshore_wind','Offshore wind','#125d83'),('fpv','Offshore solar','#27aca7'),('otec','Ocean thermal','#a9dfe7'),
    ('marine','Tidal, wave, salinity','#5d9bc4'),('solar','Land solar','#e7ac40'),('land_wind','Land wind','#8caf8c'),
    ('fission','Fission','#8066a7'),('fusion','Fusion','#cb6b9c'),('hydro','Hydro','#939393'),('other','Other','#bd8167')]
for j,y in enumerate([2050,2100,2200]):
    mix=P['portfolio_2050_TWh'] if y==2050 else {t['id']:t['TWh'] for t in P['future_portfolios'][str(y)]}
    total=sum(mix.values());bottom=0
    for key,label,color in groups:
        if key=='marine':v=sum(mix.get(k,0) for k in ['tidal','wave','salinity'])
        elif key=='other':v=sum(mix.get(k,0) for k in ['other','geothermal','bioenergy','csp','fossil'])
        else:v=mix.get(key,0)
        share=v/total*100
        ax.bar(j,share,bottom=bottom,width=.64,color=color,edgecolor='white',linewidth=.4,label=label if j==0 else None)
        bottom+=share
    ocean=sum(mix.get(k,0) for k in P['ocean_ids'])
    ax.text(j,103,f'Ocean {ocean/total:.0%}',ha='center',color='#125d83',fontsize=13)
ax.set_xticks([0,1,2],['2050\n80,000 TWh','2100\n215,327 TWh','2200\n582,420 TWh'])
ax.set_ylim(0,111);ax.set_ylabel('Share of annual electricity generation (%)');ax.legend(bbox_to_anchor=(1.02,.95),loc='upper left',frameon=False,fontsize=9)
foot(fig,'Ocean-collected includes offshore wind/solar and direct marine sources. Nuclear fuel origin is not an extra source share.\n2050 uses current Q3. 2100/2200 preserve the uploaded designed allocations; a fleet transition is not yet optimized.')
save(fig,'02_blue_planet_mix')

fig,ax=plt.subplots(figsize=(13,6.5));fig.subplots_adjust(left=.23,right=.94,top=.79,bottom=.20)
heading(fig,'Keeping the lights on also means rebuilding the fleet',
    'Illustrative annual construction at the 2100 fleet size, with 1% continuing growth.')
chosen=[next(x for x in portfolio if x['id']==key) for key in ['solar','offshore_wind','fission']]
for y,r in enumerate(chosen):
    a,b=r['replacement_GW_year'],r['growth_GW_year']
    ax.barh(y,a,color='#b8c9d0',label='Replace ageing equipment' if y==0 else None,height=.55)
    ax.barh(y,b,left=a,color='#126e91',label='Add capacity for growth' if y==0 else None,height=.55)
    ax.text(a+b+12,y,f'{a+b:,.0f} GW/year',va='center')
ax.set_yticks(range(3),[r['name'] for r in chosen]);ax.invert_yaxis();ax.set_xlim(0,max(r['gross_build_GW_year'] for r in chosen)*1.22)
ax.set_xlabel('Illustrative annual gross construction, GW');ax.legend(frameon=False,loc='lower right')
foot(fig,'Replacement approximation: fleet ÷ lifetime, assuming a spread of equipment ages; actual cohorts can differ greatly.\nAssumed lifetimes: solar/offshore 30 years, fission 60 years. This is manufacturing scale, not a timed retirement forecast.')
save(fig,'03_rebuild_the_fleet')

fig,ax=plt.subplots(figsize=(13,6.5));fig.subplots_adjust(left=.13,right=.84,top=.79,bottom=.19)
heading(fig,'At very large scale, clean energy still needs a heat budget',
    'Example: 25% of electricity from added thermal energy, converted to electricity at 40% efficiency.')
for g,col in zip(P['annual_growth_rates'],C):
    flux=demand(years,g)/8760*1e12*.25/.4/area
    ax.plot(years,flux,color=col,lw=2.5,label=f'{g:.1%} growth')
    ax.text(2304,flux[-1],f'{g:.1%}',va='center',color=col)
for b in [.1,1]:ax.axhline(b,color='#7d8c92',ls='--',lw=1);ax.text(2053,b*1.09,f'{b:g} W/m² comparison line',fontsize=9)
ax.set_yscale('log');ax.set_ylim(.007,30);ax.set_xlim(2050,2300);ax.set_xticks([2050,2100,2200,2300])
ax.set_ylabel('Added heat averaged across Earth, W/m²');ax.legend(frameon=False,ncols=2,loc='upper left')
foot(fig,'Comparison lines are not safety limits or temperature predictions. This excludes greenhouse gases and climate feedbacks.\nSolar/wind redirect existing flows; their full electrical output is not automatically new planetary heat.')
save(fig,'04_growth_and_heat')

fig,axs=plt.subplots(1,2,figsize=(13,6.5));fig.subplots_adjust(left=.08,right=.97,top=.78,bottom=.23,wspace=.35)
heading(fig,'A gigawatt in space needs hardware you can measure',
    'Idealized active area for 1 GW electrical output or 1 GW of heat rejection; actual systems need margins.')
v=[space[0]['collector_1au_km2'],space[0]['collector_mars_orbit_km2']]
axs[0].bar([0,1],v,color=['#e8ad45','#bd8062'],width=.55)
axs[0].set_xticks([0,1],['Near Earth\nabove atmosphere','At Mars distance\nabove atmosphere'])
axs[0].set_ylabel('Sun-facing solar-cell area, km²');axs[0].set_ylim(0,7)
for i,z in enumerate(v):axs[0].text(i,z+.15,f'{z:.2f} km²',ha='center')
temps=P['radiator_temperatures_K'];v=[space[0][f'radiator_{t}K_emitting_km2'] for t in temps]
axs[1].bar(range(3),v,color=['#82afb9','#3f849a','#165b77'],width=.55)
axs[1].set_xticks(range(3),[f'{t} K\n{t-273.15:.0f}°C' for t in temps]);axs[1].set_ylabel('Radiator emitting area, km²');axs[1].set_ylim(0,3)
for i,z in enumerate(v):axs[1].text(i,z+.07,f'{z:.2f}',ha='center')
foot(fig,'Solar: 30% conversion, normal incidence, full illumination; excludes eclipses, degradation and atmosphere/surface effects.\nRadiator: emissivity 0.9, ideal deep-space view; 1 GW of load heat only. Arrays and power conversion reject additional heat.')
save(fig,'05_space_hardware')

fig,ax=plt.subplots(figsize=(13,6.6));fig.subplots_adjust(left=.30,right=.91,top=.78,bottom=.20)
heading(fig,'Abundant electricity could buy more than more appliances',
    'Four illustrative service budgets. These are choices inside a future energy budget, not extra forecast demand.')
for i,s in enumerate(services):
    v=s['electricity_TWh'];ax.barh(i,v/1000,color=['#126e91','#89aa85','#a087be','#6cbdc1'][i],height=.55)
    ax.text(v/1000+.4,i,f'{v:,.0f} TWh',va='center')
ax.set_yticks(range(4),[s['service'] for s in services]);ax.invert_yaxis();ax.set_xlim(0,34)
ax.set_xlabel('Thousand TWh of electricity per year')
foot(fig,'Hydrogen: 55 kWh/kg. Water: 3 kWh/m³, before inland delivery. Carbon removal: assumed all-electric 2 MWh/t.\nCarbon removal still needs verified net removals and permanent storage. Computing is a chosen 1 TW load, not a forecast.')
save(fig,'06_what_abundance_buys')
print(json.dumps({'reference_2100_TWh':ref,'reference_2200_TWh':float(blue_demand(2200)),
    'checks':'passed','figures':len(list(FIG.glob('*.png'))),'space_1GW':space[0]},indent=2))
