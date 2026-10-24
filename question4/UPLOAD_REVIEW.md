# Review of the supplied Blue Planet research

The five uploads are valuable inputs to an ambitious long-range scenario. Their original bytes remain in `inputs/`. The current answer retains their 2100/2200 generation allocations and corrects the interpretation of the quantities below. Embedded draft directions are source material, not new authorization.

## What carries forward

- **The growth arithmetic works.** Starting with 80,000 TWh in 2050, 2% growth through 2100 gives 215,327 TWh; switching to 1% then gives 582,420 TWh in 2200, rounded. All four supplied generation-table columns sum to their stated totals.
- **The future ocean shares work.** Offshore wind, offshore solar, OTEC, tidal, wave and salinity total 99,200 TWh in 2100 and 371,400 TWh in 2200: 46.1% and 63.8% of their respective systems.
- **The central idea is useful.** Marine infrastructure can collect renewable flows, serve coastal customers and share some facilities. Its economic value depends on the actual system and customer.
- **The radiator and seawater-flow calculations broadly work**, when their different areas and physical boundaries are clearly stated.

## Corrections for publication

| Draft statement | What the current answer says |
|---|---|
| 2025's 31,089 TWh is “IEA WEO 2025 actuals” | The supplied baseline is preserved but not treated as independently verified 2025 actual data. Q1's consistent historical reference is **31,229 TWh in 2024**. |
| 2050's global mix is a Stage 3 least-cost result | No supplied global hourly optimization establishes that. Current Q3 is a **proposed** 15% ocean allocation. The uploaded 10.2% version remains a historical alternative. |
| 99,200 TWh ocean output in 2100 is “7× all today's electricity” | It is about **3.18× the whole world's 2024 electricity generation**. Total 2100 generation, 215,327 TWh, is about 6.90× that baseline. |
| Offshore wind needs about 8/21 TW in 2100/2200 | Those are **average output**. At a 45% capacity factor, the installed fleets are **17.76/45.66 TW**. |
| OTEC needs 0.9/4.6 TW | These are again average net output. At an assumed 85% capacity factor, installed net-electric ratings are **1.07/5.37 TW**. The generation mix does not include pumping as a separate free energy source. |
| 7 TW is a “no-harm ceiling” | It is a historical model comparison involving ocean temperature response, not a certified ecological or commercial limit. Newer modeling changes the rate/duration/climate assessment. |
| The 110 TWh tidal value is a global physical ceiling | The cited review derives a quasi-practical estimate from **90 sites**, about **20% of 426 candidates**. It is an incomplete site-based estimate, not a universal cap. |
| Offshore solar below 20% local coverage is safe | A study of three modeled North Sea settings evaluated specific processes and productivity measures. It does not establish a global safety rule. |
| Offshore solar at 12.3 W/m² is an established globally transferable density | It is retained as a **scenario assumption**. Site coverage, platform area, moorings, exclusion zones, sea state, spacing and shading must be distinguished. |
| A 1 GW Chinese offshore solar project proves GW-scale floating arrays | Secondary reporting describes the cited 1,223-hectare project as pile-supported. This review does not rely on it as a verified floating-solar benchmark; the 12.3 W/m² assumption stands independently as a sensitivity to test. |
| All today's power needs 0.074% of the ocean at that density | Using 31,229 TWh and 12.3 W/m² gives approximately **290,000 km², or 0.080%**. This is area arithmetic, not proof the area can be permitted or operated. |
| Tides are predictable, so they provide constant power | Predictability helps scheduling. Currents still weaken or reverse, and availability is not identical to the astronomical resource. |
| A modeled 92% OTEC profile demonstrates a commercial capacity factor | The supplied profile is a resource/operating assumption. Q3 found values above its nominal rating and clipped them in checked runs. It is not a measured multi-year commercial plant record. |
| Fusion with seawater deuterium “is ocean energy too” | Fuel origin can be discussed separately. It remains **fusion**, and counting it as marine renewable generation would obscure the comparison. |
| The ocean is the only route without added planetary heat | Land solar and wind also redirect existing flows. Extraction can still alter reflection, mixing and circulation. A small direct-heat term is not a complete climate assessment. |
| The sea is empty | It contains ecosystems, fisheries, livelihoods, navigation, infrastructure and competing rights. The denominator “all ocean area” is not a map of available sites. |
| The high seas have no legal regime | UNCLOS already governs relevant freedoms, rights and obligations. A coordinated energy-development framework may need further work, but “no law applies” is not accurate. |

## OTEC: keep the ambition, replace the safety label

The 2013 assessment estimated large global OTEC resources using a simplified circulation model. The new scenario's 4.57 TW average output in 2200 is below the draft's 7 TW reference, but that inequality does not establish ecological acceptability.

