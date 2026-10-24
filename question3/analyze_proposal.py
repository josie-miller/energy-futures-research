"""Reproduce portfolio arithmetic, data audit and publication figures.
Run: python analyze_proposal.py. Does not download data or solve the LP.
"""
from pathlib import Path
import json, hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdates

ROOT=Path(__file__).resolve().parent
IN=ROOT/'inputs'; FIG=ROOT/'figures';FIG.mkdir(exist_ok=True)
P=json.loads((ROOT/'proposal_inputs.json').read_text())
colors={'solar':'#efb44e','land_wind':'#8ab788','ocean':'#136e91','hydro':'#73b6c9',
        'fission':'#9e82ba','geothermal':'#c67c61','other':'#b9bbb6','tidal':'#008a76','wave':'#de8d35','otec':'#c25260'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,
 'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#b8c4c5','axes.labelcolor':'#25383e',
 'text.color':'#25383e','xtick.color':'#43585f','ytick.color':'#43585f','savefig.facecolor':'white',
 'figure.facecolor':'white','axes.titleweight':'bold','svg.fonttype':'none'})
def save(fig,name):
    fig.savefig(FIG/(name+'.png'),dpi=180,bbox_inches='tight');fig.savefig(FIG/(name+'.svg'),bbox_inches='tight');plt.close(fig)
def title(fig,main,sub):
    fig.suptitle(main,x=.08,y=.98,ha='left',fontsize=20,fontweight='bold')
    fig.text(.08,.91,sub,ha='left',fontsize=11,color='#526870')
def foot(fig,text):fig.text(.08,.02,text,ha='left',fontsize=9,color='#526870')

out={'as_of':P['as_of'],'sources':json.loads((ROOT/'sources.json').read_text()),'portfolio':{},'data_audit':{},'experiments':[]}
for key,total in [('policy',60000),('electrified',80000)]:
    rows=[]
    for t in P['technologies']:
        e=t[key+'_TWh'];cf=t['capacity_factor']
        rows.append(dict(id=t['id'],name=t['name'],TWh=e,share=e/total,
                         GW=(e/(8.76*cf) if cf else None),capacity_factor=cf))
    assert sum(r['TWh'] for r in rows)==total
    ocean=sum(r['TWh'] for r in rows if r['id'] in P['ocean_ids'])
    marine=sum(r['TWh'] for r in rows if r['id'] in P['marine_ids'])
    wind=next(r for r in rows if r['id']=='offshore_wind')
    out['portfolio'][key]={'total_TWh':total,'rows':rows,'ocean_TWh':ocean,'marine_TWh':marine,
        'annual_growth_2024_2050':(total/P['baseline_generation_2024_TWh'])**(1/26)-1,
        'annual_added_output_TWh':(total-P['baseline_generation_2024_TWh'])/26,
        'offshore_average_net_additions_GW_year':(wind['GW']-P['offshore_baseline_end_2025_GW'])/25,
        'offshore_build_multiple_2025':(wind['GW']-P['offshore_baseline_end_2025_GW'])/25/P['offshore_additions_2025_GW']}
    # Endpoint values derive from the energy target, rather than rounded copies.
    P['offshore_checkpoints'][key+'_GW'][-1]=wind['GW']

fig,ax=plt.subplots(figsize=(13,6.1));fig.subplots_adjust(left=.12,right=.97,top=.79,bottom=.25)
title(fig,'Our proposal: the ocean supplies 15% of a much larger grid',
      'Annual electricity generation in 2050. These are proposed build plans, not a solved global optimum.')
