# Review of the supplied technical evidence

24 October 2026. Read with the original [brief](../inputs/technical_evidence_brief.md), [61-row evidence table](../inputs/tech_evidence.csv), [113-reference bibliography](../inputs/tech_references.csv), and [original chart](../inputs/tech_gap_chart.png).

**This is useful technical source material. Its single-percentage chart should not be used as a ranking of commercial readiness.** The originals are preserved unchanged. This review checks structure, units, interpretation and selected current claims; it is not a completed verification of all 113 references.

## What to retain

Keep the source links, distinction between measured and projected results, attention to maintenance and lifetime, and separate treatment of plasma gain versus electricity delivered. Use the references to build a technology-specific record of what is demonstrated, what remains uncertain and what an actual customer needs.

## Corrections before the evidence informs a mix

| Issue | Why it changes the conclusion | How to handle it |
|---|---|---|
| One axis combines cost, operating duration, power, breeding and radiation tests | Reaching 26% of a cost target does not mean a technology is 26% commercially ready. The metrics do not share a scale of difficulty, time or probability. | Keep separate panels with native units, a named target and its rationale. Do not compute an overall readiness percentage. |
| “Every emerging technology” has one binding threshold | Most systems face several independent requirements. Passing one cannot establish economics, maintainability and manufacturing. | Show multiple unresolved requirements per technology. Use a commercial status description tied to dated evidence. |
| Tokamak triple product versus ignition | Ignition is a particular plasma condition, not a universal requirement for an economically useful externally heated reactor. A plasma result also excludes many plant loads. | State the fuel, confinement concept, gain definition and plant boundary. Test full electricity balance and practical operation. |
| Fusion tritium use of about 56 kg/year for a “1 GW plant” | The arithmetic corresponds to **1 GW of D–T fusion thermal power** operated continuously, not 1 GW net electricity. Electrical conversion and plant consumption increase the fusion power needed for a given net output. | Correct the unit boundary before sizing fuel supply. Tritium breeding requirements do not apply identically to every proposed fuel cycle. |
| Thorium conversion ratio versus breeding | A ratio near one matters to a breeding/self-sufficiency claim; it is not a prerequisite for all fission electricity. A 2 MW thermal experiment is not an electricity plant. | Separate operation, fuel conversion, breeding, materials, fuel processing and commercial cost. |
| A one-year tandem-cell result divided by a 25-year lifetime | A test duration does not measure a fraction of commercial readiness or predict all current products' lifetime. One device's degradation cannot represent the entire family. | Track full-size modules, independent certification, field cohorts, degradation conditions, warranties and manufacturing yield. Oxford PV reported first commercial shipments in September 2024; shipments alone do not prove long lifetime. [Company release](https://www.oxfordpv.com/press-releases/oxford-pv-solar-technology-patent). |
| A $20/kWh long-duration-storage threshold | This is a result tied to modeled system benefits, not a universal threshold below which all storage becomes commercial. Energy-capacity cost alone omits power equipment, efficiency and use. | Keep the study's system assumptions. Compare installed power and energy cost, duration, cycles, losses and customer service. [MIT research explanation](https://news.mit.edu/2021/powering-energy-transition-better-storage-0329). |
| Historical wind/solar reliability studies presented as universal limits | Their outcomes depend on geography, generation multiples, transmission, demand flexibility, weather and other allowed resources. | Reproduce the relevant assumptions before transferring the result. Do not infer that every possible system must use one specific dependable technology. |
| Cape Station described as commissioning in Q4 2026 | Fervo subsequently reported its first 33 MW unit commercially operating on 1 October. Planned later units remain distinct. | Update status using the [dated company announcement](https://fervoenergy.com/fervo-energy-declares-commercial-operation-at-cape-station-ahead-of-schedule-leading-the-race-for-next-generation-geothermal-energy/); retain the lack of long-term reservoir evidence. |
| The approximately 850 TWh wave calculation treated as a universal ceiling | The supplied table itself ties extraction to a Pelamis-type array. A design-specific extraction assumption cannot bound every future device or the entire ocean-energy family. | Reopen geographic, directional, array and technology assumptions in the [original study](https://doi.org/10.1016/j.renene.2012.01.101). The publisher's full text was not retrieved in this review. Do not replace this with an unsupported larger resource claim. |
| Wave or tidal target-cost ratios | A target after deployment is a conditional learning case, not evidence that the cost will be achieved. The wave and tidal examples also use different years, currencies and populations. | Separate current estimates, project bids and learning assumptions. See the current cost comparison in `ANSWER.md`. |
| Space fission, radiation tests and MOXIE on the same commercial scale | An approximate electrical equivalent is not necessarily metered output. Surviving one radiation test does not validate a whole satellite. Oxygen production is a load/product, not a generator. | Separate generation, mission loads and component qualification. Define the actual mission before comparing system mass and cost. |

The brief's instruction to test wave *only* for offshore compute is a suggested research choice inside source material. The user has chosen a broader ocean priority. Keep grid-connected wave, tidal, thermal and other routes available until the comparisons justify narrowing them.

## Improve the evidence table

Keep the original columns, but use a separate reviewed dataset with: source date; observation date; company/project; measured versus modeled versus claimed; physical unit; full system boundary; test duration; independent validation; target origin; cost year and location; unresolved issue; review status.

“Peer reviewed” describes a publication process, not whether the number is measured: several rows are theory, simulations or economic projections. The `demonstrated_value` column currently mixes observations and forecasts. Do not turn its values into an operating-capacity total. Confidence labels and citation counts in the supplied tables have not been independently assessed.

For the website, replace the universal percentage ranking with **what works now / what has been demonstrated / what still needs proof**, supported by project-specific quantities. Keep the supplied chart as a historical input, not a headline finding.
