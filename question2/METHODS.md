# Q2 — Evaluation rules and boundaries

Research cut-off: 24 October 2026. Q2 evaluates technologies and companies. The user is developing Q3, the proposed mix.

## The standardized record

Each technology uses eight fields in the same order:

1. **What it supplies:** electricity, heat, storage, fuel, computing or several separately measured services.
2. **Evidence and stage:** what has actually operated, at what scale, and who reports it. A permit, shipment, prototype and operating plant establish different things.
3. **Companies, owners and funding:** name the manufacturer/developer, project owner and customer where established. Separate control from minority investment, and company capital from project capital.
4. **Cost and its basis:** geography, currency/year, plant boundary and evidence type. No invented commercial prices for technologies without a verified cost basis.
5. **Demand contribution and timing:** actual capacity/output, dated targets, published scenarios or explicit arithmetic. No unsupported company market-share forecasts.
6. **Limitations:** engineering, resource, maintenance, manufacturing, financing and connection constraints.
7. **Geopolitical effect:** the mechanism through which ownership, supply dependence, public support or international relationships change cost or delivery.
8. **Assessment / next proof:** our interpretation and the observation needed to strengthen it.

The separate company records use the same substance, with ownership and funding split into their own fields. The JSON is the source for the generated Markdown. Edit those records and rerun `landscape_analysis.py` to keep documents consistent.

## Evidence is not a score

- **Operating data / filing:** stronger evidence of a reported event; still inspect measurement boundaries and periods.
- **Regulatory authorization:** establishes permission for a specified activity, not performance or project completion.
- **Company disclosure:** establishes what a company reports. Performance, lifetime and economic claims may still need independent confirmation.
- **Published model / scenario:** conditional on stated inputs and policy/technology assumptions; not observed commercial delivery.
- **Target / proposed financing:** prospective and conditional. Do not count as operating output or received cash.
- **Our calculation / assessment:** explicitly labeled reasoning from stated inputs; not an external forecast.

“Early operation” describes experience with the named product/project, not the age of the whole technology family. No percentages of “readiness” are assigned. The supplied chart is retained as an input and evaluated in `EVIDENCE_REVIEW.md`; its mixed metrics cannot be a universal ranking.

## Costs that cannot be pooled

Lazard's modeled US 2026 generation ranges, IRENA's global estimates for projects commissioned in 2025, NETL's US engineering cases in 2023 dollars and NASA's conceptual space-system figures in FY2022 dollars are different comparison sets. Source years remain visible. No currency conversion, inflation adjustment or subsidy normalization beyond the original source is silently applied.

A funding round is not a plant cost. A power-purchase price is not necessarily production cost. A turbine/module price excludes other plant equipment and financing. A first nuclear unit with shared infrastructure is not an overnight equipment price. Existing plant operating cost excludes the original construction capital.

Grid generation cost excludes some or all system costs: balancing, connections, transmission, curtailment, reserve capacity and storage. A common annual MWh total is not equal hourly service. Heat, stored electricity, hydrogen and compute require different units; they must be compared against the same useful output.

## Scale arithmetic

`annual TWh = installed electrical GW × 8.76 × average-output fraction`

`required GW = annual TWh / (8.76 × average-output fraction)`

The one-percent figure uses 600–800 TWh/year, derived from the 60,000/80,000 TWh planning cases in Q1. Average-output assumptions are illustrative: solar 20%; onshore wind 35%; offshore wind 45%; wave/tidal 35%; fission/geothermal 85%. They are not guarantees, universal averages or assumptions of equal reliability. Solar is on an AC plant basis; module shipments are generally DC.

For example, 800 TWh/year at 35% output requires 260.9 GW. At 85% it requires 107.4 GW. This does not establish sites, cost, build pace or hours of delivery. Storage output is not added as new primary generation. Retirements and replacement construction matter separately.

WEO scenario outputs retain the original 2024 baseline and 2050 totals. We do not splice newer company announcements into the scenario series. SMRs are within fission; advanced geothermal within geothermal; tandem solar within solar; marine subtypes within marine. The geothermal potential study and WEO are alternative conditional cases, not additive amounts.

## Selection and incompleteness

The 28 company/project profiles were selected for relevant operating, manufacturing, regulatory or financing evidence and to show different business models. They are not a comprehensive list or a claim that all are their field's market-share leader. Several large global suppliers, specialist startups, transmission vendors and private ownership details remain outside the audit. Bioenergy, solar thermal, flow-battery ownership and the space-company landscape have thinner company-level coverage, explicitly identified in the records.

Unknown private control, undisclosed contract terms and missing full project costs remain unknown. Historical shareholder percentages and rounds keep their dates; a full current cap table is not inferred. The review does not establish company cash runway or perform investment due diligence.

Geopolitical consequences are reasoned mechanisms unless a specific cited policy outcome is given. We do not assign invented geopolitical risk scores, tariff rates or legal conclusions. Local permitting and contracts must be assessed for any selected project.

## Validation and publication

The renderer checks unique record IDs and source references; the packaging check verifies local links, hashes and ZIP integrity. All three new figures were visually reviewed, and numerical values are preserved in `landscape_figure_data.json`. These checks catch transcription/format problems, not future technology failure.

Source URLs, dates and types are in `company_profiles.json`; older model sources remain in `technology_results.json`. Full third-party reports are linked rather than republished. Retain source attribution and applicable terms; WEO Annex A is identified as CC BY-NC-SA 4.0 and Annex B as CC BY 4.0.
