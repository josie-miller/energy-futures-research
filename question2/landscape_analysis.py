"""Render Q2's standardized evaluations and new figures from versioned JSON inputs.
Run: python3 question2/landscape_analysis.py (numpy/matplotlib from requirements.txt).
No network required. Status labels describe evidence, not probabilities or forecasts.
"""
from pathlib import Path
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
D=json.loads((R/'company_profiles.json').read_text()); C=D['records']; S=D['sources']
T=json.loads((R/'technology_profiles.json').read_text())['records']
F=R/'figures';F.mkdir(exist_ok=True)
BG='#F5F4ED';INK='#193932';MUTED='#596D64';GREEN='#087F72';BLUE='#466CAA';ORANGE='#B75B35';GRID='#D8DFD5'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.parse_math':False,'figure.facecolor':BG,'axes.facecolor':BG,'text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':INK,'svg.fonttype':'none','savefig.facecolor':BG})
def links(ids):return '; '.join(f'[{S[k]["title"]}]({S[k]["url"]})' for k in ids)
def table(rows):return '| Evaluation field | Finding |\n|---|---|\n'+'\n'.join(f'| **{k}** | {v} |' for k,v in rows)+'\n'
# Preserve all records; missing commercial costs remain text, never zero.
assert len({r['id'] for r in T})==len(T)
assert len({r['id'] for r in C})==len(C)
assert all(k in S for r in C+T for k in r['source_ids'])
fields=[('What it supplies','service'),('Evidence and stage','evidence'),('Companies, owners and funding','companies'),('Cost and its basis','cost'),('Demand contribution and timing','demand_and_timing'),('Main limitations','limitations'),('Geopolitical effect','geopolitics'),('Assessment / next proof','assessment')]
intro='''# Q2 — Evaluate the energy technologies

**What can each technology supply, who is building it, what does it cost, and what still has to work?**

Research cut-off: **24 October 2026**. This is the technology assessment. **The user is developing Q3, the proposed mix.** No portfolio percentages are recommended here. Earth electricity is the main comparison; industrial heat, storage and fuels have their own service labels. The final project remains a visual website inspired by The Pudding.

## The answer in one minute

- **Solar, onshore wind, hydro and large fission already supply electricity at scale.** Their main questions concern local cost, construction, connections, operating performance and the timing of output.
- **Emerging technologies are at different stages.** Enhanced and closed-loop geothermal have early grid output; floating wind has operating arrays; selected small/advanced reactors are under construction. Those achievements do not yet establish cheap repeated fleets.
- **Fusion, ocean thermal, salinity power and wave-powered computing have larger gaps between their promise and verified commercial performance.** Wave and tidal electricity have real demonstrations and operating units; their main unresolved issue is repeatable cost and sustained delivery at much larger scale.
- **Storage and hydrogen are not additional energy sources.** Evaluate the service delivered, losses, duration and charging energy. Industrial heat storage must be compared in units of useful heat.
- **There is no honest single price for many emerging options.** “Not verified” is the finding where an operating commercial price has not been established—not an assumption of zero cost or technical failure.

These are our assessments of the evidence, not investment recommendations or a forecast of which company will win. The detailed records separate verified events, company reports, targets, models and our arithmetic.

## Read the comparison consistently

Every technology below uses the same eight fields: **output; evidence; companies/ownership/funding; cost; scale/timing; limitations; geopolitics; assessment.** Dollar values retain their stated geography, year and accounting boundary. US$100/MWh is 10 cents/kWh. A generation price does not purchase reliable electricity at every hour.

The company selection covers 28 manufacturers, developers and project groups chosen for relevant production, financing or operating evidence. It is **not an exhaustive global ranking**. Specific Chinese, European, North American, Korean and multinational examples are included; other important suppliers remain outside the detailed company audit. Public institutions and utilities also matter.

[Company-by-company records](LANDSCAPE.md) · [Detailed cost and scale calculations](COST_AND_SCALE.md) · [Methods and limits](METHODS.md) · [Review of the supplied evidence](EVIDENCE_REVIEW.md)

## What the evidence actually says

![Selected project evidence](figures/07_project_evidence.png)

An operating demonstration proves more than an announcement, but less than a repeatable fleet with known lifetime costs. The labels describe the **named product or project**, not every technology a company develops. An empty commercial-cost field is not a readiness percentage.

## Cost comparison

![Common-source US cost comparison](figures/01_costs.png)

Lazard’s US new-build comparison uses a common financing framework. Its US nuclear range reflects Vogtle; it is not a global nuclear price. Its coal and geothermal estimates have older inputs adjusted for inflation. The [cost appendix](COST_AND_SCALE.md) also gives global commissioned-project averages and regional nuclear assumptions.

![Ocean cost evidence compared with established renewables](figures/08_ocean_cost_evidence.png)

This second chart deliberately distinguishes established-project averages from early marine estimates. It describes the current evidence; it is not a cost ranking for identical hourly service. Wave and tidal learning targets are conditional and appear in their records below.

## Potential contribution to demand

![IEA scenarios by technology](figures/02_supply_scale.png)

These are published **scenario outcomes, not technical ceilings**. Each share uses its own scenario’s demand total. Advanced geothermal, SMRs and tandem solar belong inside their parent categories. Do not add them a second time. Company pipelines do not establish guaranteed market share.

![Scale required for one percent](figures/09_one_percent.png)

The 1% experiment is arithmetic with explicit average-output assumptions. It makes a proposed share concrete; it does not establish available sites, hourly reliability, cost or a feasible construction schedule.

## Technology index

Click a technology for its standardized evaluation. Expand only the records you need; the JSON files contain the same text for later website use.

| Technology | Service | Evidence stage |
|---|---|---|
'''
intro+='\n'.join(f'| [{x["name"]}](#{x["id"]}) | {x["group"]} | {x["status"]} |' for x in T)+'\n\n'
for x in T:
    intro+=f'<a id="{x["id"]}"></a>\n<details>\n<summary><strong>{x["name"]}</strong> — {x["status"]}</summary>\n\n'
    intro+=table([(name,x[key]) for name,key in fields])+'\nSources: '+links(x['source_ids'])+'\n\n</details>\n\n'
