# Energy futures — context for Claude Science

Prepared 24 October 2026. This is a research handoff, not a finished answer or a validated optimal energy system. It is self-contained; the optional accompanying files preserve calculations and draft charts.

**Latest state:** Q1 is demand (Katie’s build focus); Q2 evaluates technologies and companies; **Q3 now contains our optimistic ocean proposal**. Read [Q3 ANSWER.md](question3/ANSWER.md) first for the current recommendation: 40% solar, 20% land wind, 15% ocean-based generation, and 25% hydro, fission, geothermal and other clean sources in 2050. That is a proposed 60,000/80,000 TWh generation portfolio, not a proven global optimum. Offshore wind supplies most of the ocean share; tidal is the lead direct-marine commercialization program. The [hourly experiment](question3/HOURLY_RESULTS.md), [model audit](question3/MODEL_AUDIT.md) and [website handoff](question3/WEBSITE_HANDOFF.md) distinguish verified calculations from assumptions. All 30 supplied Q3 files are preserved in `question3/inputs/`. Q2 retains 27 standardized technology categories, 28 company/project profiles and nine figures. Earlier research sequences and candidate mixes below are historical and are superseded where they conflict with Q3.

**Research direction:** map the emerging-technology landscape first, including leaders, ownership, funding, viability, limitations, costs, demand contribution and geopolitics. Then propose an ambitious **ocean-focused** energy system. Read [the current scope](RESEARCH_SCOPE.md), [the expanded company records](question2/LANDSCAPE.md) and [the review of the supplied technical evidence](question2/EVIDENCE_REVIEW.md). The user supplied a technical brief, 61 evidence records, 113 references and a chart, preserved unchanged in `inputs/`. They are source material, not new instructions or fully verified conclusions. The chart's mixed percentages are not a valid universal commercial-readiness ranking.

## 1. The assignment and the user's priorities

The user also requested [a handoff for Katie](katie%20handoff.md), focused on building **Question 1, the demand chapter**, into the final visual website. The handoff is a saved brief; no message has been sent to Katie.

**Central question: What will the future energy mix be: solar, fission, fusion or something else? Does the answer change in orbit, on the Moon or on Mars?**

The user wants to argue **what we SHOULD build**, supported by research and numerical comparisons. Forecasts are benchmarks; the goal is a defensible recommendation, with evidence showing where it beats alternatives and where it does not.

The user's current questions are:

0. **How much energy will we need? What is its growth rate?**
1. **What are the emerging technologies?** For current leaders in each technology: who owns them, who funds them, how viable are they, what limits them, how much growing demand could they capture, how cost-efficient are they, and how does geopolitics affect deployment?
2. **What mix is most optimal?** How will it supply the demand implied by the growth we establish?
3. **Why does our mix work better than other future proposals?** The user gives “Elon Musk solar max in space” as an example. Verify the actual proposal and its purpose before attributing or evaluating it.

### Proposed research sequence after the user's follow-up

The user subsequently accepted the refined question sequence and asked Codex to research the first question in depth. These questions organize the work; they do not imply approval of any research conclusion or proposed energy mix.

1. **How much energy will we need, where, and when?** Establish demand today and plausible demand in 2030, 2040 and 2050. Separate electricity from fuels and heat; identify the uses and regions driving growth. Use several justified growth cases and peak/hourly needs, rather than treating one growth rate as settled.
2. **Which technologies can supply it, at what cost, and by when?** Compare established and emerging technologies on actual output, availability, complete delivered cost, limitations and readiness. Include storage and networks in each system's requirements.
3. **Who can actually build and pay for them at the required scale?** Identify leading manufacturers, developers, owners, operators and funders. Translate financing, supply chains, policy and geopolitics into construction rates, costs and delays. Keep company research tied to delivery evidence.
4. **What mix should we build to meet demand reliably at the lowest acceptable total cost?** State the emissions and reliability requirements. Include growth, replacement of retiring plants, storage, networks and construction limits. Produce regional recommendations and an explicit deployment path.
5. **How does our mix perform against the strongest alternatives, and what would change the winner?** Compare under matching service requirements. Separate forecasts of likely outcomes from proposals for desirable systems. Verify each attributed proposal before testing it; show cases where alternatives win.
6. **How does the recommendation change in orbit, on the Moon and on Mars?** Compare the same defined load with complete system mass, cost, reliability, lifetime and delivery requirements. Separate power used in orbit from orbital electricity transmitted to Earth.

Each section should produce a decision and a numerical comparison, with a visual that explains the result. The goal remains a recommendation about what to build, with uncertainty and conditions that could overturn it.

