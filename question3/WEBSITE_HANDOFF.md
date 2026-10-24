# Q3 visual story: build an ocean-powered coast

## Editorial position

Our optimistic proposal is 40% solar, 20% land wind, 15% ocean-based generation and 25% hydro, fission, geothermal and other clean sources in 2050. Ocean means 9,000–12,000 TWh/year across Q1's two generation cases. Offshore wind supplies most of it; tidal is the lead direct-marine commercialization program.

The story should help a reader understand **what to build, how much, and why combining resources can be valuable**. The annual global allocation is a proposed plan. The coastal hourly model is a conditional experiment. Do not present either as a proved global least-cost optimum.

## Suggested sequence

1. **Reveal demand.** Carry Q1's 60,000/80,000 TWh selector into Q3. Show a complete proposed mix and the remaining supply whenever a technology is removed.
2. **Move to the coast.** Split ocean electricity into offshore wind, tidal, wave and ocean thermal. Make the size difference visible. Offshore wind must retain its label; do not imply water-motion devices produce its output.
3. **Show a difficult week.** Animate the supplied Scotland wind-lull window. Keep hourly tidal output visible alongside its smooth daily average, so the viewer sees the gaps. Label the profiles modeled and the week selected.
4. **Price reliability.** Let the reader change tidal price and see the checked system cost, storage requirement, generation mix and unmet demand. Use only saved solved cases or a clearly labeled interpolation. Never invent fresh solver output in the browser.
5. **Let alternatives compete.** Add the firm-power and storage sensitivities. A cheaper complementary source should visibly reduce system cost, even if it lowers the ocean share.
6. **Turn energy into construction.** Show 2.2–2.9 TW offshore wind, net additions of 85–114 GW/year, ports/cables/vessels and the staged tidal learning program. Use separate switches for demand and technological success.
7. **Choose a first hub.** Present the proposed 1 GW wind + 20 MW initial tidal development brief, its approximate annual energy and the customer service that remains to be contracted. Show that 1 GW installed is not 1 GW constant supply.

## Data and graphics

Use `proposal_results.json`, `proposal_inputs.json`, `experiment_jobs.json`, and the individual files in `experiments/`. PNG and editable SVG charts are in `figures/`. Original user charts and both pitch drafts remain in `inputs/` as historical research, not final validated graphics.

Global controls can recompute `TWh = GW × 8.76 × mean output` in the browser. They cannot establish reliability. Put annual generation, power capacity, storage energy, discarded potential output and end-use demand in their correct units. Show unknown values explicitly.

## Claims to retain

- The ocean can become a major part of an electrified world.
- Tidal output can arrive when wind output is low, which can make it worth more than a simple plant-cost comparison suggests.
- Building the first several gigawatts of tidal is a learning and industrial-policy decision with measurable performance gates.
- The complete mix includes solar, inland generation, grids and storage. Successful clean firm power improves the proposal.

## Claims to avoid

- “This is the globally optimal mix.” No global hourly optimization has established that.
- “Ocean power covers 90% of worldwide demand.” The supplied Scottish percentages do not generalize worldwide.
- “Tides are constant” or “wave is weather-proof.”
- “A 30% mandate costs only 1% more,” using the original pre-curtailment constraint.
- “Every modeled hour was served,” for original results that contain non-delivery.
- “3 GW guarantees $100/MWh tidal.” Cost learning is uncertain and the original source was misread.
- “The 2010 case used actual 2010 tides.” It pairs 2010 weather with 2023 tidal timing.

The final product should be an experimental narrative website inspired by The Pudding, with concise explanatory copy, readable charts and meaningful reader choices. This file is a content/design handoff; this research round does not implement the complete website.
