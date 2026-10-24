# The next grid is offshore
### An evidence-backed case for an ocean-first energy mix, led by tidal stream (24 October 2026)

**The claim, stated precisely.** For coastal regions with strong tides, the cheapest way to supply clean power every hour is an ocean-first system. Floating offshore wind supplies the bulk of the energy. Tidal stream supplies weather-proof output on an astronomical schedule. Storage bridges the fortnightly neap tides. Wave energy is added to the wind farms' shared foundations and cables. In our hourly model, this system supplies **88–91% of its energy from the ocean**. Once tidal stream reaches the costs projected for about 3–4 GW of global deployment, it costs **$19/MWh less** than the best system without tidal.

We do **not** claim the ocean is the answer everywhere. Sunny tropics, inland regions, and places that can build nuclear cheaply have better options, and we show where those boundaries lie. The bounded claim is stronger, because every number below survives scrutiny.

---

## 1. Why the ocean: five advantages no land resource combines

**Scale.** Offshore wind could generate more than **420,000 TWh/yr**, about 18 times global electricity demand when the IEA published the figure. About **36,000 TWh/yr** of that lies in waters shallower than 60 m ([IEA Offshore Wind Outlook 2019](https://www.iea.org/reports/offshore-wind-outlook-2019)). World electricity use was 28,600 TWh in 2025. Ocean thermal energy (OTEC) adds an estimated **7–14 TW of net power** (61,000–123,000 TWh/yr) in tropical waters ([Rajagopalan & Nihous 2013](https://doi.org/10.1016/j.renene.2012.07.014); [high-resolution update](https://doi.org/10.1115/1.4023868)). Waves (2.11 TW gross, of which about 4.6% is extractable with current devices; [Gunn & Stock-Williams 2012](https://doi.org/10.1016/j.renene.2012.01.101)) and tides are regional resources, but they are concentrated close to major coastal grids.

![Ocean resource scale]({{artifact:8367e697-f702-44b9-ac8f-5d11af84b94e}})

**Quality.** Hywind Scotland, the first floating wind farm, averaged a **54% capacity factor over five years**, the highest of any UK wind farm, against a UK offshore average of about 40% ([offshoreWIND.biz, 2022](https://www.offshorewind.biz/2022/12/29/worlds-first-floating-offshore-wind-farm-celebrates-five-years-of-operation)). Solar at our modelled sites runs at 9% (Scotland) to 21% (Hawaii). Ocean hardware produces two to six times more energy per installed kilowatt.

**Predictability.** Tidal stream is the only renewable source whose output can be forecast decades ahead from astronomy. In our 2022–24 data, its month-to-month output varies by **5%**, compared with **23%** for wind.

**Security.** There is no fuel to import, enrich, or blockade. Ocean power is built with shipyards, ports, and offshore oil and gas skills that coastal economies already have.

**Momentum.** Offshore wind reached **92.5 GW** installed by the end of 2025, and GWEC forecasts **420 GW by 2035** ([GWEC 2026](https://www.gwec.net/reports/globaloffshorewindreport)). Floating wind is still under 0.4 GW, but has a pipeline of about 150 GW.

## 2. The lead ocean technology: tidal stream

Among the strict marine technologies (tidal, wave, OTEC, salinity gradient, ocean currents), tidal stream is the clear winner on present evidence, for three reasons.

**(a) It keeps producing when the weather fails.** Using hourly reanalysis and ocean-model data for the Pentland Firth and Orkney:
- tidal output is uncorrelated with wind (hourly r = 0.01), while wave output moves with the wind (r = 0.41);
- during multi-day wind lulls (3.4% of hours), floating wind fell to 3% of capacity, wave to 6%, and tidal held at **34%**, essentially its normal 35%;
- in the worst wind week of 2023 (1–8 June), wind ran at 1.9%, wave at 3.4%, and tidal at **49%**.

![Tidal output during wind lulls]({{artifact:e9d4483b-bfe8-43cb-8807-17a2855b0841}})

**(b) It is proven in the water.**
- **MeyGen.** The array in Scotland has generated more than 84 GWh ([EMEC](https://www.emec.org.uk/offshore-operations-at-meygens-tidal-array/)). Its longest-deployed turbine averaged 95% availability ([Offshore Energy](https://www.offshore-energy.biz/meygen-sets-record-with-worlds-first-50gwh-of-electricity-generated-by-tidal-energy/)), and one turbine has run for more than seven and a half years against a five-year design life.
- **Global output.** Cumulative tidal-stream generation reached 127 GWh in 2025 ([Ocean Energy Europe 2026](https://www.oceanenergy-europe.eu/wp-content/uploads/2026/09/Ocean-Energy-Stats-Trends-2026-1.pdf)).
- **Wave, by comparison,** still lacks multi-year farm-scale operating data.
- **OTEC's** largest operating plant is about 100 kW. The 2017–2022 Kuroshio ocean-current test (IHI's Kairyu) was also 100 kW.

**(c) It is closest to paying its way.** Our hourly least-cost model (Section 3) starts buying tidal at about **$120–140/MWh**. ORE Catapult projects **£78/MWh in 2012 money (≈$140 today) at 1 GW deployed around 2035**, and below £50 (≈$90) by 2050 ([ORE Catapult cost pathway](https://cms.ore.catapult.org.uk/wp-content/uploads/2022/10/Tidal-stream-cost-reduction-report-T3.4.1-v1.0-for-ICOE.pdf)). The most recent UK auction cleared tidal at £172/MWh in 2012 money (≈$310) ([AR6 results](https://www.hsfkramer.com/notes/energy/2024-posts/AR6-CfD-Results)). Peer-reviewed analysis supports a learning rate of about 17% ([Coles et al. 2021](https://doi.org/10.1098/rspa.2021.0469)). On that curve, starting from the ~43 MW installed since 2010, tidal reaches $125/MWh at about **1.3 GW** and $100/MWh at about **2.9 GW** of cumulative global deployment (our calculation). The UK alone has about 11.5 GW of practical tidal resource.

**Tidal's weakness, and the answer to it.** The spring–neap cycle weakens every tidal site at the same time; the 7-day average output swings between 9% and 62%. Sites around the UK and NW Europe are also largely **in phase**, so spreading turbines across sites does not make tidal firm ([Iyer et al. 2013](https://doi.org/10.1016/j.renene.2012.09.017)). The answer is storage. Tidal's value in the model is highest when long-duration storage is available, because the neap gap is a few days long and arrives on a known date. Wind droughts, by contrast, are longer and unpredictable.

## 3. The ocean-first mix: what the model chose

**Model.** An hourly least-cost capacity-expansion model (a linear program, solved with HiGHS) serving a flat **1 GW, 24/7 load**. This is the hardest case for variable renewables and the case relevant to industry and data centres. The model uses real 2023 hourly data from ERA5 (wind, solar), ERA5-Ocean (waves) and the Mercator ocean model (tides). Wind is calibrated to Hywind's measured 54% capacity factor, and tidal to a 35% design capacity factor.

**Costs** are published 2035 projections: floating wind at the US DOE target of $74/MWh; tidal at ORE Catapult's $140/MWh; wave at IRENA's $120/MWh; batteries at $120/kWh; long-duration storage at $25/kWh; no new nuclear (Scotland's position).

| Pentland Firth/Orkney hub, 2035 costs | System cost $/MWh | Ocean share of generation | Mix (share of generation) |
|---|---:|---:|---|
| No tidal (tidal at $140 is not selected) | 194.6 | 81% | floating wind 81%, solar 19%; 174 GWh long-duration storage |
| Tidal at $120 | 190.6 | 92% | wind 68%, **tidal 25%**, solar 8% |
| Tidal at $100 (~2.9 GW deployed globally) | 181.7 | 88% | wind 49%, **tidal 39%**, solar 12% |
| Tidal at $90 (2050 target) | **175.5** | **91%** | wind 43%, **tidal 48%**, solar 9% |
| Forced ≥30% marine output, tidal at $140 | 196.7 | 90% | wind 70%, tidal 16%, wave 4%, solar 10% |

**What the table shows.**
- An ocean-first system is already the cheapest clean option for a 24/7 coastal load at 2035 costs. Even without tidal, floating wind supplies 81% of the energy.
- Each step down tidal's learning curve makes the system cheaper and more ocean-heavy.
- Requiring a marine share now costs only about **1%** more, a small price for building the supply chain early.
- Wave earns a share only below about $100/MWh. Its best route is co-location on wind platforms, which one study estimates cuts wave cost from $0.347 to $0.115 per kWh ([JMSE 2022](https://doi.org/10.3390/jmse10020267); see also [Nature Communications 2024](https://www.nature.com/articles/s41467-024-50040-6)).
- **Hawaii:** solar plus storage wins ($106/MWh). OTEC enters only at about $100/MWh, where it supplies 47% of generation, while the best published projection is about $168. OTEC is a credible tropical-island option, but it is not yet the lead technology.

![Break-even: tidal enters first]({{artifact:4dbec169-98d9-45d5-894f-551c35ea934c}})


### Robustness check: three weather years, a wind drought, tidal output assumptions, nuclear as a competitor

We reran the key cases over 2022–24 (26,304 hours), in the 2010 wind-drought year, and with tidal capacity factors of 30% and 40%. The conclusion holds: tidal stream enters near its projected cost, and each step down its learning curve makes the system cheaper.

| Case (2035 costs, no new nuclear) | No tidal / tidal at $140 | Tidal at $120 | Tidal at $100 | Tidal at $90 |
|---|---|---|---|---|
| 2022–24 (3 years) | $184.1, tidal 9% | $180.2, tidal 20% | $172.4, tidal 30% | $167.5, tidal 38% |
| 2023 only | $194.6, tidal 0% | $190.6, 25% | $181.7, 39% | $175.5, 48% |
| 2010 wind-drought weather | $167.4, tidal 26% | $158.9, 37% | $148.1, 40% | n/a |
| Tidal capacity factor 30% / 40% (2022–24) | n/a | $181.3 / $178.6 (16% / 25%) | $174.7 / $170.1 (29% / 35%) | n/a |

**Nuclear as a competitor (2022–24).** New nuclear at Hinkley Point C's contract price serves the flat load alone at $166.8/MWh. With tidal at $90/MWh, the least-cost mix shifts to a hybrid ($165.0/MWh, nuclear 16% of generation). At $80/MWh nuclear falls to 3%. At $70/MWh nuclear exits entirely and the ocean mix costs $154.6/MWh. **Tidal therefore displaces new nuclear once it reaches about $70–90/MWh**, the range of ORE Catapult's 2050 target.

**Co-location and mandates (2022–24).**
- Wave at $80/MWh, added to wind platforms next to tidal at $100: wave supplies 14% and cost falls to $170.0/MWh.
- A 30% marine-output requirement raises cost by 1.0%; a 50% requirement by 3.5%.

**Hawaii (2022–24).** OTEC enters at about $90/MWh (56% of generation). Wave enters earlier, at $80/MWh (16%).

**Caveat.** In the 3-year runs the optimiser left about 0.5% of demand unserved in extreme hours, because unmet demand was priced at $5,000/MWh. Absolute 3-year costs are therefore slightly understated relative to a strict reliability standard. Comparisons between scenarios within the same weather set remain like-for-like. Weather year alone moves the absolute cost by about $30/MWh (2010: $167; 2022–24: $184; 2023: $195).

## 4. Why this beats the alternatives

| Rival | Where it wins | Why ocean-first is better for coastal regions | Honest limit |
|---|---|---|---|
| Solar + batteries | Sunny, low latitudes (it beat OTEC in our Hawaii case) | At 59°N the model never takes more than about 20% of a 24/7 load from solar (9% capacity factor). With batteries alone and no long-duration storage, the 2035 wind and solar system costs $241/MWh | In the tropics, solar is cheaper today |
| Onshore wind + storage | Cheapest today in Scotland ($264/MWh today, no nuclear) | Floating wind takes over by 2035. Onshore land, planning consent and visual impact limit how far it can grow | Onshore stays a useful complement |
| New nuclear | A flat load, if it can be built at contract prices (Hinkley Point C at $167/MWh) | Ocean projects build in modules, need no fuel and produce no waste, and Hinkley's cost has nearly doubled to £35bn (2015 prices) | Nuclear beats ocean-first for a flat load until tidal reaches about $70–90/MWh |
| Fusion | Nothing yet | Fusion has produced no net electricity. The ocean delivers to the grid today | Treat fusion as an upside option |
| Orbital solar (SpaceX AI satellites) | Computing in orbit | The SpaceX plan powers computers in orbit; it delivers no electricity to Earth. Floating wind already delivers 54% output on Earth, and beamed space solar is modelled at $0.61–1.59/kWh | Orbit is a separate market (computing in space) |

## 5. What would change our minds

- **Tidal stays above about $140/MWh after 1 GW of deployment.** Tidal then remains a niche, and floating wind carries the ocean case alone.
- **New nuclear is delivered well below Hinkley Point C's $167/MWh.** The firm-power role shifts to nuclear; tidal must then be cheaper than about $70–90/MWh to compete.
- **Long-duration storage fails to reach about $25–50/kWh.** Tidal's advantage shrinks: with batteries only, it enters at about $100/MWh.
- **Floating wind misses the $74/MWh target.** Costs rise across the board, and tidal's relative value increases.

## 6. Roadmap: how the ocean-first future happens

1. **Build tidal to 3 GW worldwide.** UK (Pentland Firth, Morlais), France (Raz Blanchard; a 250 MW tender by 2030), Canada (Bay of Fundy), Korea, Japan and Indonesia. Use ring-fenced auctions, as the UK did with £15m reserved for tidal in AR6.
2. **Co-locate.** Install wave converters and tidal arrays alongside floating-wind hubs to share cables, ports and vessels.
3. **Pair with multi-day storage sized for the neap cycle.** The neap's timing is known years ahead, so storage can be dispatched to a schedule.
4. **Tropical islands.** Run OTEC pilots at 10–50 MW with desalination co-products until costs approach $100/MWh.

## 7. Methods, data and caveats

- **Data.** Hourly ERA5 wind and solar, ERA5-Ocean waves (via Open-Meteo), and Mercator global ocean currents including tides (2022–24). Model points: Pentland Firth (58.63°N, 3.04°W), offshore 59.0°N, 4.0°W; Oʻahu.
- **Calibration.**
  - Floating-wind capacity factor is calibrated to Hywind's measured 54%. ERA5 alone gave 57.5%; reanalysis is known to over-predict NW-European wind.
  - Tidal timing comes from the 8 km ocean model. The turbine rating is calibrated to a 35% capacity factor, with 30% and 40% as sensitivities.
  - Wave converters are rated for a 30% capacity factor.
  - OTEC output scales with the square of the sea–deep-water temperature difference, against a 4.5 °C deep-water source.
- **Limits.**
  - Single-site profiles. The model has no transmission, imports or demand flexibility, all of which would lower costs for every option.
  - Nuclear is modelled as fully flexible.
  - Reported shares are generation used, including storage losses.
  - The break-even sweeps use 2023 weather; the robustness section reports 2022–24, 2010 and tidal capacity-factor sensitivity runs.
- **Currency conversion.** 2012 pounds are converted to 2025 dollars at ×1.80 (our assumption: CPI ×1.42, $1.27/£).
