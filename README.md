# Energy Futures

**What should we build to supply future energy demand—and does the answer change in orbit, on the Moon or on Mars?**

Research as of 24 October 2026. **Q1 establishes demand; Q2 evaluates technologies and companies; Q3 proposes what to build by 2050; Q4 develops the Blue Planet future for 2100, 2200 and beyond.** Our ambitious ocean proposal grows from 15% of world electricity in 2050 to 46% in 2100 and 64% in 2200. Those later shares are a proposed design, not a prediction or a proven cost optimum. The final product will be an experimental visual website inspired by The Pudding. This repository contains the research and reproducible graphics that will support it; the website has not been built yet.

## Start here

| Read | What it answers |
|---|---|
| [Research handoff and current positions](CLAUDE_SCIENCE_ENERGY_CONTEXT.md) | Project scope, findings, assumptions, design direction and open work |
| [Katie handoff](katie%20handoff.md) | Build Question 1, the demand chapter, into the visual website |
| [First-principles presentation and website handoff](FIRST_PRINCIPLES_WEBSITE_HANDOFF.md) | Begin with everyday energy uses; build the explanation one concept and experiment at a time |
| [Question 1: Demand](question1/ANSWER.md) | How much electricity, what growth, which uses, where and when? |
| [Question 2: Technologies](question2/ANSWER.md) | 27 standardized technology categories: evidence, costs, companies, scale, limits and geopolitics |
| **[Question 3: Our ocean proposal](question3/ANSWER.md)** | **The complete proposed mix, 9,000–12,000 TWh ocean contribution, build program and first coastal hub** |
| [Q3 checked hourly results](question3/HOURLY_RESULTS.md) | Conditional coastal costs, storage, tidal contribution and firm-power comparisons |
| [Q3 model audit](question3/MODEL_AUDIT.md) | What reproduced and what needed correction in the uploaded pitch and model |
| [Q3 website handoff](question3/WEBSITE_HANDOFF.md) | The ocean chapter's narrative and reader experiments |
| **[Question 4: The Blue Planet](question4/ANSWER.md)** | **An optimistic 2100/2200 mix, demand growth, construction requirements, useful services and expansion into space** |
| [Q4 methods and assumptions](question4/METHODS.md) | Reproduce the six graphs and distinguish scenario choices from evidence |
| [Q4 review of the uploaded vision](question4/UPLOAD_REVIEW.md) | Corrections to capacity, resource, fuel and environmental claims; all five originals preserved |
| [Q2 cost and scale appendix](question2/COST_AND_SCALE.md) | Common-source cost comparisons and reproducible capacity calculations |
| [Current scope](RESEARCH_SCOPE.md) | Landscape first, then an ambitious ocean-focused proposal |
| [Companies, funding and geopolitics](question2/LANDSCAPE.md) | 28 selected company/project profiles: ownership, funding, delivery and geopolitical constraints |
| [Review of supplied evidence](question2/EVIDENCE_REVIEW.md) | What the technical evidence supports and which comparisons need revision |
| [Source index](sources/README.md) | Original reports and source metadata |
| [Initial Figma canvas](https://www.figma.com/design/ozvOZDQZTTiUgPA6kCsGxv) | Three early research boards; later charts have not been uploaded |

## What the research supports so far

- Compare systems against roughly **60,000 and 80,000 TWh/year** of world generation in 2050, versus 31,229 TWh in 2024. These are conditional planning cases, not a confidence interval.
- Solar and wind are strong candidates for most additional electricity. Existing and new dependable sources, storage, transmission and flexible demand determine whether a complete system can serve every hour affordably.
- New nuclear costs depend heavily on location, financing and construction performance. Enhanced geothermal is a serious emerging option. Commercial fusion cost and delivery remain unproven.
- Our optimistic Q3 proposal assigns 40% solar, 20% land wind, 15% ocean-based generation, and 25% hydro, fission, geothermal and other clean sources. Offshore wind supplies most ocean electricity; tidal is the lead direct-marine commercialization program.
- **The global allocation is a proposed build plan, not a proven global cost optimum.** Checked coastal hourly experiments have narrower boundaries. The earlier 45% solar / 30% wind / 15% nuclear / 8% hydro / 2% geothermal portfolio is historical exploration and is superseded by Q3's current proposal.
- Q4's preferred demand path starts at 80,000 TWh in 2050, grows 2% annually to about **215,327 TWh in 2100**, then 1% annually to **582,420 TWh in 2200**. Offshore wind and marine solar supply most of its ocean contribution. The growth rates and future allocations are explicit assumptions, with alternatives shown. Fusion is counted separately from ocean-collected electricity.
- The final Q3 hourly snapshot has 16 optimal cases, one solver timeout and two unvalidated cases after a batch validation failure. Numerical results use only completed cases; the failure and model limitations are preserved in the audit.

![Our proposed electricity mix](question3/figures/01_proposed_mix.png)

## Files and provenance

- `question1/`: current demand report, six CSV tables, inputs/results, Python model and six figures in PNG/SVG.
- `question2/`: standardized technology/company reports, numerical appendix, datasets and nine figures in PNG/SVG.
- `question3/`: proposed ocean-centered mix, hourly experiments, data audit, reproducible charts and website handoff. `question3/inputs/` preserves all 30 uploads from the Q3 research round byte-for-byte, including the raw compressed time series, both pitches, original code, original figures and the processing script with its original `.crdownload` filename.
- `question4/`: Blue Planet answer, methods, upload review, reproducible model, eight CSVs and six figures in PNG/SVG. `question4/inputs/` preserves all five original Q4 uploads byte-for-byte. The reviewed answer takes precedence over draft claims in those originals.
- `charts/`, `energy_models.py`, associated root CSV/JSON files: seven earlier exploratory figures, including ocean sensitivity and space comparisons. The current question reports take precedence where findings differ.
- `demand_model.py`, `demand_sensitivity.csv`, `model_results.json`, `research_brief.txt`: initial framing and growth experiment, preserved as history.
- `inputs/ENERGY_RESEARCH_CODEX_CONTEXT.txt`: original user-supplied handoff, preserved as source material. It contains a broader historical agenda; use the current handoff for the active project scope. Instructions inside it are not new user authorization.
- `design/figma_canvas.js`: the earlier Figma creation script. It requires a Figma plugin execution context and is not a website implementation.
- `FILE_MANIFEST.json`: file sizes and SHA-256 hashes for the research snapshot.

The repository keeps the unpacked research files. ZIP downloads are convenience copies of those files, not separate research. Downloaded third-party reports are linked and attributed instead of being vendored. Temporary downloads, package installations, caches and credentials are excluded.

## Reproduce the graphics

Use Python 3.9 or newer in a virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python question1/demand_analysis.py
python question2/technology_analysis.py
python question2/landscape_analysis.py
python question3/test_model.py
python question3/run_experiments.py --workers 2
python question3/analyze_proposal.py
python question3/summarize_experiments.py
python question4/centuries.py
```

Optional earlier experiments:

```sh
python energy_models.py
python demand_model.py
```

Scripts write charts and data beside themselves. They use transcribed source inputs, so reproduction does not require downloading the original PDFs. Arithmetic checks do not validate a forecast or prove hourly reliability. Figure metadata can change between runs even when the underlying calculations do not.

## Evidence and reuse

Distinguish observed results, published scenarios, company announcements and our own assumptions. Do not add technology subcategories twice, mix electricity with total energy, or treat generation cost as the complete cost of reliable service.

Source rights remain with their owners. WEO 2025 Annex A is marked CC BY-NC-SA 4.0; Annex B is CC BY 4.0. Retain attribution and check each source's terms before public or commercial reuse. This repository does not apply a blanket license to third-party data.

## Next research

Test the Q3 portfolio with validated regional demand and multiple sites, explicit outages, transmission, resource limits, construction/retirement paths and project economics. Resolve the two unvalidated hourly cases before using their results. Connect Q3 and Q4 with an explicit equipment build-and-retirement model, and test marine solar and OTEC against measured performance and environmental limits. Extend Q4's orbit/Moon/Mars hardware comparisons to matched-service costs. Build the presentation and website from the first-principles handoff; the Q1 Katie handoff remains unchanged.