intro+='''## What Q2 establishes for Q3

The records supply **technology-specific evidence and constraints**, not an optimized allocation. For any proposed share, Q3 will need a location, customer service, annual and hourly output, build rate, complete financing, outages/maintenance, and costs for storage and networks. Ocean options deserve the same test as every alternative.

Important open fields remain: private-company control, current cost to finish some projects, independently audited long-term output, repeated-project costs, and regional construction limits. These gaps are named rather than filled with invented scores or prices. A company’s funding round does not establish cash remaining, project bankability or the electricity it can deliver.

## Files and reproducibility

- [Technology records](technology_profiles.json) and [company/source records](company_profiles.json) hold the standardized text and citations.
- [Landscape renderer](landscape_analysis.py) reproduces this answer, the company document and the three new PNG/SVG figures.
- [Numerical comparison model](technology_analysis.py) reproduces the earlier six figures and ten CSV datasets. [Detailed cost and scale appendix](COST_AND_SCALE.md) explains their boundaries.
- [Landscape figure inputs](landscape_figure_data.json) records every plotted value, assumption and source key. All source keys resolve in `company_profiles.json`.

No hourly reliability model, optimal mix, complete project due diligence or future deployment guarantee is claimed.
'''
(R/'ANSWER.md').write_text(intro)
company='''# Q2 — Companies, owners, money and delivery evidence

Checked **24 October 2026**. Companion to the standardized [technology evaluation](ANSWER.md).

These 28 selected records are examples with relevant evidence, not an exhaustive list of leaders. Manufacturer, technology developer, project owner and customer are different roles. An investor is not necessarily a controlling owner. Percentages retain their filing dates; undisclosed private ownership stays unknown.

Funding is recorded in original currency and by instrument. Equity, debt, grants, power-purchase agreements, guarantees and proposed raises are not added into a single “funding strength” number. Historical raises do not establish cash currently available. Company operating claims are labeled; projected dates are not treated as achieved milestones.

| Company / project group | Technology | Ownership evidence |
|---|---|---|
'''
company+='\n'.join(f'| [{x["name"]}](#{x["id"]}) | {x["family"]} | {x["ownership"]} |' for x in C)+'\n\n'
cf=[('Technology','family'),('Ownership / control','ownership'),('Funding and instrument','funding'),('What has happened','evidence'),('Cost evidence','cost'),('Demand and scale','demand'),('Limitations','limitations'),('Geopolitical effect','geopolitics'),('Next evidence needed','next_evidence')]
for x in C:
    company+=f'<a id="{x["id"]}"></a>\n<details>\n<summary><strong>{x["name"]}</strong> — {x["family"]}</summary>\n\n'
    company+=table([(a,x[b]) for a,b in cf])+'\nSources: '+links(x['source_ids'])+'\n\n</details>\n\n'
