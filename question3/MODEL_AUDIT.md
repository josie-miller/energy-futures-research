# Audit of the supplied ocean proposal and model

24 October 2026. The supplied work is a useful starting experiment. The proposal in [ANSWER.md](ANSWER.md) retains its ambition while distinguishing physical resource, operating evidence, modeled costs and our recommendations.

## What reproduced

- All five supplied capacity-factor files were rebuilt from the raw compressed downloads using the supplied processing script. Maximum absolute differences were below **1.5 × 10⁻¹⁵**, consistent with floating-point rounding.
- The file named `Unconfirmed 462875.crdownload` contains that Python processing script. It is preserved under its original name. Its contents were inspected before execution in a separate working directory; the raw inputs were not overwritten.
- The profiles have unique, ordered, continuous hourly timestamps and no blank modeled capacity factors. The three-year files contain **26,304 hours**, including 2024's leap day. The 2010 file has 8,760 hours.
- The selected 2023 wind-lull averages reproduce: 1.85% offshore wind, 3.43% wave, 48.93% tidal and 19.99% solar. Wind–tidal correlation over 2022–24 is 0.011; wind–wave is 0.413.
- With the supplied 2035 cost coefficients, the checked 2023 no-new-nuclear case reproduces the original **$194.556/MWh** result to much less than $0.001/MWh. The checked version requires zero unmet demand.

This establishes computational reproducibility. It does not independently validate the underlying weather/ocean product, device power curves, calibration or commercial costs.

## Corrections that change the interpretation

