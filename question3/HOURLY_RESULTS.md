# Q3: checked hourly experiments

**Snapshot: 3 of 19 planned cases have saved optimal solutions.** Only these completed cases support numerical conclusions below. Unfinished or unsuccessful cases are not counted as evidence.

These are conditional model comparisons for an isolated, constant 1 GW load. All completed checked cases require zero unmet demand in every modeled hour. They use supplied 2035 cost assumptions, perfect knowledge of the weather, cyclic storage and no explicit equipment outages. They are not project bids, real-world reliability guarantees or a worldwide optimum. See [methods](METHODS.md) and [input audit](MODEL_AUDIT.md).

## Cost and energy comparisons

Generation shares below include energy sent into storage, before storage losses. They are not shares of electricity traced to the customer. Capacity is GW; storage energy is GWh. Tidal prices in case names are assumed generation costs in USD/MWh, not the complete supply cost.

| Case | Complete supply cost, USD/MWh | Tidal generation share | Direct marine generation share | Unmet demand, GWh | Long storage, GWh | Battery, GWh |
|---|---:|---:|---:|---:|---:|---:|
| original_2023_reliability_check | 194.56 | 0.0% | 0.0% | 0.000000 | 173.9 | 15.2 |
| scotland_3yr_no_tidal | 220.00 | 0.0% | 0.0% | 0.000000 | 124.2 | 23.4 |
| scotland_3yr_tidal_140 | 212.90 | 25.5% | 25.5% | 0.000000 | 171.3 | 12.2 |

## What the Scottish comparison says

Without tides, this restricted three-year system costs **$220.00/MWh**. Floating wind is priced at an assumed $74/MWh on a common reference profile; land wind, solar and storage can also be built.

- With tidal generation at an assumed **$140/MWh**, total supply cost becomes **$212.90/MWh**, a **3.2% reduction** ($7.10/MWh). The model builds 1.06 GW of tidal capacity and attributes 25.5% of dispatched primary generation to tides.

This is evidence for the value of tidal timing under the stated choices. The cheapest configuration can still use mostly land wind. The model has no transmission, reservoir hydro, geothermal, geographic diversity or flexible demand, and its storage and tidal technologies assume future performance. Adding alternatives can change the result.

## Cases without a completed optimal result in this snapshot

- `scotland_3yr_tidal_120`: not yet saved.
- `scotland_3yr_tidal_100`: not yet saved.
- `scotland_3yr_tidal_90`: not yet saved.
- `scotland_3yr_tidal100_ldes50`: not yet saved.
- `scotland_3yr_tidal100_battery_only`: not yet saved.
- `scotland_3yr_marine30`: not yet saved.
- `scotland_3yr_tidal100_wave80`: not yet saved.
- `scotland_3yr_nuclear_allowed`: not yet saved.
- `scotland_3yr_firm100`: not yet saved.
- `scotland_3yr_tidalcf30`: not yet saved.
- `scotland_3yr_tidalcf40`: not yet saved.
- `scotland_2010_no_tidal`: not yet saved.
- `scotland_2010_tidal100`: not yet saved.
- `hawaii_3yr_no_otec`: not yet saved.
- `hawaii_3yr_otec100`: not yet saved.
- `hawaii_3yr_otec90`: not yet saved.

## Reproduce and inspect

Each saved JSON contains its input hash, cost coefficients, capacities, generation, storage losses, unmet demand, solver status and physical residual checks. Run `python run_experiments.py --workers 2` to solve the cases, then `python analyze_proposal.py` and `python summarize_experiments.py` to refresh the figures and this document. See [METHODS.md](METHODS.md) for environment setup and boundaries.
