"""Question 1 scale model. Python 3, standard library only.

Run: python3 demand_model.py
Writes CSV/JSON beside this script. This is a sensitivity prototype, not a forecast.
Anchor: IEA Electricity Mid-Year Update 2026, published 23 July 2026.
https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary
IEA reported consumption is retained as its own boundary; it is not gross generation.
"""
from pathlib import Path
import csv
import json

OUT = Path(__file__).resolve().parent
BASE_TWH = 28600.0
BASE_YEAR = 2025
RATES = [0.02, 0.03, 0.04]
rows = []
for rate in RATES:
    for year in range(BASE_YEAR, 2051):
        demand = BASE_TWH * (1 + rate) ** (year - BASE_YEAR)
        rows.append(dict(year=year, assumed_growth_rate=rate,
                         demand_twh=round(demand, 6),
                         increase_vs_2025_twh=round(demand - BASE_TWH, 6),
                         evidence_type="illustrative sensitivity"))
with (OUT / "demand_sensitivity.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

milestones = [r for r in rows if r["year"] in (2030, 2040, 2050)]
capacity = [{"generation_twh_per_year": 1000, "assumed_capacity_factor": cf,
             "capacity_gw": 1000 / (8.76 * cf)} for cf in (.2, .4, .9)]
data = {
    "baseline": {"year": 2025, "twh": BASE_TWH, "type": "IEA reported historical estimate",
                 "report_date": "2026-07-23",
                 "source": "https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary"},
    "published_forecast": {"2026_growth_percent": 3.6, "2027_growth_percent": 3.8,
                           "2027_twh_rounded": 30700},
    "milestones": milestones,
    "annual_capacity_equivalents": capacity,
    "illustrative_loads_twh": {
        "10_million_evs_at_12000_km_and_0.18_kwh_per_km_at_charger": 10e6 * 12000 * .18 / 1e9,
        "100_million_households_adding_2000_kwh_per_year": 100e6 * 2000 / 1e9,
        "100_gw_facility_load_at_85_percent_load_factor": 100 * 8.76 * .85},
    "same_useful_heat_100_twh": {"gas_input_twh_at_efficiency_0.9": 100 / .9,
                                "heat_pump_electricity_twh_at_cop_3": 100 / 3},
    "same_annual_load_100_twh": {"peak_gw_at_load_factor_0.8": 100 / (8.76 * .8),
                               "peak_gw_at_load_factor_0.4": 100 / (8.76 * .4)},
    "limitations": ["No probabilities attached to growth rates; no sector calibration yet.",
                    "Published 2027 forecast is a separate benchmark, not spliced into curves.",
                    "Capacity equivalents assume full-year operation and do not establish reliability.",
                    "No losses, retirements or curtailment added to the demand sensitivity.",
                    "Load examples are independent assumptions, not additive market forecasts."]}
(OUT / "model_results.json").write_text(json.dumps(data, indent=2))
for r in milestones:
    print(f'{r["assumed_growth_rate"]:.0%} | {r["year"]} | {r["demand_twh"]:,.0f} TWh/yr')
assert len(rows) == 78
assert abs(data["illustrative_loads_twh"]["10_million_evs_at_12000_km_and_0.18_kwh_per_km_at_charger"] - 21.6) < 1e-10
assert all(abs(c["capacity_gw"] * 8.76 * c["assumed_capacity_factor"] - 1000) < 1e-8 for c in capacity)
