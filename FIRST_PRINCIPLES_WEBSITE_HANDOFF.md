# Blue Planet — a first-principles website handoff

Prepared 24 October 2026. This is the editorial and interaction brief for the complete website. Katie's existing [Q1 handoff](katie%20handoff.md) still defines her demand-chapter focus.

**The reader's journey: understand energy → understand growing demand → understand the machines → compare complete systems → choose a 2050 mix → explore the Blue Planet of 2100 and 2200.**

The intended result is a readable, working visual essay inspired by The Pudding, with an ocean atmosphere and controlled, scroll-linked reveals. The ocean is the setting and the eventual proposal. Let the reader understand the problem before asking them to believe the proposal.

## What to learn from The Pudding

[Dicing an Onion](https://pudding.cool/2025/08/onions/) starts with a recognizable object, defines one measurable goal, changes one variable at a time, then lets the reader explore. It also explains where its simplified mathematical object differs from a real onion. Apply that structure to a lamp, a power plant and an hourly grid.

[The mowing experiment](https://pudding.cool/2026/06/mow/) invites a small attempt before naming the more complicated problem. Its guided replay makes a consequential choice understandable. Apply that approach by asking the reader to power a town through one day before showing why annual energy totals are insufficient.

Our interpretation of these examples: **show an understandable situation, invite a prediction, reveal the result, and explain what changes it.** Borrow the teaching method; make our own visual identity and writing. Apple-like pacing means generous space, clear focus and controlled transitions. It does not require locking the reader's scroll or hiding the argument behind animation.

## The visual setting

Open on a dark ocean horizon. Use a restrained blue palette, warm sunlight and bright but sparse markers for useful energy. As the story develops, reveal a coastal city, land generation, offshore equipment, cables and the deeper ocean. The setting should accumulate meaning: sunlight becomes a solar explanation; moving water becomes a tidal explanation; the horizon becomes the future timeline.

Keep important prose on stable, high-contrast surfaces. Water can move slowly behind the opening and transitions; it should settle behind charts. Motion must have a purpose, such as showing a changing quantity or following energy through a machine. Do not use decorative particles as a substitute for actual data.

## Scene 1 — What are we trying to do?

**Opening copy:** “Every light, warm room and moving train has something in common: energy changed form to make it happen.”

Start with three familiar needs: light, comfortable temperature and movement. Clicking one reveals its chain. For example: sunlight → solar panel → electricity → motor → movement and heat. The reader should see the useful service at the end before encountering a large global number.

**Principle:** energy is a quantity we track when things move, warm up, give off light or change chemically. We transfer and convert it to do useful things. We do not create energy in a power station. “Generation” means converting another form into electricity.

Show that electricity is a convenient way to transfer energy through a circuit. It is not an original fuel or a resource that appears from nowhere. Heat and electricity are also different services: a household can need heat without every unit of that heat having to be generated electrically.

## Scene 2 — How much, and how fast?

**Copy:** “Power tells you how fast. Energy tells you how much.”

Give the reader a 100-watt lamp and a time control. At ten hours, the counter reaches **1 kilowatt-hour**. Double the power or the time and the energy doubles. Keep the equation visible in ordinary units:

`100 watts × 10 hours = 1,000 watt-hours = 1 kilowatt-hour`

The picture should show power as the height of a bar and accumulated energy as its growing area. Introduce larger units only after this example. A gigawatt is a billion watts; a terawatt-hour is a billion kilowatt-hours. A 1 GW plant running at full output for a 365-day year produces **8.76 TWh**. At 45% average output it produces **3.94 TWh**. This is the foundation for every later fleet-size comparison.

Do not label a battery “1 GW” without its energy capacity. A 1 GW / 4 GWh battery can ideally deliver its rated power for four hours, before practical limits. Its charging losses belong in the energy balance.

## Scene 3 — Energy remains; usefulness changes

**Copy:** “We do not use energy up. We use its ability to do the job we want.”

Follow energy into a motor. Some becomes motion; some becomes heat. Eventually the motion also dissipates. The total energy has not vanished, but dispersed heat is harder to turn back into useful work. A heat engine needs a temperature difference; a warm ocean alone is not a free, unlimited source of electricity.

Then show the same room heated two ways. Use Q1's explicit teaching assumptions: to deliver 100 units of heat, a 90%-efficient boiler needs about 111 units of gas; a heat pump with a performance ratio of three needs about 33 units of electricity and moves about 67 units of heat from its surroundings. It is moving heat, not creating energy.

**Takeaway:** electricity demand can rise while the purchased energy needed for the same service falls. Do not turn all current fuel use into a one-for-one electricity requirement. [Q1 explanation](question1/ANSWER.md).

## Scene 4 — Why demand grows

**Copy:** “More people are doing more things. More of those things are becoming electric. Better machines push the other way.”

Build a small town rather than an abstract dashboard. Add homes and people, then cooling, transport, factories and computing. Let equipment become more efficient. Separate increased access to useful services from increased waste.

Use a simple accounting relationship: **people × services per person × energy per service**, with a further choice of how much of each service is supplied electrically. Sum different activities; do not pretend this one formula independently forecasts the world economy. Industry and trade also make national per-person comparisons more complicated.

The controls should distinguish population, activity, electrification and efficiency. Illustrate why AI is one driver among several, and keep data-centre use within the sector totals that already contain it. The result of this teaching toy must say “illustration,” not masquerade as Q1's published forecast.

## Scene 5 — How big is the task?

Reveal **31,229 TWh of world generation in 2024**, then the project's two 2050 planning cases: **60,000 and 80,000 TWh/year**. Keep the historical definition and year attached to the first number. The two future values are rounded planning cases grounded in published pathways, not probabilities or an upper and lower confidence interval.

Use an annual-output area that grows as the reader moves between cases. Then translate the increase into what must be built. A demand selector should remain available through Q3 so the supply proposal answers the same demand the reader selected.

Explain compounding with a small starting quantity. Each year's percentage applies to a larger total. Display the chosen rate and period next to the result. Through 2050, use Q1's published scenarios and distinguish their exact endpoints from the rounded 60k/80k cases. After 2050, clearly switch to our own experiments.

Data: [published scenarios](question1/published_scenarios.csv), [calculated growth](question1/calculated_growth.csv), [sector electricity](question1/sector_electricity.csv), [regional demand](question1/regional_demand.csv), [demand results](question1/demand_results.json).

## Scene 6 — Where energy comes from

**Copy:** “Many machines. A smaller number of physical ideas.”

Introduce the families before company names. Solar radiation, moving air and water, temperature differences, chemical reactions and nuclear reactions are distinct starting points. Some are connected: the Sun drives much of the wind and water cycle; winds create most ocean surface waves. Tides draw on the Earth–Moon–Sun system's gravitational interactions and the associated rotational and orbital energy. Earth's internal heat includes retained heat and radioactive decay.

Use one selectable machine at a time. Follow the same visual grammar: **source → conversion → useful output → what limits delivery**.

| Technology | Plain-language mechanism | What the reader should notice |
|---|---|---|
| Solar photovoltaic | Light transfers energy to electrons in a semiconductor; the cell produces electrical power. | Night, weather, installation area and electrical connections matter. |
| Concentrated solar | Mirrors concentrate sunlight to heat a fluid; that heat can drive a turbine or serve industry. | Heat storage can shift delivery, but the system still needs solar input. |
| Land and offshore wind | Moving air pushes blades; the rotating machine drives a generator. | Offshore is a location and engineering change, not a different energy source. |
| Hydropower | Water moving downhill drives a turbine and generator. | Reservoir storage can help with timing, but water, sites and ecosystems constrain it. |
| Wave | A device captures the motion or pressure created by waves and converts it to electricity. | Wave motion is different from tidal current; storms also challenge the equipment. |
| Tidal stream | Moving seawater turns a turbine as tides drive currents. | The schedule is predictable, but output weakens and stops at parts of the cycle. |
| Ocean thermal, OTEC | Warm surface water and cold deep water provide the temperature difference for a heat engine. | The small temperature difference, pumping, pipes and ocean response matter. |
| Salinity gradient | Membranes or related systems capture part of the energy available when waters of different salt concentrations mix. | Membrane performance, fouling, freshwater supply and local ecology limit delivery. |
| Geothermal | Wells access underground heat for direct use or electricity generation. | Heat flow, drilling, fluids and reservoir longevity vary by location and design. |
| Fission | Splitting heavy atomic nuclei releases energy; most plants use the heat to make electricity. | Fuel, construction, cooling, waste management and availability all count. |
| Fusion | Joining light nuclei releases energy; most proposed power plants must collect it and turn it into useful output. | A plasma result is not yet a durable, economical electricity plant with a complete fuel cycle. |
| Fossil fuels and bioenergy | Chemical reactions release stored energy as heat, which can drive machinery or generate electricity. | Supply chains, emissions and land use matter; bioenergy is not automatically carbon-neutral. |
| Batteries and other storage | Store energy supplied earlier, then return some of it later. | They shift energy in time and incur losses; they do not add a new primary source. |
| Hydrogen and synthetic fuels | Manufacture a chemical fuel using energy; use or ship the fuel for a later service. | Production and conversion losses must be counted. Electrolysing water does not make water an energy source. |

For an optional “trace it back” interaction, let readers follow wave energy back to wind and sunlight. Let them see why uranium or deuterium extracted from seawater still powers fission or fusion. Fuel origin and energy-conversion mechanism are separate labels.

## Scene 7 — How do we compare them fairly? (Q2)

Ask readers to power the same town, not merely choose their favourite machine. Start with annual output, then reveal a difficult night or wind lull. A source's inexpensive annual electricity may need partners to deliver at the right hour. A source available at that hour can be valuable even with a higher generation cost.

Use the same fields for every technology: useful output; operating evidence; current cost and its geography/year; timing; construction scale; limitations; companies, ownership and funding; deployment and geopolitical constraints. Keep company detail behind the basic mechanism and comparison, where an interested reader can open it.

Separate **measured operation**, **company-reported achievement**, **published model**, **target**, and **our assumption**. Missing commercial-cost evidence should read “not established.” It should never become a zero-dollar bar or an invented readiness percentage.

Data: [technology records](question2/technology_profiles.json), [company records](question2/company_profiles.json), [cost appendix](question2/COST_AND_SCALE.md), [cost ranges](question2/new_build_cost_ranges.csv), [commissioned-project averages](question2/commissioned_renewable_costs.csv). Different cost tables retain their different boundaries; do not merge them into a universal league table.

## Scene 8 — What should we build by 2050? (Q3)

**Copy:** “Build the ocean into the grid.”

Reveal the current proposal: **40% solar, 20% land wind, 15% ocean-based generation, and 25% hydro, fission, geothermal and other clean sources**. Show the two demand cases as real TWh as well as percentages. Ocean-based output is 9,000–12,000 TWh/year; offshore wind supplies most of it. Tidal, wave and OTEC remain separately visible.

Let the reader remove a technology and see the missing annual energy. Do not silently redistribute that shortfall or claim that replacing annual output preserves hourly reliability. The complete global allocation is our proposed build plan, not a proven global least-cost result.

Then zoom into the Scottish timing experiment. Show hourly tidal gaps alongside the smoother daily pattern. Allow only solved cost cases from the checked model. Display storage, discarded output and unmet demand. End with the proposed first coastal hub: 1 GW offshore wind, 20 MW initial tidal, batteries, flexible demand and a grid connection. Its roughly 4 TWh/year is not a promise of 1 GW continuous delivery.

Data: [Q3 answer](question3/ANSWER.md), [portfolio inputs](question3/proposal_inputs.json), [results](question3/proposal_results.json), [checked hourly results](question3/HOURLY_RESULTS.md). Q3's current 15% ocean proposal takes precedence over the older 10% draft.

## Scene 9 — What if the ocean becomes a much larger energy frontier? (Q4)

The horizon opens into a future timeline. Keep the frame clearly labeled **“Blue Planet: an ambitious designed scenario.”** Start from 80,000 TWh in 2050, apply 2% annual growth to 2100, then 1% to 2200: approximately **215,327 and 582,420 TWh/year**. The supplied long-run portfolios assign approximately **46.1% and 63.8% to energy collected at sea**. Use the checked Q4 files for final implementation and any documented revisions.

Expose what those shares mean: offshore wind, offshore solar, OTEC and smaller marine sources. Give fission and fusion their own categories. The future scene can show maintained offshore fleets, connected coastal industry, water production and fuel manufacture, while identifying which technologies must become much more capable and economical.

Show average output and installed capacity separately. The draft's 70,000 TWh of offshore wind in 2100 is about 8 TW of average power, but about **17.8 TW installed at 45% average output**. A large resource does not build the turbines, replace them, connect them or establish an acceptable ecological footprint.

Let readers change the growth rate before changing the technology. Slower growth, faster growth and the staged Blue Planet path should all remain visible as alternatives. Do not continue a two-century curve indefinitely and call it a forecast.

The resource panel should distinguish annual renewable flows from finite fuel stocks. OTEC's 7 TW comparison is not a universal ecological safety limit. Ocean cooling transfers heat; it does not erase heat. Land solar also redirects existing sunlight, so this advantage is not unique to ocean collectors. Read [Q4](question4/ANSWER.md) and its audit before reusing claims from the original [Blue Planet draft](question4/inputs/BLUE_PLANET_2100_2200.md).

## Scene 10 — Does the answer change elsewhere?

Close with a destination switch: Earth, orbit, Moon, Mars. The same principles still apply, but sunlight, nights, weather, materials, transport and cooling change. In space, heat must be radiated away. On the Moon, long darkness changes storage needs. Mars receives less sunlight and has dust. The ocean proposal is specific to Earth's conditions.

This is the next investigation, not proof that orbital power beats the terrestrial grid. Compare electricity used in space separately from power transmitted back to Earth. Let the final line open the question: **“The best source depends on the world you are trying to power.”**

## Keep the argument usable

Every major chart needs a one-sentence takeaway, a visible unit, a source or assumption label and an accessible data table. Put short source links beside claims; put full methods in an expandable section. Distinguish published scenarios, our calculations and proposed allocations through text as well as color.

Scroll should advance explanations while ordinary navigation still works. Provide chapter links, keyboard-operable controls, readable focus states and explicit input labels. On mobile, use a single column and put the control beside the visual it changes. In reduced-motion mode, replace travelling camera moves and continuous water motion with static compositions and direct state changes. All essential explanations must remain available without hover or animation.

Suggested chart descriptions should state the finding: “Two 2050 generation cases rise from 31,229 TWh in 2024 to roughly 60,000 and 80,000 TWh,” or “The selected Scottish wind lull has low wind and wave output while modeled tidal output continues to cycle.” Avoid alt text that merely says “energy chart.”

The first usable version should cover the whole argument in a concise sequence, with working unit, demand, technology and future controls. Further detail can live in chapter expansions. The goal is a reader who can explain the proposal and its assumptions after scrolling, not a reader who has merely watched an impressive ocean animation.