| Issue | What the supplied files actually do | How we treat it |
|---|---|---|
| Unmet demand | `voll=5000` lets the optimizer buy non-delivery. Several three-year Scotland cases leave around 0.5% of demand unserved; the proportions differ between cases | Checked headline comparisons require **zero unmet demand in every supplied hour**. A common penalty is not equal achieved reliability |
| Marine mandate | `min_ocean` constrains capacity × potential output, before curtailment | A 30% label does not establish 30% delivered marine electricity. The checked explicit formulation constrains marine **dispatched primary generation** |
| Generation shares | The original `share` fields are generation used, including energy sent into storage, divided by demand; their sum can exceed 100% | Normalize only when describing the mix of dispatched generation. Do not label it a final-customer share. Storage losses are separately reported |
| Attribution | Original code prorates renewable curtailment across all available technologies each hour | This is an accounting convention, not a unique optimal dispatch. The checked fast formulation uses the same convention for comparability; an explicit dispatch formulation is used for the marine-share test |
| Floating-wind price | The 2035 fixed-cost input is **$247.604/kW-year**. At the actual Scottish 2022–24 mean output, that is about **$51/MWh**, rather than the pitch's stated $74 | Preserve the original case, and run a separate comparison calibrated to a stated **$74/MWh at the common three-year reference output**. This is a sensitivity assumption, not a verified DOE forecast |
| DOE attribution | The cited historical US Floating Offshore Wind Shot targets **$45/MWh by 2035**, not $74 | Correct the attribution. Neither figure is a demonstrated commercial price. [DOE](https://www.energy.gov/cmei/systems/floating-offshore-wind-shot) |
| Storage efficiency | `eta_b=.94` and `eta_l=.63` apply once on charging and once on discharging | Round-trip efficiencies are **88.36% and 39.69%**, respectively. They are not 94% and 63% |
| Storage cost | Energy and power capacities incur separate annualized charges | “$25/kWh storage” is an assumed energy component, not the complete installed or delivered cost. Retain the power charge and conversion losses |
| Storage capacity units | The original output dictionary is called `caps_GW`, but energy capacities are in GWh | Label `batt_E` and `ldes_E` as **GWh**, and `batt_P` and `ldes_P` as **GW** |
| Nuclear reliability | `nu[t] ≤ 0.9 × capacity` makes 90% available every hour, with flexible dispatch | This removes actual outage events and tends to favor firm coverage. Treat it as an idealized comparator, not a reliability study of a nuclear fleet |
| Flat demand | A constant load is useful for a particular industrial service | It is not universally the hardest demand shape. Peaks, heating and cooling can create harder cases; flexible customers can create easier ones |
| Technology competition | No fixed-bottom offshore wind, transmission, imports, hydro or geothermal is available in the supplied Scottish comparison | It cannot establish the cheapest clean system across all alternatives. Our proposal reintroduces those candidates |
| No finite resource limits | A site can expand indefinitely unless an explicit capacity maximum is passed | GW-scale solutions at one synthetic site require separate resource, wake, seabed and environmental studies |

For example, the supplied 2023 case labeled `min_marine_0.3` costs $196.67/MWh. Its tidal-plus-wave `share` fields sum to **0.238**, and marine energy is **20.64% of normalized dispatched generation**, not 30%. Its 1.1% cost increase does not price a genuine 30%-of-delivered-generation requirement.

## Weather and current inputs need care

**The 2010 case combines 2010 weather with 2023 tidal timing.** Its tidal column exactly matches the 2023 column. The processing script confirms this substitution. That is a useful synthetic alignment experiment, but it is not a reconstruction of actual 2010 tides. The phase between the imposed tide and the weather can affect the result.

The Scottish wind calibration is performed over the longer raw weather period, 2010–24. Its 54% target is therefore not the mean of each analyzed year. Supplied offshore-wind means are about **58.1%, 50.3% and 56.7% in 2022, 2023 and 2024**. Hywind's reported five-year average supports a calibration target, but it does not validate this different location or power curve. [Operator report](https://www.equinor.com/news/hywind-5-years-world-first-floating-wind-farm).

The raw current series has **120 missing hours during 2022–24**. The script interpolates up to six consecutive hours, then backfills and forward-fills remaining gaps. It calibrates turbine rated speed to achieve a target three-year mean output. That is not validation of a turbine at the actual site. The ocean model's stated coarse grid is especially consequential in narrow tidal channels.

The Hawaii sea-temperature series lacks **7,830 hours in 2022**. The script fills missing values with monthly averages from the available record. Its OTEC profile is a temperature-based proxy, not a plant design, and exceeds 100% of its reference capacity in **6,379 hours**. Checked runs cap output at a hard 100% AC rating and disclose that change. A plant whose rating is defined differently needs a different explicit model.

The raw downloads identify variables and site coordinates, and the script names ERA5/ERA5-Ocean and Mercator/SMOC via Open-Meteo. Exact API request parameters, time-zone declarations, product revisions, and original retrieval dates were not included. Preserve that provenance gap rather than reconstructing undocumented requests. Current evidence does not support treating modeled current speed as site-measured turbine inflow.

## Source corrections

1. **Tidal cost learning:** the ORE Catapult £78 ±25/MWh projection for 2035 assumes **2.6 GW global deployment**, with 877 MW UK and 783 MW France. Its **1 GW UK/France** point is £98 ±32/MWh. All are modeled costs in 2012 pounds. The supplied conversion factor of 1.8034 to 2025 dollars is an assumption, not a newly verified inflation/currency series. [ORE report, printed pp. 24–25](https://cms.ore.catapult.org.uk/wp-content/uploads/2022/10/Tidal-stream-cost-reduction-report-T3.4.1-v1.0-for-ICOE.pdf).
2. **Cumulative generation:** OEE's 127 GWh figure is cumulative **European** tidal-stream output through 2025. It is neither annual output nor a verified worldwide total. [OEE report](https://www.oceanenergy-europe.eu/wp-content/uploads/2026/09/Ocean-Energy-Stats-Trends-2026-1.pdf).
3. **Resource comparisons:** IEA's offshore-wind technical potential is not a commercial build forecast. The 2012 wave extraction percentage applies to the converter configuration chosen in that paper, not all current or future wave devices. The OTEC estimates represent modeled extraction/environmental cases, not a reliable economic supply range. Do not add overlapping resources or use them as evidence of affordable 2050 output. [IEA](https://www.iea.org/reports/offshore-wind-outlook-2019), [Gunn and Stock-Williams](https://tethys-engineering.pnnl.gov/publications/quantifying-global-wave-power-resource).
4. **Predictability:** tidal timing is valuable, but equipment availability, weather effects on currents and maintenance are not fixed by astronomy. Solar also has an astronomical component. Avoid “the only predictable renewable.”
5. **Co-location:** a modeled saving from one shared platform does not establish a general two-thirds wave-cost reduction. Wave and tidal sites need not coincide with wind sites. Sharing an export route also creates congestion and possible common failures.
6. **Nuclear comparator:** a contract strike price is not directly interchangeable with an unsubsidized production cost or a global future nuclear cost. The supplied $166.8/MWh idealized case is one sensitivity. Cheaper firm power needs to be allowed to win.

## How the new model is checked

`test_model.py` verifies units against a hand-calculated constant-generator case, a two-hour storage case, infeasibility when no power is available, explicit non-delivery accounting, and a marine-share constraint applied to dispatched output. Every successful research run checks its energy balance, storage equations, capacity limits and unmet-demand limit numerically.

The smaller formulation has the same cost optimization as explicit renewable dispatch when no generation-share rule is imposed. The source allocation of renewable curtailment is not unique, so precise technology shares should not be overinterpreted. The marine-share test uses explicit generation variables to prevent discarded potential output from satisfying the rule.

The checked runs preserve the original round-trip storage efficiencies and cost structure unless a named sensitivity changes them. The 30%/40% tidal-output tests hold the central case's annual cost per installed kW constant; the original sensitivity changed that cost to preserve a nominal $/MWh. Our version asks what happens if the same-priced asset produces less or more energy.

The 2010 stress case also retains the three-year reference annual fixed costs, rather than making equipment cheaper merely because a weather year produces less energy. Case definitions, solver outcomes and input hashes are saved with each result. Failed or timed-out optimizations are not reported as optimal solutions.

**Still needed for an investment-grade result:** multiple measured/validated sites, finer tidal hydrodynamics, actual regional demand, many weather years, out-of-sample fixed-capacity dispatch, transmission and cable failures, operating reserves, maintenance schedules, resource limits, environmental constraints, financing terms and retirement/replacement schedules. Reoptimizing separately for each weather case is not the same as proving that one built fleet survives every case.

## Final batch outcome and failed validation

The 24 October checked batch ended with exit code 1 after an `AssertionError` at the physical/accounting residual check in `ocean_model_checked.py` (line 223 in the executed version). That check requires the hourly equation residual below `2e-5`, the constraint residual below `2e-5`, and the absolute horizon energy-balance gap below `1e-3` GWh. The traceback does not identify which individual case triggered the failure.

The saved case files contain **16 optimal outcomes and one solver time-limit outcome**. Two cases have no saved validated result: `scotland_3yr_tidal_100` and `scotland_3yr_tidalcf30`. They are **not pending** and no cost or mix is inferred for them. The error cannot be assigned to one specific unsaved case from the available record. See [the batch failure record](BATCH_FAILURE.json) and [the full outcome table](checked_experiments.csv).

Saved optimal cases were retained and their stored physical residuals rechecked. The runner now catches assertion failures per case, saves `failed_validation` with the job identity and traceback locations, omits partial costs and capacities, and continues collecting the other cases. **No residual tolerances were weakened and no invalid solution was accepted.** The failing cases require a separate diagnosis before they can support conclusions; this publication does not claim that diagnosis is complete.