**Final deliverable: an experimental, visual, interactive website inspired by [The Pudding](https://pudding.cool/).** It should tell an understandable story through experiments and graphics, with a clear argument and accessible methods. A report, dashboard or collection of static charts alone is not the final product.

Writing preferences: direct language, concrete comparisons, no unnecessary jargon. Every major visual should answer a question, state the result, and explain why it matters. The user wants substantial research and decisive progress, not another general outline.

Earlier context supplied by the user described strong interest in ocean energy, including Panthalassa, and possible ocean/nuclear combinations. Preserve that hypothesis and test it seriously. **The user has not required ocean energy to win, selected a reactor, accepted any numerical mix, or approved a particular business model.** Do not turn assistant suggestions into user decisions. The user also asked to broaden beyond AI; study overall energy use.

Keep the scope to this central energy-mix question. Battery economics, company financing and industrial demand belong here when they affect the answer; do not turn them into separate unrelated research projects.

## 2. Where the work stands

Completed: research into major technologies, costs, ocean energy and space power; source-table extraction; transparent calculation scripts; seven earlier draft PNG/SVG charts; an initial Figma demand canvas. A subsequent Question 1 research pass adds a detailed demand answer, six new figures, six CSV datasets, and reproducible calculations in `question1/`.

Not completed: a calibrated sector-by-region demand model; hourly reliability analysis; total delivered system costs; an optimized mix; systematic company ownership/funding research; quantitative geopolitical scenarios; comparison with a verified Musk proposal; website design or implementation.

**No result yet establishes that “our mix” is cheapest, reliable every hour, or superior to existing projections.** Those are the next research tasks. Some positions below are reasonable working judgments; numerical shares below are only an assistant-selected test case.

This handoff was created for Claude Science, after which the user asked Codex to continue, refine the research questions, and research Question 1. The new Question 1 figures have not been added to Figma. The website does not yet exist.

### Question 1 research update — 24 October 2026

Read [the full demand answer](question1/ANSWER.md) and its six figures before continuing. Its calculations are in `question1/demand_analysis.py`, with exact inputs, sources and limitations in `question1/demand_results.json`.

- **Planning recommendation:** compare supply systems against roughly **60,000 TWh/year of generation in 2050** under policy-led pathways and **80,000 TWh/year** under a more electrified net-zero pathway, versus **31,229 TWh in 2024**. These are published-system benchmarks, not a confidence interval or a ceiling. Recalculate required generation for the losses and operating needs of the proposed mix.
- **Growth:** the long-term generation endpoints imply **2.4–3.7% annual growth over 2024–2050**. Near-term electricity demand grows around **3–4%**, but there is no single permanent energy-growth rate. Total final consumption may grow slowly or fall while electricity grows.
- **Drivers:** buildings supply about half of added final electricity use in the stated-policies case. Industry and transport supply about three-quarters in the net-zero case. These shares come from rounded WEO sector data; fuel production is outside this final-use ledger.
- **Place:** China, India and Southeast Asia account for roughly **54% of added world electricity demand** through 2050 in the stated-policies case. Regional annual and hourly requirements must guide later supply comparisons.
- **Population:** WEO population grows **18%**, while electricity demand grows **82%**. Holding electricity per person constant would raise demand to only **32,285 TWh**, versus the scenario's **49,657 TWh**. The difference combines living standards, industry, electrification, efficiency and other changes; it is not a causal estimate of each driver.
- **AI:** IEA's 2026 update gives data-centre electricity of **485 TWh in 2025** and **950 TWh in 2030**, around 3% of world demand then. Data centres are included in the sector totals. They can have large local effects without explaining most global growth.
- **Timing:** an explicit experiment with 10 million electric cars holds annual energy at **21.6 TWh**, while a four-hour charging window needs **14.8 GW** and a ten-hour window **5.9 GW**. These assumptions illustrate timing; they are not a forecast or an estimate of total grid peaks.
- **New source:** [IEA Electrification, September 2026](https://www.iea.org/reports/electrification), pp. 50–51, compares about **925 TWh of demand added each year in 2025–2035** under stated policies with nearly **1,400 TWh/year** in its goal-driven high-electrification scenario. Its final-energy denominator excludes non-energy uses; WEO's total final consumption includes them. Do not compare their electricity shares without reconciling that difference.
- **Independent check:** [DNV's public 2026 outlook](https://www.dnv.com/energy-transition-outlook/2026/) projects electricity demand growing **80% by 2050**. The full data were not obtained, so this is a directional check, not a precisely reconciled second forecast.

This completes a substantive published-scenario comparison, not an independently calibrated demand forecast or an hourly adequacy model. The next model should measure activity, energy per unit, equipment adoption and hourly schedules by region. The website's first chapter can show why a more electrified world may need less total energy but much more electricity.

### Question 2 research update — 24 October 2026

Read [the full technology answer](question2/ANSWER.md) for the latest cost and deployment comparison. It adds six PNG/SVG figures, ten CSV datasets, a source ledger in `question2/technology_results.json`, and the reproducible `question2/technology_analysis.py`. This update takes precedence over older cost or deployment summaries below where they differ.

- **What to build:** solar and wind for most new electricity, complemented by dependable low-emissions supply, storage and networks. This is a supported direction, not an optimized percentage mix.
- **Comparable starting costs:** Lazard's July 2026 US new-build ranges are $37–99/MWh for onshore wind, $40–98 for solar, $51–129 for combined-cycle gas, and $175–255 for new US nuclear based on Vogtle. These are generation costs, not equal-service system costs or global prices. Existing reactors, restarts and repeat-build nuclear assumptions have different cost boundaries.
- **Supply scale:** in the same WEO cases as Question 1, solar and wind supply 31,365 TWh/year (54% of stated-policies generation) or 58,759 TWh/year (73% of net-zero generation) in 2050. Fission supplies 5,531–6,853 TWh, hydro 6,383–7,398, and geothermal 452–825. These are conditional scenario outcomes, not technical maxima.
- **Construction matters:** the net-zero capacity endpoints imply average net additions of about 848 GW/year of solar, 264 GW/year of wind, 25 GW/year of fission and 45 GW/year of hydro over 2024–2050. Gross construction must also replace retirements. Keep AC/DC capacity definitions consistent.
- **Reconsider the older draft mix:** 15% nuclear in an 80,000 TWh world needs about 1,612 GW at 85% average output, or about 46 GW/year of net growth from the 2024 fleet, before retirements. Its 2% geothermal share also exceeds the WEO net-zero geothermal output. Neither assumption is yet justified as the default.
- **Enhanced geothermal:** Fervo reported its first 33 MW Cape Station unit commercially operating on 1 October 2026. This is a company-reported operating milestone, not proof of the entire planned project or long-term fleet economics. The IEA's much larger potential of nearly 6,000 TWh/year depends on cost and deployment improvements; do not add it to WEO output as an independent supply source.
- **SMRs and fusion:** model SMRs within total fission. The IEA's 40/120/190 GW SMR cases convert to about 298/894/1,415 TWh/year at our assumed 85% output. Commercial fusion costs remain unproven; CFS and Helion dates are company targets. Even 1% of an 80,000 TWh world would need about 107 GW of fusion at 85% output, equivalent to roughly 269 plants of 400 MW.
- **Storage:** our explicit battery experiment costs about $114 per stored-and-delivered MWh at 350 cycles/year, $505 at 52 cycles and $2,436 at 10 cycles. These include assumed charging electricity and describe that battery's service, not the cost of an entire renewable grid. Frequent use is central to economics; other forms of long-duration flexibility need comparison.

The company ownership/funding and geopolitical work remains incomplete. Hourly reliability, total system cost and a justified optimal mix also remain open. The new Question 1 and Question 2 figures have not been added to Figma.

The research repository is [josie-miller/energy-futures-research](https://github.com/josie-miller/energy-futures-research), private. It preserves reports, data, charts, scripts, the original supplied context and the earlier Figma creation script. The README distinguishes current answers from exploratory drafts and links the underlying reports.

## 3. Working answer to test

The evidence currently supports this direction:

- **Earth:** build large amounts of solar and wind, the networks that connect them, storage and flexible demand, while maintaining and expanding dependable low-emissions supply where it is economical. Existing fission, hydro and geothermal deserve separate consideration from expensive first-of-a-kind projects.
- **Fission:** retain safe, economical existing reactors; assess new plants by region, repeatable construction, financing, fuel and delivery evidence. Small modular reactors are not automatically cheap because they are small.
- **Fusion:** fund development, but do not require unproven commercial output to meet the baseline demand plan. Change that judgment when operating evidence warrants it.
- **Ocean:** pursue measured demonstrations and plausible early markets. Do not infer low delivered cost from the size of the ocean resource. Wave, tidal stream, tidal range, offshore wind and floating nuclear are different technologies.
- **Earth orbit:** solar plus storage is a strong starting point for ordinary near-Earth missions. Orbit, eclipse pattern, power level, maintenance and heat rejection can change the answer.
- **Moon and Mars:** fission plus local solar/storage deserves serious preference for essential continuous loads, particularly through darkness or dust. Mission-specific mass, cost, reliability and readiness still need comparison.

The common design idea is **cheap local generation plus dependable supply for the hours it cannot cover**. The hardware changes with location. Wave generators do not transfer to the Moon or Mars. Coastal nuclear uses water as a heat sink; that alone does not establish a benefit from combining it with wave power. Space systems need radiators.

These are provisional research positions, not settled conclusions or user-approved choices.

## 4. Demand: verified anchors and what they mean

Keep four quantities separate: energy entering the system; energy delivered to users; useful services such as heat or motion; electricity. Electricity generation also differs from electricity demand. Avoid calling their entire difference “grid losses”: plant own-use and energy transformation also matter.

The latest short-term electricity forecast reviewed was [IEA Electricity Mid-Year Update 2026](https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary), published 23 July 2026: **28,600 TWh electricity consumption in 2025**, forecast growth **3.6% in 2026** and **3.8% in 2027**, reaching approximately **30,700 TWh in 2027**. Its revised baseline differs from the February report. Do not splice editions silently.

Long-term comparisons below use one consistent source: [IEA World Energy Outlook 2025, Annex A](https://iea.blob.core.windows.net/assets/5306bae2-1f99-402f-8d14-542bfa0ae96e/WorldEnergyOutlook2025.pdf), especially pp. 423, 429 and 437. These figures were extracted and the demand/generation table visually checked.

| World case | Electricity demand, TWh/year | Electricity generation, TWh/year |
|---|---:|---:|
| 2024 historical | 27,290 | 31,229 |
| 2050, stated policies | 49,657 | 58,081 |
| 2050, current policies | 50,667 | 59,426 |
| 2050, net-zero pathway | Not transcribed on the same demand basis | 80,175 |

These cases are conditional pathways with different assumptions, not probabilities, a confidence interval, or upper and lower physical limits. The net-zero case includes more electrification and energy conversion. Approximately 58,000–80,000 TWh/year is a useful **comparison range**, not a claim that future demand must fall inside it.

In the stated-policies case, additional electricity demand from 2024 to 2050 is:

| Non-overlapping region | Added TWh/year |
|---|---:|
| China | 7,029 |
| India | 3,159 |
| Southeast Asia | 1,880 |
| European Union | 1,741 |
| United States | 1,545 |
| Africa | 1,444 |
| Rest of world | 5,569 |
| **Total** | **22,367** |

For the broader energy question, WEO reports roughly **453 EJ of final consumption in 2024**: industry 174, transport 125, buildings 127, remainder about 27. Electricity is approximately 95 EJ of that final-consumption ledger. These rounded figures use a different accounting boundary from the electricity-demand table. Industry, buildings, transport, efficiency and electrification matter; AI is not the whole story.

An earlier simple sensitivity used `D(y) = 28,600 × (1 + g)^(y − 2025)`:

| Assumed annual growth | 2030 demand | 2040 demand | 2050 demand |
|---|---:|---:|---:|
| 2% | 31,577 | 38,492 | 46,921 |
| 3% | 33,155 | 44,558 | 59,882 |
| 4% | 34,796 | 51,507 | 76,243 |

Units are TWh/year of electricity consumption. These curves are **our assumptions**, not IEA forecasts. In particular, 60,000 TWh of consumption does not mean only 60,000 TWh of generation is needed.

**Next:** explain growth through population, living standards, industrial activity, cooling, transport, heating, efficiency and fuel substitution. Build regional hourly loads as well as annual totals. Reconcile historical sources and back-test before calling the result a forecast.

## 5. Technologies, cost and deployment evidence

### Comparable generation-cost starting point

[Lazard LCOE+ v19, July 2026](https://lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf), p. 7, gives these unsubsidized ranges, in US dollars per MWh:

| Technology | Range |
|---|---:|
| Onshore wind | 37–99 |
| Utility solar | 40–98 |
| Gas combined cycle | 51–129 |
| Solar plus storage | 61–156 |
| Geothermal | 67–111 |
| Offshore wind | 105–167 |
| New US nuclear | 175–255 |

Important boundaries: US nuclear uses Vogtle 3/4 experience, not all countries or existing reactors. Geothermal uses older estimates adjusted for inflation. Solar-plus-storage is not a promise of continuous supply. Financing assumes 60% debt at 8% interest and 40% equity at 12%. These generation costs do not establish a ranking for complete reliable systems.

For global commissioned-project evidence, consult [IRENA Renewable Power Generation Costs in 2025](https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025), published in 2026. Reported global weighted averages include onshore wind $33/MWh, solar $44/MWh and offshore wind $78/MWh. Keep that population separate from Lazard's ranges.

Cost comparisons need installation, financing, fuel, maintenance, replacement, storage, transmission, unused output, backup, decommissioning and the same emissions/reliability requirements. Storage shifts energy; it does not create it. Do not add independently calculated generation and storage cost figures without checking their denominators.

### Evidence and limits by technology

| Technology | Research position | Main question still to resolve |
|---|---|---|
| Solar | Strong candidate for large-scale expansion | Where do networks, land, seasonal output and storage change delivered cost? |
| Onshore/offshore wind | Complements solar in many locations | Actual hourly complementarity, permitting, connection and marine costs |
| Hydro | Valuable existing generation and flexibility | Ecological limits, drought, suitable sites; reservoir vs run-of-river distinction |
| Conventional/next-generation geothermal | Potential dependable low-emissions supply | Drilling success, repeatability, reservoir life and location-specific cost |
| Existing/new large fission | Evaluate separately; dependable low-emissions output | Repeat construction, cost of capital, schedule, fuel and operating history |
| Small/advanced fission | Promising designs with varying readiness | Completed projects and repeated delivery, not announcement counts |
| Fusion | Development option, no required baseline contribution | Sustained net electricity after all plant loads; materials, fuel cycle, maintenance and cost |
| Wave/tidal | Pilot and early-market opportunity | Net output, repair access, survivability and complete project cost |
| Gas/coal, with or without carbon capture | Necessary comparison cases | Fuel exposure, emissions, capture/storage performance and future dependence |
| Bioenergy | Limited, site-specific contribution | Sustainable feedstock, competing uses and full emissions accounting |
| Storage, networks, flexible loads | Essential parts of portfolios | Duration, efficiency, location, build speed and actual services delivered |

Useful primary starting points: [IEA nuclear report](https://www.iea.org/reports/the-path-to-a-new-era-for-nuclear-energy/executive-summary), [DOE fusion roadmap](https://www.energy.gov/documents/fusion-science-and-technology-roadmap), [NRC fusion roadmap](https://www.nrc.gov/materials/fusion/fusion-roadmap), [IEA geothermal investment update](https://www.iea.org/commentaries/investment-in-next-generation-geothermal-is-surging-policies-are-key-to-further-growth).

[IEA Electricity 2026 — Grids](https://www.iea.org/reports/electricity-2026/grids) reports network projects can take 5–15 years against 1–5 years for renewable projects. Its more-than-2,500-GW connection-queue figure includes generation, storage and large loads; do not describe all of it as renewable generation. Building generators without their connections does not meet demand.

### Ocean and Panthalassa: preserve the distinction between promise and evidence

IRENA's 2026 report, pp. 153–156, describes wave/tidal stream as pilot to pre-commercial technologies. It gives indicative 2025 cost estimates of **$454/MWh for wave** and **$358/MWh for tidal stream**, with Europe-based projections of approximately **$120/MWh wave** and **$140/MWh tidal** at 2 GW cumulative deployment. These are early-stage surveys/models, not large samples of operating plants. Since 2010, it reports 27 MW wave and 43 MW tidal stream deployed worldwide; cumulative deployment is not necessarily capacity still operating. [Public report mirror](https://tethys-engineering.pnnl.gov/sites/default/files/publications/Dardour-Zamora-2026.pdf).

[Panthalassa's website](https://panthalassa.com/) and its [4 May 2026 company announcement](https://www.prnewswire.com/news-releases/panthalassa-raises-140-million-to-power-ai-at-sea-302761078.html) describe a $140 million Series B and wave-powered offshore AI inference. In this concept, electricity is used aboard the device and data leave by satellite; it is not simply a plant sending electricity ashore. Reported prototypes, a 2026 pilot and 2027 commercial plans are company claims/targets. Independently verified fleet-scale cost and lifetime performance were not established in this research.

Check the actual customer product: electricity, computing, fresh water or fuel. Compare complete cost per unit of that product. Include marine maintenance, connectivity and utilization. Ocean cooling is not costless.

Our wave sensitivity model:

```text
annual capital recovery factor = r(1+r)^n / [(1+r)^n − 1]
generation cost ($/MWh) = installed $/kW × (capital recovery factor + annual operating-cost fraction)
                          / (8.76 × net capacity factor)
```

Assume 7% real financing, 20 years, annual operating cost equal to 4% of installed cost, and 40% net average output. Results: $4,000/kW installed gives about **$153/MWh**; a **$100/MWh test target** requires about **$2,607/kW** installed. Doubling annual operating costs to 8% raises the $4,000/kW case to roughly $199/MWh. These are assumptions, not Panthalassa estimates. Early-stage financing may be more expensive. Include all installation, mooring, electrical and end-of-life provisions consistently; customer backup/storage remains additional.

Possible project sequence, proposed by the assistant: measure a roughly 1 MW pilot through two years including difficult seasons; then a 10–20 MW array; scale further only after repeatable output, repair and cost evidence. This is not a user-selected project or a funded deployment plan.

## 6. Company ownership, funding and geopolitics — an explicit research gap

An [initial company and funding map](question2/LANDSCAPE.md) now covers ten selected developers and several geopolitical mechanisms, using current primary disclosures. It is not exhaustive, and exact private-company ownership/control and many project owners remain unresolved. Do not imply that a comprehensive leader ranking exists. The latest user direction is to complete this landscape before proposing the ocean-focused mix.

For each important technology, select a few leaders using operating output, completed delivery, manufacturing scale or verified technical milestones—not publicity or valuation alone. Distinguish designer, equipment manufacturer, project developer, owner, operator, financier and customer.

Use a consistent company/project record:

```text
Technology and exact product; headquarters and production countries;
owner/control structure, including state ownership where relevant;
funders, dated funding amounts and type (equity, loan, grant, guarantee);
actual operating projects and measured output;
under-construction, financed, licensed, contracted and announced capacity separately;
customer and route to revenue;
installation cost, financing, operations and delivered-cost evidence;
materials/fuel/supplier dependencies;
earliest credible deployment and scalable annual manufacturing/construction;
remaining technical tests; reasons it could fail;
primary sources, evidence date and confidence.
```

For geopolitics, identify the **mechanism and numerical effect**: tariffs changing installed cost; restrictions changing supply or delivery time; fuel/enrichment dependencies; state finance changing interest rates; domestic-content rules; grid rules; mineral/refining concentration; manufacturing concentration; local consent; or export controls. Treat these as research questions until supported by dated evidence. Evaluate multiple regions rather than presenting one country's rules as universal.

Compare a policy/supply disruption case with a normal case. Show cost, build delay and output effects. In space, include launch capacity, mission approval, nuclear launch requirements and access to transport. Funding announcements and customer agreements do not establish a functioning power plant.

## 7. A numerical mix exists only as a test case

The assistant created an annual generation budget totaling **80,000 TWh/year in 2050**, approximately the scale of the WEO net-zero generation case. Shares were selected to make a concrete model, **not optimized or approved by the user**:

| Technology | Assumed share | TWh/year | Assumed average output / rated power | Implied total GW | Average net GW added/year, 2024–2050 |
|---|---:|---:|---:|---:|---:|
| Solar | 45% | 36,000 | 18% | 22,831 | 794.9 |
| Wind | 30% | 24,000 | 35% | 7,828 | 257.6 |
| Fission | 15% | 12,000 | 85% | 1,612 | 45.8 |
| Hydro | 8% | 6,400 | 40% | 1,826 | 15.0 |
| Geothermal | 2% | 1,600 | 85% | 215 | 7.7 |

Formula: `GW = annual TWh / (8.76 × capacity factor)`. Starting fleet from WEO 2025: solar 2,164 GW; wind 1,131; fission 420; hydro 1,437; geothermal 15. Confirm compatible solar AC/DC and gross/net capacity conventions before publishing build-rate comparisons.

This is annual arithmetic only. It does not include an hourly dispatch model, retirements, a full storage/network build, unused generation, complete costs or a forecast of achievable construction. Replacement of retired plants makes gross construction higher. The fission and geothermal expansion requirements are substantial hypotheses to test.

Do not present the table as “the optimal future mix.” Change or discard it if regional optimization disagrees. A 60,000-TWh case can scale the annual budget down by 25%, but reliability and costs will not necessarily scale proportionally.

For perspective, WEO's net-zero case has roughly 44% solar generation, 29% wind and 9% nuclear in 2050, alongside other sources. The candidate above changes those shares; it has not demonstrated an improvement over the IEA case.

### What a defensible mix model must do next

Define “best” before optimization: suggested objective is minimum full delivered cost subject to explicit reliability and emissions limits, then report construction feasibility and supply-chain exposure separately. These priorities are proposed assumptions, not user-approved numerical targets.

Choose representative regions and use multiple weather years. At each hour:

```text
generation + imports + storage discharge
    = served demand + exports + storage charging + unused output
```

Enforce plant limits, outages, transmission limits, storage power/energy/efficiency, fuel availability, build rates and retirement dates. Model flexible demand with real service constraints. Track unserved energy and hours of shortage, rather than letting a large annual surplus hide outages.

Compare at least: renewables/storage/networks; renewables plus dependable low-carbon supply; the same system with wave/tidal; and a development-success case for fusion. Also compare against current policy projections. Use the same demand, weather, financing, emissions and reliability requirements where the comparison permits. Show where the recommendation loses as well as wins.

A useful background model is [Sepulveda et al., 2018, on dependable low-carbon generation](https://doi.org/10.1016/j.joule.2018.08.006). It motivates testing the value of such supply; it is not proof that today's proposed mix wins in every region.

## 8. Space: compare the same job in different environments

Separate three fundamentally different proposals:

1. Generate electricity in orbit and **use it there**.
2. Generate electricity in orbit and **beam it to Earth**.
3. Power equipment or settlements **on the Moon or Mars**.

An orbital data center is not automatically a space-solar power station supplying Earth's grid. Do not attribute one of these concepts to Musk without the original dated statement, design and intended customer.

Use a **100 kW continuous electrical load** as a transparent comparison case: 876 MWh per Earth year. This is a design assumption, not a colony-demand forecast. Then test 10 kW, 1 MW and growing loads, and distinguish essential life-support loads from work that can wait.

### Existing storage calculation

Assumptions: zero solar during the stated gap; battery pack 200 Wh/kg; 80% usable energy; 95% discharge efficiency. Battery nameplate energy = `load × gap / (0.8 × 0.95)`.

| Example | Gap | Battery nameplate energy | Battery mass |
|---|---:|---:|---:|
| Representative low Earth orbit | 35 minutes | 76.8 kWh | 0.384 tonnes |
| Mars night | 12.3 hours | 1,618 kWh | 8.09 tonnes |
| Mars no-solar stress test | 72 hours | 9,474 kWh | 47.37 tonnes |
| Non-polar lunar-night illustration | 14 days | 44,211 kWh | 221.05 tonnes |

These are **battery-only** figures, excluding arrays, charging hardware, thermal systems, packaging beyond the assumed pack, degradation, replacements and spares. They do not compare complete solar and reactor systems. The 72-hour Mars case is an analyst-selected stress test, not a forecast or worst possible storm. Polar Moon sites require actual terrain/illumination data, not a universal 14-day night assumption.

Sources: [NASA STS-116 press kit](https://www.nasa.gov/wp-content/uploads/2023/05/162182main-sts-116-press-kit.pdf), [NASA lunar surface technology](https://www.nasa.gov/lunar-surface-technology/), [NASA Mars facts](https://science.nasa.gov/mars/facts/), [NASA lunar environment](https://www.nasa.gov/reference/moonbase-environment/).

### Stronger mission evidence

[NASA Mars Surface Power, February 2025](https://www.nasa.gov/wp-content/uploads/2025/02/iparch07-wp-mars-surface-power.pdf), p. 2, states fission was selected as primary surface power for initial crewed Mars missions. Page 6 gives historical study estimates:

| Mission design | Approximate load description | Solar system | Fission system |
|---|---|---:|---:|
| 2009 DRA 5 | 26 kW cargo; ~35 kW crew | 22.5 t | 6–8 t |
| 2016 EMC | 26 kW cargo; 31 kW crew | 11.7 t, northern hemisphere | 9 t |
| 2020 POD | 9 kW cargo/crew | 11.22 t | 7.93 t |

These pairs use different historical mission designs. They are not current commercial offers, flight-proven reactor masses, or values to multiply directly into the separate 100 kW illustration.

For solar beamed to Earth, [NASA's 2024 space-based solar power study](https://ntrs.nasa.gov/citations/20230018600) evaluates two representative 2050 designs at baseline costs of **$0.61/kWh and $1.59/kWh**. These are modeled outcomes, not an operating market or permanent physical limit. Favorable combinations of launch, manufacturing and other assumptions improve the results. Compare those assumptions with current evidence before claiming space solar is either inevitable or impossible.

**Next space model:** complete system mass delivered to the actual site; launch and landing cost; array output over time; storage and replacement; reactor conversion, shielding, separation and radiators; redundancy; installation; repair/resupply; mission lifetime; and probability/consequences of failure. Do not carry terrestrial $/MWh rankings straight into space.

## 9. How to test alternative visions fairly

For every competing vision, record: original author/source/date; exact claim; location and customer; load; promised capacity and completion date; cost boundary; required technical advances; financing; and what is already demonstrated.

Priority comparisons:

- Solar-heavy Earth systems with storage and transmission.
- Renewables plus fission/hydro/geothermal.
- Wave/tidal supplying a grid versus power used offshore.
- Fusion-dependent expansion versus a plan that works without fusion.
- Solar powering orbital equipment versus electricity beamed down to Earth.
- Solar/storage versus fission/hybrids on specified lunar and Martian sites.

The user wants an argument for our solution. **Earn that argument through matched comparisons; do not assume the answer in advance.** Report break-even conditions: e.g. what launch cost, battery mass, nuclear construction cost, wave maintenance rate or fusion completion date changes the winner?

The earlier user-supplied [Casey Handmer “Energy Predictions 2025” essay](https://caseyhandmer.wordpress.com/2025/12/08/energy-predictions-2025/) is a thesis to test, not independent validation of every cost claim.

## 10. Website direction: experiments that reveal the argument

This is a proposed story structure, not a finished design. Use The Pudding as inspiration for narrative, playful interaction and explanatory visuals; develop an original visual identity.

| Story beat | Reader experiment | Required evidence/model |
|---|---|---|
| How much more power? | Move through 2025–2050; change growth and electrification | Sourced sector/region demand; separate forecasts from assumed curves |
| What can we build? | Compare technologies and see actual vs announced projects | Technology, ownership, funding and deployment records |
| Cheap at noon, expensive at night? | Turn sunlight off; extend the gap from hours to days | Hourly generation and storage model with complete costs |
| Build a mix | Adjust a portfolio; see cost, shortages, emissions and annual construction | Regional model with equal service requirements |
| What could derail it? | Change fuel availability, interest rates or build delays | Dated geopolitical mechanisms and sensitivity cases |
| Change the planet | Carry the same load from Earth to orbit, Moon and Mars | Complete mission mass/cost/reliability comparisons |
| Does our answer survive? | Test the strongest alternative under favorable assumptions | Matched comparison and break-even results |

The site should have a visible argument and a conclusion, not just controls. Show one clear takeaway at a time, then let readers explore exceptions. Keep methods and sources accessible beside each result. Mark numbers as **measured**, **published scenario**, **company target**, or **our assumption**. Show ranges where justified; do not invent probabilities.

Prefer concrete units: homes, factories or a specified base only when their load assumptions are explicit; TWh/year for energy and GW for power. Distinguish 100 MW Earth illustrations from 100 kW space illustrations. Use plain-English explanations for technical terms. Provide mobile layouts, keyboard controls, reduced-motion support and a readable static fallback.

Current cream/green chart styling and Figma boards are provisional research assets, not a locked website aesthetic. The website can be much more experimental.

## 11. Existing artifacts and how to continue

Initial Figma file: [Energy Futures — 01 Demand Lab](https://www.figma.com/design/ozvOZDQZTTiUgPA6kCsGxv). It contains three earlier boards: research specification (`3:2`), demand sensitivity (`3:58`), and comparison units (`3:117`). The later seven-chart research set is local, not uploaded there.

Optional companion files, relative to this Markdown:

- `energy_models.py`: reproducible seven-chart calculation script; Python 3.9+, numpy and matplotlib. Run `python energy_models.py` after installing those libraries.
- `energy_model_results.json`: inputs, formulas' results, sources and limitations.
- `published_demand.csv`, `regional_growth.csv`, `generation_costs.csv`, `candidate_build.csv`, `wave_cost_sensitivity.csv`, `earth_storage.csv`, `space_storage.csv`, `nasa_mars_mass.csv`.
- `charts/01_demand.png` and `.svg`: published generation cases and regional growth.
- `charts/02_generation_cost.*`: Lazard cost ranges with boundaries.
- `charts/03_candidate_build.*`: **unoptimized assistant test case**, annual generation and net build rates.
- `charts/04_wave_threshold.*`: assumed installation/output/maintenance sensitivity.
- `charts/05_storage_duration.*`: storage energy for a 100 MW Earth load.
- `charts/06_space_storage.*`: battery-only mass for a 100 kW space load.
- `charts/07_nasa_mars.*`: historical NASA mission mass comparisons.
- Earlier `demand_model.py`, `demand_sensitivity.csv`, `model_results.json` and `research_brief.txt` concern the initial demand framing. This handoff takes precedence for the current task scope.

The code verifies annual generation sums and capacity arithmetic. That is not a reliability or optimization test. The draft chart titles must not be cited as independent evidence. Check data licensing before website publication: WEO 2025 Annex A identifies CC BY-NC-SA 4.0; IRENA and other sources have their own attribution and reuse terms.

### Recommended next research sequence

1. Reconcile the demand scenarios and choose explicit regional cases, dates, emissions and reliability requirements. Separate desired outcomes from forecasts.
2. Build the technology/company/funding/geopolitics evidence table. Update the as-of date and verify leader claims.
3. Construct and test regional hourly portfolios with realistic build-rate and retirement limits. Replace the arbitrary mix if the evidence points elsewhere.
4. Verify the strongest competing proposals, including the user's Musk example, using original sources and matched service requirements.
5. Complete orbit/Moon/Mars system comparisons; quantify which assumptions change the preferred solution.
6. Write a concise position for each environment, with evidence that would change it. Turn the strongest discoveries into the website's experiments and narrative.

Start from the evidence here, but remain willing to overturn the provisional answer. The objective is a clear, defensible recommendation that readers can test themselves.