company+='''## How geopolitics changes the comparison

| Mechanism | Evidence or basis | Consequence to assess |
|---|---|---|
| Manufacturing concentration | IEA 2026 supply-chain assessment | Compare local delivered equipment prices and alternate suppliers; a low factory price does not include tariffs or delivery risk. |
| Nuclear fuel capacity | DOE January 2026 enrichment awards: US$900m each to two HALEU suppliers and one LEU supplier | Identify fuel requirements by design and actual delivery dates. A funding award is not finished enrichment capacity. |
| Supported early markets | UK AR7 awarded 20.9 MW of tidal contracts; EU demonstrations support marine projects | Compare subsidized revenue with production cost and the next unsupported project. Awards are future capacity. |
| Sovereign and utility finance | EDF, KHNP/KEPCO, OPG and Equinor ownership/project records | Cost of capital and willingness to carry construction risk can change which projects proceed. State ownership is not zero cost. |
| Strategic customer funding | Computing buyers and industrial firms appear as investors, customers or both | Separate equity from purchase commitments; inspect who pays for delays, cancellation and overruns. |
| Physical infrastructure | IEA grid analysis describes long development/connection times | A finished generator without a usable connection cannot serve the intended grid load. |
| Local marine and water access | Site-specific engineering and permitting mechanism | Ports, seabed, cables, navigation, fisheries, water rights and ecology must be assessed for the selected location. |

These consequences are analytical mechanisms, not invented percentage penalties or a legal assessment of a particular project. Detailed contractual and local regulatory work remains for site selection.

Sources: '''+links(['supply','haleu','tidalpolicy','grids'])+'\n'
(R/'LANDSCAPE.md').write_text(company)
# Figures: values and states are explicit, with no invented readiness scores.
evidence=[
 {'label':'LONGi · solar modules','state':'Factory deliveries','detail':'86.58 GW modules shipped in 2025','sources':['longi']},
 {'label':'Vestas · wind turbines','state':'Factory deliveries','detail':'14.54 GW delivered in 2025','sources':['vestas']},
 {'label':'Fervo · Cape Station','state':'Early operation','detail':'33 MW net commercial output reported','sources':['fervo']},
 {'label':'Eavor · Geretsried','state':'Early operation','detail':'First loop feeds grid; economics under review','sources':['eavorvisit']},
 {'label':'Orbital · O2','state':'Early operation','detail':'2 MW operating tidal turbine','sources':['orbital','orbitalfuture']},
 {'label':'Hydrostor · Goderich','state':'Early operation','detail':'1.75 MW discharge; small storage reference','sources':['hydro']},
 {'label':'CorPower · C4','state':'Demonstration','detail':'Grid-connected wave demonstration','sources':['corpower']},
 {'label':'Minesto · Dragon','state':'Demonstration','detail':'Extended grid-connected testing reported','sources':['minesto']},
 {'label':'Sweetch · OPUS-1','state':'Demonstration','detail':'Real-water demonstrator; scale unproven','sources':['sweetch']},
 {'label':'TerraPower · Natrium','state':'Construction / development','detail':'Construction authorized; plant not operating','sources':['nrc','terrabuild']},
 {'label':'GEH / OPG · BWRX-300','state':'Construction / development','detail':'300 MW first unit under construction','sources':['cnsc']},
 {'label':'Form · Cambridge','state':'Construction / development','detail':'Customer acceptance not verified in this review','sources':['formstatus']},
 {'label':'CFS / Helion · fusion','state':'Construction / development','detail':'Commercial net-electric output unverified','sources':['cfsarc','helion','fusionroadmap']},
 {'label':'Global OTEC · Bahamas','state':'Construction / development','detail':'Feasibility study; not a power plant','sources':['globalotec']},
]
colors={'Factory deliveries':GREEN,'Early operation':BLUE,'Demonstration':'#9B7A30','Construction / development':ORANGE}
fig=plt.figure(figsize=(15,10));ax=fig.add_axes([.045,.15,.91,.70]);ax.set_xlim(0,1);ax.set_ylim(-.6,len(evidence)-.4);ax.invert_yaxis();ax.axis('off')
for i,r in enumerate(evidence):
    if i%2==0:ax.axhspan(i-.47,i+.47,color='#E9EDE3',zorder=0)
    ax.text(.01,i,r['label'],va='center',fontsize=11,fontweight='bold')
    ax.text(.335,i,r['state'],va='center',fontsize=10,color=colors[r['state']])
    ax.text(.62,i,r['detail'],va='center',fontsize=9.5)
