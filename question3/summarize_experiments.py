"""Write a readable snapshot using only saved, successfully solved cases."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
jobs = json.loads((ROOT / 'experiment_jobs.json').read_text())
results = {}
for job in jobs:
    path = ROOT / 'experiments' / (job['id'] + '.json')
    if path.exists():
        results[job['id']] = json.loads(path.read_text())
ok = {key: value for key, value in results.items() if value.get('status') == 'ok'}
lines = ['# Q3: checked hourly experiments', '',
    f'**Snapshot: {len(ok)} of {len(jobs)} planned cases have saved optimal solutions.** Only these completed cases support numerical conclusions below. Unfinished or unsuccessful cases are not counted as evidence.', '',
    'These are conditional model comparisons for an isolated, constant 1 GW load. All completed checked cases require zero unmet demand in every modeled hour. They use supplied 2035 cost assumptions, perfect knowledge of the weather, cyclic storage and no explicit equipment outages. They are not project bids, real-world reliability guarantees or a worldwide optimum. See [methods](METHODS.md) and [input audit](MODEL_AUDIT.md).', '',
    '## Cost and energy comparisons', '',
    'Generation shares below include energy sent into storage, before storage losses. They are not shares of electricity traced to the customer. Capacity is GW; storage energy is GWh. Tidal prices in case names are assumed generation costs in USD/MWh, not the complete supply cost.', '',
    '| Case | Complete supply cost, USD/MWh | Tidal generation share | Direct marine generation share | Unmet demand, GWh | Long storage, GWh | Battery, GWh |',
    '|---|---:|---:|---:|---:|---:|---:|']
for job in jobs:
    r = ok.get(job['id'])
    if not r:
        continue
    s, c = r['primary_generation_share'], r['caps']
    marine = sum(s.get(k, 0) for k in ['tidal', 'wave', 'otec'])
    lines.append(f"| {job['id']} | {r['cost_usd_mwh']:.2f} | {s.get('tidal', 0):.1%} | {marine:.1%} | {r['unserved_GWh']:.6f} | {c.get('ldes_E', 0):.1f} | {c.get('batt_E', 0):.1f} |")
baseline = ok.get('scotland_3yr_no_tidal')
if baseline:
    lines += ['', '## What the Scottish comparison says', '',
        f"Without tides, this restricted three-year system costs **${baseline['cost_usd_mwh']:.2f}/MWh**. Floating wind is priced at an assumed $74/MWh on a common reference profile; land wind, solar and storage can also be built.", '']
    for price in [140, 120, 100, 90]:
        r = ok.get('scotland_3yr_tidal_' + str(price))
        if not r:
            continue
        saving = baseline['cost_usd_mwh'] - r['cost_usd_mwh']
        lines.append(f"- With tidal generation at an assumed **${price}/MWh**, total supply cost becomes **${r['cost_usd_mwh']:.2f}/MWh**, a **{saving / baseline['cost_usd_mwh']:.1%} reduction** (${saving:.2f}/MWh). The model builds {r['caps']['tidal']:.2f} GW of tidal capacity and attributes {r['primary_generation_share'].get('tidal', 0):.1%} of dispatched primary generation to tides.")
    lines += ['', 'This is evidence for the value of tidal timing under the stated choices. The cheapest configuration can still use mostly land wind. The model has no transmission, reservoir hydro, geothermal, geographic diversity or flexible demand, and its storage and tidal technologies assume future performance. Adding alternatives can change the result.']
for name, title in [('04_checked_tidal_value.png', 'Checked tidal cost comparison'), ('05_storage_and_firm_power.png', 'Storage and firm-power comparison')]:
    if (ROOT / 'figures' / name).exists():
        lines += ['', f'![{title}](figures/{name})']
pending = [j['id'] for j in jobs if j['id'] not in ok]
if pending:
    lines += ['', '## Cases without a completed optimal result in this snapshot', '']
    for case in pending:
        status = results.get(case, {}).get('status', 'not yet saved')
        lines.append(f'- `{case}`: {status}.')
lines += ['', '## Reproduce and inspect', '',
    'Each saved JSON contains its input hash, cost coefficients, capacities, generation, storage losses, unmet demand, solver status and physical residual checks. Run `python run_experiments.py --workers 2` to solve the cases, then `python analyze_proposal.py` and `python summarize_experiments.py` to refresh the figures and this document. See [METHODS.md](METHODS.md) for environment setup and boundaries.', '']
(ROOT / 'HOURLY_RESULTS.md').write_text('\n'.join(lines))
print(f'Hourly report: {len(ok)}/{len(jobs)} optimal cases')
