# Katie handoff

Prepared 24 October 2026.

## Your focus: build Question 1 into the final website

**Focus on Question 1: How much energy will we need, and how fast will demand grow?** Turn the existing demand research into a clear, experimental visual chapter for the final website, inspired by The Pudding.

This is the user's requested focus for your contribution. In this repository, Question 1 means the demand chapter in `question1/`. The broader project asks what the future energy mix should be on Earth and in orbit, on the Moon and on Mars. Those later questions give the demand chapter its purpose, but they are not the implementation scope of this handoff.

**Your deliverable is an understandable, working website chapter—not another outline or a PDF.** Let a reader discover how much electricity the world may need, what causes the growth, where it happens, and why the timing of use matters.

## Read these first

1. [Question 1 answer](question1/ANSWER.md): the current argument, source links, definitions and six figures.
2. [Demand inputs and results](question1/demand_results.json): structured inputs, sources and limitations.
3. [Demand analysis code](question1/demand_analysis.py): reproducible calculations and chart logic.
4. [Current project scope](RESEARCH_SCOPE.md): technology landscape now, ambitious ocean-focused proposal later.
5. [Full research handoff](CLAUDE_SCIENCE_ENERGY_CONTEXT.md): broader context and open research.

Repository: [josie-miller/energy-futures-research](https://github.com/josie-miller/energy-futures-research), private.

The [initial Figma canvas](https://www.figma.com/design/ozvOZDQZTTiUgPA6kCsGxv) contains early research boards. The newer demand figures are in this repository. The earlier cream/green graphics are usable research assets, not a mandatory final visual identity. There is no existing website implementation or chosen frontend stack to preserve.

## The main message

**A more electrified world can use energy more efficiently while needing much more electricity.** Population is only one driver. Buildings, industry, transport, equipment adoption and changes in how we supply heat and fuels matter too.

For comparing future supply systems, the research uses roughly **60,000 and 80,000 TWh of electricity generation per year in 2050**, versus **31,229 TWh in 2024**. The exact WEO endpoints are **58,081 TWh** under stated policies and **80,175 TWh** under the net-zero pathway. These imply about **2.4% and 3.7% annual generation growth over 2024–2050**.

These are conditional scenarios, not a probability range, a guaranteed forecast or the highest possible demand. They are reference cases that help us ask what must be built. The growth in generation also does not capture the whole construction task: replacing retiring plants and changing the mix come later.

## Suggested reader journey

| Reader question | What to build | Starting material |
|---|---|---|
| How much more electricity? | Start with today's generation, then reveal the two 2050 cases. A simple control can switch the assumptions and show the additional annual output. | `published_scenarios.csv`, `calculated_growth.csv`, figure 01 |
| How can electricity grow while total energy does not? | An explanation showing that fuels, useful services and electricity are different measures. Use a concrete example only if its input/output assumptions are explicit. | Figure 02 and the report's accounting discussion |
| What drives the increase? | Let readers inspect buildings, industry and transport, with the two scenarios side by side or switchable. | `sector_electricity.csv`, figure 03 |
| Where does growth happen? | A readable regional comparison; do not force a map if bars explain it better. | `regional_demand.csv`, figure 04 |
| Is this just population growth or AI? | Show the population-only comparison, then explain the additional drivers. Keep data centres within their existing sector totals. | Figure 05, JSON population and data-centre sections |
| Does the hour matter? | Let readers change a charging window while annual energy stays fixed. Show how required charging power changes. | Figure 06, JSON `ev_timing` |
| What does this mean for the next chapter? | End with the amount, location and timing of demand that a supply system must satisfy. Introduce the next question: which technologies can serve it? | Current report conclusion |

The sequence is a proposed design, not a requirement to reproduce six static charts. Use interaction only when it makes the reasoning clearer. Each scene should have one sentence that says what the reader learned.

## Data and chart files

All current demand assets live in `question1/`:

- `published_scenarios.csv`: published world scenarios.
- `calculated_growth.csv`: growth implied by the selected endpoints.
- `near_term_anchors.csv`: dated short-term observations and projections.
- `regional_demand.csv`: regional demand changes.
- `sector_electricity.csv`: sector data with explicit boundaries.
- `growth_sensitivity.csv`: illustrative growth-rate experiment.
- `figures/01_electricity_outlook.png` and `.svg`.
- `figures/02_energy_vs_electricity.png` and `.svg`.
- `figures/03_sector_demand.png` and `.svg`.
- `figures/04_regional_growth.png` and `.svg`.
- `figures/05_population.png` and `.svg`.
- `figures/06_timing.png` and `.svg`.

Use the CSV/JSON values for the website. Do not estimate numbers from image pixels. Keep data and explanatory copy easy to update separately from rendering code.

## Research boundaries to preserve

- **Energy and power differ:** TWh/year measures annual electricity; GW measures a rate of supply or use. Explain both in ordinary language.
- **Consumption and generation differ:** 2024 electricity demand is 27,290 TWh in the selected WEO table; generation is 31,229 TWh. Do not label their whole difference as grid losses or compare mismatched series as growth.
- **Electricity and total energy differ:** preserve the report's definitions of final consumption, fuels and non-energy uses. Do not add incompatible totals.
- **Scenario choices change the system:** switching to a net-zero pathway is more than increasing one growth slider.
- **AI is part of total demand:** don't count data centres twice or make them explain all global growth. Their local connection needs can be important even with a modest global share.
- **Population-only arithmetic is an illustration:** it does not isolate the causal effect of income, efficiency or electrification.
- **Annual balance does not prove reliability:** a supply system must also meet the right hours. The charging-window demonstration is not a global peak forecast.
- **Interpolated lines must be labelled:** selected future-year points do not supply observations for every intermediate year. Keep assumed growth curves distinct from published scenarios.
- **Keep citations near the claim:** preserve source date, geography, units and scenario. Follow source reuse terms, including WEO Annex A's CC BY-NC-SA 4.0, before public release.

## How this fits the ocean direction

The user wants the later proposal to take ocean energy seriously and ambitiously. Your demand chapter should establish the problem that an ocean-focused system could help solve. It should not preselect a wave device, offshore computing business, percentage mix or winning technology. The landscape and ocean proposal are separate subsequent work.

Keep the original supplied technical-gap chart out of this demand chapter. It concerns other questions and combines unlike measures; see [its review](question2/EVIDENCE_REVIEW.md) before using it elsewhere.

## Definition of done

- A working, responsive Question 1 chapter that a non-specialist can understand without reading the research report.
- A clear story, visible assumptions, and source links beside the relevant claims.
- Meaningful interactions that preserve the calculations and update labels consistently.
- Keyboard access, reduced-motion behavior, readable contrast and a useful static fallback.
- Checked calculations against the CSV/JSON inputs, plus visual checks on desktop and mobile.
- A short implementation README explaining how to run it, where the data live, and which research questions remain open.

The full website is a later deliverable. **Katie's immediate responsibility is the demand chapter—Question 1.**