fig.text(.045,.96,'A funded company is not yet a working power station',fontsize=23,fontweight='bold',va='top')
fig.text(.045,.91,'Selected project evidence as of 24 October 2026. These are different milestones—not readiness scores.',fontsize=12,color=MUTED)
fig.text(.055,.86,'NAMED PRODUCT / PROJECT',fontsize=9,color=MUTED);fig.text(.35,.86,'EVIDENCE CATEGORY',fontsize=9,color=MUTED);fig.text(.61,.86,'WHAT THE RECORD ESTABLISHES',fontsize=9,color=MUTED)
fig.text(.045,.085,'Sources: issuer filings, project/operator disclosures, NRC/CNSC and the Geothermal Alliance Bavaria site visit.\nCompany claims and unverified acceptance are identified. Factory GW, generator MW and storage MW are not interchangeable.\nEarly operation does not establish long lifetime or repeatable cost. Full source mapping: landscape_figure_data.json.',fontsize=9,color=MUTED,linespacing=1.6)
for e in ['png','svg']:fig.savefig(F/('07_project_evidence.'+e),dpi=170)
plt.close(fig)
costs=[{'technology':'Onshore wind','usd2025_mwh':33,'basis':'commissioned-project average'}, {'technology':'Solar PV','usd2025_mwh':44,'basis':'commissioned-project average'}, {'technology':'Offshore wind','usd2025_mwh':78,'basis':'commissioned-project average'}, {'technology':'Tidal stream','usd2025_mwh':358,'basis':'early-sector estimate'}, {'technology':'Wave','usd2025_mwh':454,'basis':'early-sector estimate'}]
fig,ax=plt.subplots(figsize=(12,7.8));fig.subplots_adjust(left=.22,right=.92,top=.74,bottom=.26)
for i,r in enumerate(costs):
    ax.barh(i,r['usd2025_mwh'],color=GREEN if i<3 else ORANGE,height=.58,hatch=None if i<3 else '//',alpha=.9)
    ax.text(r['usd2025_mwh']+8,i,str(r['usd2025_mwh']),va='center',fontweight='bold')