A 2025 study explicitly examines how extraction rate, duration and climate state affect the resource. It finds high initial extraction can deplete usable temperature differences, and results depend materially on the scenario. The correct next task is coupled physical and ecosystem modeling, followed by operating evidence—not simply checking a box under 7 TW. [2013 assessment](https://doi.org/10.1016/j.renene.2012.07.014), [2025 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12069477/).

## Wind and solar: footprint is not proof of availability

The wind footprint calculation is internally consistent if the assumed density is **average electrical output per farm area**. At 1.5–6 W/m², 180,000 TWh/year spans roughly **3.42–13.70 million km²**, or **0.95–3.79% of total ocean area**. The high-density end reflects a particular open-ocean atmospheric simulation, not a guaranteed worldwide operating yield. [Possner and Caldeira](https://www.pnas.org/doi/10.1073/pnas.1705710114).

At 12.3 W/m², 150,000 TWh/year of offshore solar uses approximately **1.39 million km²**. A one-percent-ocean deployment at that density would yield about **388,970 TWh/year**. Neither result says the footprint is safe, storm-proof, cheap, connected to customers, or free of competing uses. The published ecological study itself calls for more spatially detailed research. [North Sea study](https://os.copernicus.org/articles/16/195/2020/index.html).

Do not add the wind and solar percentages as if their areas necessarily overlap or never overlap. The design of co-located farms decides that. Shared export cables can also limit simultaneous output.

## Fuel stocks: abundant does not mean an available power system

The draft's fuel-year illustration assumes a fixed **178 TW electrical draw**, chosen from the constant-2% high-demand case. That is different from the main Blue Planet 2200 average of **66.49 TW**. Any retained figure must label the scenario correctly.

The uranium calculation depends on the assumed inventory, conversion efficiency, burnup, enrichment requirement and recycling. The deuterium calculation assumes an advanced, fully burned reaction chain; 7.2 MeV per deuteron is not a demonstration that an ordinary D–D reactor can deliver that performance. These calculations do not establish economical extraction, fuel processing, reactor construction, maintenance or complete fuel-cycle closure. Commercially relevant D–T fusion also needs a tritium supply strategy. [ITER tritium program](https://www.iter.org/machine/supporting-systems/tritium-breeding).

“Years of fuel” calculated at a constant annual draw must not be used under exponential demand growth. If a stock equals **Y years of initial consumption**, then consumption growing at rate **g** exhausts that mathematical stock after approximately `ln(1 + g × Y) / ln(1 + g)` years. An illustrative stock equal to 1.1 billion constant-consumption years becomes about **854 years at uninterrupted 2% growth**. This is a mathematical comparison, not a depletion forecast. The current headline therefore discusses fuel options without claiming billion-year economic energy security.

## Cooling and heat: a fair comparison

For 1 GW of waste heat at 300 K, emissivity 0.9 and ideal views of deep space, the required emitting area is **2.42 km²**. A two-sided radiator can have **1.21 km² of panel footprint** if both faces radiate effectively. These are different measures. Higher-temperature heat can use less area, but the equipment and thermodynamic cycle must support that temperature.

For seawater at an assumed density 1,025 kg/m³ and heat capacity 3,990 J/kg/K, rejecting 1 GW with a 1°C temperature rise requires about **245 m³/s** of flow. That number excludes pumps, heat exchangers, fouling, local discharge limits, intake effects and recirculation. It does not prove an underwater computer is cheaper, more efficient or easier to repair. Claimed percentage savings from data-centre announcements are not carried forward without comparable workload and system boundaries.

The draft's **0.029 W/m²** arithmetic for 2200 fission-plus-fusion heat is reproducible at 40% conversion efficiency. It is a partial source-origin account, not the entire Blue Planet climate effect. Comparison with a historical “today” forcing estimate cannot establish safety. [NASA thermal-control basis](https://www.nasa.gov/wp-content/uploads/2021/10/7.soa_thermal_2021_0.pdf).

## Resource estimates and deployment gates

The tidal review's 110 TWh estimate is partial. The wave 850 TWh number depends on a particular extraction methodology, and the salinity 625 TWh label has not been reconstructed here from its underlying source. They remain research references rather than enforced physical limits in a solved system. [Tidal review](https://ora.ox.ac.uk/objects/uuid%3A25b79764-64f0-47ad-9f8d-883dee27eba2).

The draft's “DOE $74/MWh” floating-wind target and “3 GW guarantees sub-$100 tidal” formulations were already corrected in Q3. Use Q3's methods and source qualifications. Learning depends on what gets built, financing, operating experience and the chosen cost basis; a deployment threshold does not guarantee a price.

UNCLOS Articles 56, 60 and 87 establish relevant rights and duties for offshore energy, installations and high-seas activities. This research does not resolve a specific project's legal permissions. [UNCLOS text](https://www.un.org/Depts/los/convention_agreements/texts/unclos/unclos_e.pdf).

**Editorial decision:** keep the Blue Planet imagination and the explicit future allocations. Present resource, cost, ecosystem and operating results at their actual level of evidence. Publish the checks as part of the story so readers can see which assumptions matter.