group_ids=['solar','land_wind','ocean','hydro','fission','geothermal','other']
labels={'solar':'Solar','land_wind':'Land wind','ocean':'Ocean','hydro':'Hydro','fission':'Fission','geothermal':'Geothermal','other':'Other'}
for y,key in enumerate(['policy','electrified']):
    d=out['portfolio'][key]; left=0
    for name in group_ids:
        v=d['ocean_TWh'] if name=='ocean' else next(r['TWh'] for r in d['rows'] if r['id']==name)
        ax.barh(y,v/1000,left=left/1000,height=.5,color=colors[name],label=labels[name] if y==0 else None)
        if v/d['total_TWh']>=.075:
            ax.text((left+v/2)/1000,y,f'{v/1000:g}k\n{v/d["total_TWh"]:.0%}',ha='center',va='center',fontsize=11,
                    color='white' if name in ['ocean','fission'] else '#22363d')
        left+=v
    ax.text(d['total_TWh']/1000+.6,y,f'{d["total_TWh"]:,} TWh',va='center',fontsize=11,fontweight='bold')
ax.set_yticks([0,1],['Policy-scale\ndemand','More electrified\nworld']);ax.invert_yaxis()
ax.set_xlim(0,94);ax.set_xlabel('Thousand TWh per year');ax.legend(ncols=7,loc='lower left',bbox_to_anchor=(-.01,-.36),frameon=False,fontsize=10)
foot(fig,'Ocean includes offshore wind plus tidal, wave and ocean thermal. Storage is not counted as new generation.\nDemand scale: Q1 / IEA WEO 2025. Allocation: our proposal. Annual totals do not establish hourly reliability.')
save(fig,'01_proposed_mix')

fig,axs=plt.subplots(1,2,figsize=(13,6.7),gridspec_kw={'width_ratios':[1.5,1]});fig.subplots_adjust(left=.08,right=.97,top=.79,bottom=.22,wspace=.3)
title(fig,'An ocean future requires an industrial buildout',
      'Our 15% goal requires 2.2–2.9 TW of offshore wind by 2050, plus smaller marine fleets.')
yr=P['offshore_checkpoints']['years']
for key,label,style in [('policy','60,000 TWh case','-'),('electrified','80,000 TWh case','--')]:
    ys=P['offshore_checkpoints'][key+'_GW'];axs[0].plot(yr,ys,style,color=colors['ocean'],marker='o',label=label,lw=2.5)
    axs[0].text(2050.6,ys[-1],f'{ys[-1]:,.0f} GW',va='center',fontsize=10)
axs[0].scatter([2035],[420],marker='D',color='#7d8790',s=50,label='GWEC 2035 forecast')
axs[0].set_xlim(2024,2056);axs[0].set_ylim(0,3250);axs[0].set_ylabel('Operating offshore-wind capacity, GW');axs[0].set_xticks(yr)
axs[0].legend(frameon=False,loc='upper left',fontsize=9)
v=[9.3,out['portfolio']['policy']['offshore_average_net_additions_GW_year'],out['portfolio']['electrified']['offshore_average_net_additions_GW_year']]
axs[1].barh([2,1,0],v,color=['#b4c2c9',colors['ocean'],colors['ocean']],height=.5)
axs[1].set_yticks([2,1,0],['Installed\nin 2025','60k case\n2026–50 mean','80k case\n2026–50 mean']);axs[1].set_xlim(0,145)
for y,z in zip([2,1,0],v):axs[1].text(z+2,y,f'{z:.1f} GW/yr',va='center',fontsize=10)
axs[1].set_xlabel('Annual capacity additions')
foot(fig,'Historical and forecast references: GWEC 2026. Our checkpoints are proposed targets.\nFuture bars show net capacity growth; replacing retired turbines increases gross construction requirements.')
save(fig,'02_ocean_buildout')

