# Q4 methods and reproduction

Q4 is a scenario calculator and a research synthesis. It is not a demand forecast, global dispatch optimization, climate model or investment-grade project estimate.

## Files

- `inputs.json`: explicit assumptions, 2050 Q3 snapshot and the supplied 2100/2200 allocations.
- `centuries.py`: reproducible arithmetic, checks, CSV tables and six PNG/SVG graphics.
- `results.json`: all calculated results and source metadata for website use.
- `blue_planet_growth.csv`: the main 2%-then-1% trajectory.
- `blue_planet_mix.csv`: technology output, assumed capacity factor, calculated fleet and simple replacement/growth illustrations.
- `blue_planet_scale_checks.csv`: average output, installed fleet, area and the partial nuclear heat account.
- `demand_scenarios.csv`: constant 0.5%, 1%, 2% and 3% alternatives.
- `space_hardware.csv`, `heat_benchmarks.csv`, `illustrative_services.csv`: separate physical scale experiments.
- `inputs/`: all five original user uploads and a SHA-256 inventory.

## Reproduce

From the repository root, using the shared requirements:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python question4/centuries.py
```

The script reads local inputs and writes beside itself. It makes no network requests. PNG/SVG metadata may change on rerun without changing the underlying numbers.

## Demand and generation

For a constant rate, `generation(year) = generation(2050) × (1 + growth)^(year − 2050)`.

Blue Planet uses 80,000 TWh in 2050, 2% through 2100 and 1% after 2100. The 2100/2200 mix totals are the rounded integers in the supplied table, differing from the exact growth formula by less than 1 TWh. No probability is assigned to a path. Starting at 60,000 instead scales every path by 0.75.

Power and energy conversions:

- `average electrical TW = annual TWh / 8,760`.
- `installed GW = annual TWh / (8.76 × capacity factor)`.
- Capacity factors summarize average plant output; they do not prove hourly service.
- Storage is not a primary generation source. Storage losses, curtailment and grid losses must be included in a future complete system model.

The 2050 source allocation is a snapshot of current Q3's upper case. Future source allocations come from the Blue Planet upload. The source-by-source transition has not been optimized, and some categories decrease between the designs. No instruction to retire working plants follows from that difference.

## Area and fleet replacement

`area(m²) = average output(W) / average power density(W/m²)`.

Offshore wind uses a **1.5–6 W/m² sensitivity**, not a certified site yield. Offshore solar uses an assumed **12.3 W/m²**. Ocean surface is assumed to be 361 million km². Total ocean area is a denominator, not available leasable area. Areas cannot be added without deciding overlap, spacing, ecological exclusions, access and cable capacity.

The fleet chart uses `replacement capacity/year = installed capacity/lifetime`, with 30 years for solar and offshore wind and 60 years for fission. This is a stationary age-distribution approximation. Real retirement cohorts, refurbishment and repowering may differ substantially. The chart adds 1% annual growth to illustrate the task just after 2100; it does not recreate an exact fleet history or force individual technologies to follow the global demand growth rate.

## Heat

The general sensitivity uses `flux = electricity(W) × selected added-heat fraction / conversion efficiency / Earth area`.

The selected fraction is 25% and conversion efficiency 40%; these are independent scenario assumptions. The 0.1 and 1 W/m² lines are comparison markers, not safety limits or temperature predictions. Earth is approximated by a sphere of radius 6,371 km.

The Blue Planet mix calculation separately counts only fission-plus-fusion output at an assumed 40% electrical conversion. It excludes geothermal extraction, changes in solar absorption, greenhouse gases, ocean circulation and other climate effects. Existing solar/wind flows are not automatically counted as new planetary heat; their use still affects the environment. Seawater cooling redistributes heat within Earth.

## Space and service examples

Solar collector area is `electrical power / (incident solar flux × efficiency)`. Inputs are 1,361 W/m² at Earth's distance, 586.2 W/m² at Mars's average distance and 30% conversion. The calculation assumes normal incidence and uninterrupted illumination. It excludes eclipses, surface atmosphere/dust, degradation and transmission.

Radiator emitting area is `heat / (emissivity × Stefan–Boltzmann constant × temperature^4)`, with emissivity 0.9 and an ideal cold-space view. The model neglects absorbed sunlight, planetary radiation, gradients and structural constraints. It rejects 1 GW of load heat per 1 GW example; solar-cell and power-conversion losses require additional heat rejection. Two-sided panel footprint is at best half the emitting area, subject to useful views from both sides.

The 14-day lunar-night example is a simplified equatorial-style case; illumination at polar sites differs. Battery mass at 250 Wh/kg is an ideal accounting example before margins, depth of discharge, temperature, losses, redundancy and space qualification.

Hydrogen, water, carbon removal and computation are illustrative service budgets, not additions to the growth trajectory. The carbon-removal example specifically assumes an all-electric 2 MWh/tonne budget rather than borrowing a mixed heat/electricity figure and calling it electricity. It does not demonstrate net removals or permanent storage.

## Checks

The script checks source shares and annual totals, demand at the starting year, proportional scaling from the lower demand case, linear hardware scaling, radiator temperature scaling, and hand-computable service-energy conversions. These verify arithmetic, not forecasting accuracy or engineering feasibility. Original uploads remain byte-identical and are separately hashed.
