# Sources and provenance

Original research reports are linked rather than copied into the repository. The models contain small source transcriptions and explicit assumptions. Source-specific rights and attribution apply.

[Structured source metadata](source_ledger.json) preserves URLs, pages, dates and qualifications from the models. The current company records and supplied-evidence review carry their own inline citations. The supplied bibliography in `../inputs/tech_references.csv` has not been fully verified.

## Model source entries

### question1/demand_results.json

- [WEO2025](https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf): 2025-11-12
- [ElectricityFeb2026](https://www.iea.org/reports/electricity-2026/demand): 2026-02-06
- [ElectricityJul2026](https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary): 2026-07-23
- [ElectrificationSep2026](https://iea.blob.core.windows.net/assets/1c696cc3-e251-46a9-8d4d-9edb2a4e806a/Electrification.pdf): 2026-09-22; 27, 29, 50–51
- [DNV2026](https://www.dnv.com/energy-transition-outlook/2026/): 2026
- [AI2026](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary%C2%A0): 2026
- [GER2026](https://www.iea.org/reports/global-energy-review-2026/key-findings): 2026

### question2/technology_results.json

- [WEO2025](https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf): 417, 423, 429, 453–456; Published scenarios and regional modeled costs; Annex A CC BY-NC-SA 4.0; Annex B CC BY 4.0
- [Lazard2026](https://www.lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf): 7, 11 and appendix; Unsubsidized modeled generation costs; 60% debt at 8%, 40% equity at 12%; nuclear based on Vogtle
- [IRENA2026](https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025): 13–18, 141, 153–156; 2025 USD; commissioned renewable project cost estimates; emerging technology estimates have a different evidence base
- [NETL2025](https://netl.doe.gov/projects/files/CostandPerformanceBaselineFossilEnergyPlantsVolume1BituminousCoalNaturalGastoElectricity_052125.pdf): 12–18; PDF pages 34–40; 2023 USD; modeled US Midwest plants, 85% utilization; gas $3.42/MMBtu; CO2 transport/storage included
- [Nuclear2026](https://www.iea.org/reports/global-energy-review-2026/technology-nuclear): 2025 capacity additions and retirements
- [GeothermalPotential](https://www.iea.org/reports/the-future-of-geothermal-energy/executive-summary): 2024 conditional low-cost case, not a forecast
- [Fervo2026](https://fervoenergy.com/fervo-energy-declares-commercial-operation-at-cape-station-ahead-of-schedule-leading-the-race-for-next-generation-geothermal-energy/): 2026-10-01; Company reports first 33 MW unit commercial; remaining phase I units not yet commercial
- [SMR](https://www.iea.org/reports/the-path-to-a-new-era-for-nuclear-energy/executive-summary): 2025 report: 40/120/190 GW in different 2050 cases, included within nuclear, not additional
- [OPG](https://www.opg.com/wp-content/uploads/2026/03/2025-Q4-OPG-PR-MDA-FS-FINAL.pdf): First Darlington SMR budget C$7.7bn including shared infrastructure, interest, escalation and contingency
- [FusionDOE](https://www.energy.gov/articles/energy-department-releases-finalized-fusion-science-and-technology-roadmap-accelerate): 2026-06-09; Development roadmap; commercial electricity is a goal
- [CFS](https://www.cfs.energy/technology/arc/): Company target: 400 MW early 2030s; no commercial operating cost
- [Helion](https://www.helionenergy.com/orion): Company target: at least 50 MW and initial operations in 2028
- [Grids](https://www.iea.org/reports/electricity-2026/grids): Project times: renewables 1–5 years, grids 5–15; scope and permitting matter

### energy_model_results.json

- [weo](https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf): 423, 429, 437; 2024 fleet capacity on page 423
- [lazard](https://lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf): 7 and associated notes
- [irena](https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025): 153–156
- [nasa_mars](https://www.nasa.gov/wp-content/uploads/2025/02/iparch07-wp-mars-surface-power.pdf): 2 and 6
- [leo](https://www.nasa.gov/wp-content/uploads/2023/05/162182main-sts-116-press-kit.pdf)
- [moon](https://www.nasa.gov/lunar-surface-technology/)
- [mars_day](https://science.nasa.gov/mars/facts/)

## Boundaries

WEO 2025 Annex A identifies CC BY-NC-SA 4.0, and Annex B CC BY 4.0. Retain the figure attributions. Other sources have their own terms. Company releases establish announcements, not independent verification. Historical sources are dated and must not be presented as fresh observations.

Local download caches and PDF table screenshots used during review are not part of the repository. No runtime packages, browser state, login material or credentials are included.