for p in sorted(IN.glob('profiles*.csv')):
    df=pd.read_csv(p,index_col=0,parse_dates=True)
    assert df.index.is_unique and df.index.is_monotonic_increasing
    assert (df.index.to_series().diff().dropna()==pd.Timedelta(hours=1)).all()
    assert not df.isna().any().any()
    out['data_audit'][p.name]={'hours':len(df),'start':str(df.index.min()),'end':str(df.index.max()),
         'yearly_means':{str(y):g.mean().to_dict() for y,g in df.groupby(df.index.year)},
         'above_one_hours':(df>1).sum().to_dict(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
sc=pd.read_csv(IN/'profiles_scotland.csv',index_col=0,parse_dates=True)
s10=pd.read_csv(IN/'profiles_scotland_2010.csv',index_col=0,parse_dates=True)
out['data_audit']['2010_tide_equals_2023']=bool(np.array_equal(s10.tidal.values,sc.loc['2023'].tidal.values))
s23=sc.loc['2023'];end=s23.offwind_floating.rolling(168).mean().idxmin();start=end-pd.Timedelta(hours=167)
window=s23.loc[start:end]
out['data_audit']['worst_wind_week_2023']={'start':str(start),'end':str(end),'means':window.mean().to_dict()}
out['data_audit']['correlation_2022_2024']=sc[['offwind_floating','wave','tidal']].corr().to_dict()
for name in ['sco_current.csv.gz','haw_sst.csv.gz']:
    df=pd.read_csv(IN/name,index_col=0,parse_dates=True).loc['2022':'2024']
    out['data_audit'][name]={'missing':df.isna().sum().to_dict(),'first':str(df.index.min()),'last':str(df.index.max())}
fig,axs=plt.subplots(2,1,figsize=(13,7.5),height_ratios=[2,1],sharex=True);fig.subplots_adjust(left=.08,right=.97,top=.79,bottom=.19,hspace=.18)
title(fig,'Tides can keep contributing through a wind lull',
      'Selected worst 168-hour wind window of 2023 in the supplied northern Scotland profiles.')
view=s23.loc[start-pd.Timedelta(days=3):end+pd.Timedelta(days=3)]
for name,label,color in [('offwind_floating','Offshore wind',colors['ocean']),('wave','Wave',colors['wave']),('solar','Solar',colors['solar'])]:
    axs[0].plot(view.index,view[name].rolling(25,center=True,min_periods=1).mean()*100,label=label,lw=2.3,color=color)
axs[0].plot(view.index,view.tidal.rolling(25,center=True,min_periods=1).mean()*100,label='Tidal stream',color=colors['tidal'],lw=2.7)
axs[1].plot(view.index,view.tidal*100,color=colors['tidal'],lw=.8)
for ax in axs:
    ax.axvspan(start,end,color='#d5e6e8',alpha=.35);ax.set_ylim(0,100)
axs[0].set_ylabel('25-hour mean output\n(% of capacity)');axs[1].set_ylabel('Hourly tidal\noutput (%)')
axs[0].legend(frameon=False,ncols=4,loc='upper center',fontsize=10)
axs[0].text(.50,.78,'Week averages: wind 1.9%, wave 3.4%,\ntidal 48.9%, solar 20.0%',transform=axs[0].transAxes,ha='center',fontsize=10)
axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
foot(fig,'Calculated from supplied modeled profiles, not measured turbine output. The lower panel shows regular tidal gaps.\nThis selected week illustrates complementarity; it does not establish year-round reliability or a universal pattern.')
save(fig,'03_tides_during_wind_lull')

for p in sorted((ROOT/'experiments').glob('*.json')):
    out['experiments'].append(json.loads(p.read_text()))
good={r['job']['id']:r for r in out['experiments'] if r['status']=='ok'}
base_id='scotland_3yr_no_tidal'
prices=[p for p in [140,120,100,90] if 'scotland_3yr_tidal_'+str(p) in good]
if base_id in good and prices:
    fig,axs=plt.subplots(1,2,figsize=(13,6.5));fig.subplots_adjust(left=.08,right=.97,top=.79,bottom=.21,wspace=.32)
    title(fig,'Cheaper tides can lower coastal supply cost',
          'Only completed cases shown. Isolated 1 GW load, northern Scotland, 2022–24 supplied profiles.')
    rs=[good['scotland_3yr_tidal_'+str(p)] for p in prices];base=good[base_id]['cost_usd_mwh']
    vals=[r['cost_usd_mwh'] for r in rs]
    axs[0].scatter(prices,vals,color=colors['tidal'],s=65,label='Tidal allowed',zorder=3)
    axs[0].axhline(base,color='#677a80',ls='--',label=f'No tidal: ${base:.0f}/MWh')
    for x,y in zip(prices,vals):axs[0].annotate(f'${y:.0f}',(x,y),xytext=(0,-18),textcoords='offset points',ha='center')
    axs[0].set_xlim(145,85);axs[0].set_ylim(min(vals)-14,base+20)
    axs[0].set_xticks([140,120,100,90]);axs[0].set_xlabel('Assumed tidal generation cost ($/MWh)')
    axs[0].set_ylabel('Whole modeled supply cost ($/MWh)');axs[0].legend(frameon=False,fontsize=9,loc='upper right')
    shares=[100*r['primary_generation_share'].get('tidal',0) for r in rs]
    axs[1].bar(range(len(prices)),shares,color=colors['tidal'],width=.58)
    for x,y in enumerate(shares):axs[1].text(x,y+1,f'{y:.0f}%',ha='center')
    axs[1].set_xticks(range(len(prices)),[f'${p}' for p in prices]);axs[1].set_ylim(0,max(shares+[40])+10)
    axs[1].set_xlabel('Assumed tidal generation cost ($/MWh)');axs[1].set_ylabel('Tidal share of dispatched generation (%)')
    foot(fig,'Every modeled hour served. Floating wind $74/MWh; supplied future storage costs; no nuclear in this sweep.\nShares include storage charging. No transmission, reserves or equipment outages. Prices are assumptions, not bids.')
    save(fig,'04_checked_tidal_costs')

options=[('scotland_3yr_tidal_100','Base storage assumptions',colors['ocean']),
 ('scotland_3yr_tidal100_ldes50','Long-storage energy costs 2×',colors['ocean']),
 ('scotland_3yr_tidal100_battery_only','Batteries only',colors['ocean']),
 ('scotland_3yr_nuclear_allowed','Supplied nuclear option allowed',colors['fission']),
 ('scotland_3yr_firm100','$100/MWh firm option allowed',colors['geothermal'])]
options=[x for x in options if x[0] in good]
if len(options)>=2:
    fig,ax=plt.subplots(figsize=(13,6.6));fig.subplots_adjust(left=.34,right=.96,top=.78,bottom=.22)
    title(fig,'Firm power can win this simplified coastal test',
          'Tidal price $100/MWh in every case. Same three-year profiles and 1 GW load; all hours served.')
    vals=[good[i]['cost_usd_mwh'] for i,_,_ in options]
    ax.barh(range(len(options)),vals,color=[c for _,_,c in options],height=.55)
    for j,v in enumerate(vals):ax.text(v+2,j,f'${v:.0f}/MWh',va='center')
    ax.set_yticks(range(len(options)),[label for _,label,_ in options]);ax.invert_yaxis()
    ax.set_xlim(0,max(vals)*1.18);ax.set_xlabel('Whole modeled supply cost ($/MWh)')
    foot(fig,'Both firm-power cases choose 100% idealized nuclear generation and no storage. This assumes 90% output available every hour.\nNo outages, reserves or construction constraints are modeled. Only completed cases shown; see the results table for status.')
    save(fig,'05_storage_and_firm_power')

if (ROOT/'BATCH_FAILURE.json').exists():
    out['experiment_batch_failure']=json.loads((ROOT/'BATCH_FAILURE.json').read_text())

(ROOT/'proposal_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'portfolio_totals':[out['portfolio'][k]['total_TWh'] for k in out['portfolio']],
                  'successful_experiments':len(good),'figures':len(list(FIG.glob('*.png')))},indent=2))