ax.set_yticks(range(len(costs)),[r['technology'] for r in costs]);ax.invert_yaxis();ax.set_xlim(0,510);ax.set_xlabel('Generation cost · 2025 US dollars per MWh');ax.grid(axis='x',color=GRID);ax.set_axisbelow(True)
for s in ax.spines.values():s.set_visible(False)
fig.text(.045,.95,'Wave and tidal power still have high estimated costs',fontsize=23,fontweight='bold',va='top')
fig.text(.045,.87,'Green: averages for established renewable projects commissioned in 2025.\nOrange: early marine estimates with a smaller and less certain evidence base.',fontsize=12,color=MUTED,linespacing=1.6,va='top')
fig.text(.045,.065,'Source: IRENA Renewable Power Generation Costs in 2025 (2026), pp. 13–16 and 153–156.\nGeneration costs, not prices for identical hourly supply. Offshore wind is wind, not wave/tidal energy.\nConditional learning estimates at 2 GW cumulative deployment: tidal ~140 and wave ~120 US$/MWh; not current offers.',fontsize=9.5,color=MUTED,linespacing=1.6)
for e in ['png','svg']:fig.savefig(F/('08_ocean_cost_evidence.'+e),dpi=170)
plt.close(fig)
scale=[]
for name,cf in [('Solar',.2),('Onshore wind',.35),('Offshore wind',.45),('Wave or tidal (illustration)',.35),('Fission or geothermal',.85)]:
    scale.append(dict(technology=name,assumed_average_output_fraction=cf,low_twh=600,high_twh=800,low_gw=600/(8.76*cf),high_gw=800/(8.76*cf)))
assert math.isclose(scale[3]['high_gw'],260.9262883235486)
fig,ax=plt.subplots(figsize=(12,7.5));fig.subplots_adjust(left=.31,right=.93,top=.74,bottom=.25)
for i,r in enumerate(scale):
    ax.plot([r['low_gw'],r['high_gw']],[i,i],lw=14,solid_capstyle='butt',color=BLUE if i!=3 else GREEN)
    ax.text(r['low_gw']-8,i,f"{r['low_gw']:.0f}",ha='right',va='center');ax.text(r['high_gw']+8,i,f"{r['high_gw']:.0f} GW",va='center',fontweight='bold')
ax.set_yticks(range(len(scale)),[f"{r['technology']}\n{r['assumed_average_output_fraction']:.0%} average output assumed" for r in scale]);ax.invert_yaxis();ax.set_xlim(0,540);ax.grid(axis='x',color=GRID);ax.set_axisbelow(True);ax.set_xlabel('Installed electrical capacity required · GW')
for s in ax.spines.values():s.set_visible(False)
fig.text(.045,.95,'Even 1% of future demand means a large fleet',fontsize=23,fontweight='bold',va='top')
fig.text(.045,.87,'1% of our two Q1 planning cases = 600–800 TWh of electricity per year.\nEvery range supplies the same annual amount; availability by hour still differs.',fontsize=12,color=MUTED,linespacing=1.6,va='top')
fig.text(.045,.055,'Calculation: capacity (GW) = annual electricity (TWh) / [8.76 × average-output fraction].\nFractions are explicit illustrations, not company guarantees. Solar is on an AC plant basis.\nNo siting, transmission loss, retirement, construction-rate, cost or hourly-reliability claim is implied.',fontsize=9.5,color=MUTED,linespacing=1.6)
for e in ['png','svg']:fig.savefig(F/('09_one_percent.'+e),dpi=170)
plt.close(fig)
(R/'landscape_figure_data.json').write_text(json.dumps({'as_of':'2026-10-24','evidence_map':evidence,'cost_comparison':{'source_ids':['irena'],'rows':costs},'one_percent_experiment':{'source':'Our arithmetic using the Q1 60000/80000 TWh planning cases; not a forecast','rows':scale}},indent=2)+'\n')
print(f'Rendered {len(T)} standardized technology categories, {len(C)} company/project profiles and 3 PNG/SVG figures.')
