---
type: agent_finding
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
research_run_id: 8dc6f17b-67f0-4fff-b980-b18e83006abe
analysis_date: 2026-04-09
persona: base-rate
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-threshold
question: "Will monthly inflation increase by 0.8% or more in March?"
driver: seasonality
date_created: 2026-04-09
agent: Orchestrator
stance: no
certainty: medium
importance: high
novelty: medium
time_horizon: immediate
related_entities: ["bureau-of-labor-statistics"]
related_drivers: ["macro", "seasonality"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-source-notes/2026-04-09-base-rate-bls-february-2026-cpi-release.md", "qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-source-notes/2026-04-09-base-rate-historical-cpi-base-rate-series.md", "qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/assumptions/base-rate.md"]
downstream_uses: []
tags: ["cpi", "inflation", "base-rate", "official-stat-market"]
---

# Claim

Base-rate view: **No**. A March 2026 seasonally adjusted CPI-U print of **0.8% or higher** looks materially less likely than the market implies. My estimate is **12%**, versus the market-implied **94.65%**.

**Evidence-floor compliance:** exceeded the minimum for a medium-difficulty official-stat market by checking the authoritative governing source (BLS CPI release family and release schedule), explicitly verifying the market's seasonal-adjustment mechanic, and performing an additional historical base-rate verification pass using a trusted CPI time series mirror.

**Canonical-mapping check:** clean canonical match found for `bureau-of-labor-statistics`. Clean canonical driver matches used: `macro`, `seasonality`. No material unresolved entity or driver slugs identified from this run.

## Market-implied baseline

Current price is **0.9465**, implying about **94.65%** for "yes".

## Own probability estimate

**12%** for "yes" that March 2026 CPI-U m/m seasonally adjusted prints **0.8% or higher**.

## Agreement or disagreement with market

**Strongly disagree.** The market is pricing this threshold as almost certain, but 0.8%+ monthly SA CPI is historically unusual, March-specific 0.8%+ prints are rare, and the latest official momentum is only 0.2%-0.3% in January-February 2026. To justify a 95% yes probability, I would want strong direct evidence that March 2026 looks like an outlier inflation-shock month; I did not find that in the governing source set.

## Implication for the question

From an outside-view perspective, the burden of proof is on the "yes" side because the threshold is high relative to typical monthly CPI behavior. Unless there is compelling late-breaking case-specific evidence not captured here, this market appears severely overconfident on "yes".

## Key sources used

- **Primary / authoritative / direct settlement source:** BLS CPI release family and release schedule, including the current CPI release page and BLS schedule page.
  - Source note: `qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-source-notes/2026-04-09-base-rate-bls-february-2026-cpi-release.md`
- **Secondary / contextual verification source:** FRED mirror of the seasonally adjusted CPI-U index (`CPIAUCSL`) used to calculate historical monthly frequencies and March-specific base rates.
  - Source note: `qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-source-notes/2026-04-09-base-rate-historical-cpi-base-rate-series.md`
- **Direct contract-mechanics verification:** BLS technical note stating short-term trend analysis should use seasonally adjusted data and noting annual February seasonal-factor updates and 5-year revisions.

## Supporting evidence

- The governing BLS release shows **February 2026 CPI-U at 0.3% SA m/m**, after **0.2% in January**. That is far below the 0.8% threshold.
- Using the historical seasonally adjusted CPI-U series, **0.8%+ monthly prints occurred about 8.3% of months** since 1948 (79 of 948).
- For **March specifically**, 0.8%+ occurred **7 of 79 times** since 1948, about **8.9%**.
- Since **2000**, March reached 0.8%+ only **once in 26 years**: **March 2022** at 1.1%, during the exceptional 2021-2022 inflation surge regime.
- Recent 0.8%+ months cluster in the obvious outlier regime of **2021-2022**, not in the current official 2026 run-rate.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that **monthly CPI can jump abruptly when a broad-based inflation shock or seasonal-adjustment quirk hits**, and **March 2022 did reach 1.1%**, proving the threshold is not impossible and that March is not structurally capped below 0.8%. If March 2026 had a fresh energy or services surge that survived seasonal adjustment, my estimate would be too low.

## Resolution or source-of-truth interpretation

The governing source of truth is the **BLS Consumer Price Index report for March 2026**, scheduled for **April 10, 2026 at 8:30 a.m. ET**. The market resolves on the **one-month percent change in seasonally adjusted CPI-U**, reported by BLS to **one decimal place**.

**Case-specific BLS report check:** completed. I verified the current BLS CPI release family, the BLS CPI schedule page, and the March 2026 scheduled release timing.

**Case-specific seasonal-adjustment check:** completed. BLS technical notes explicitly say short-term trend analysis usually should use **seasonally adjusted** data and that seasonal factors are updated each February with revisions to the prior five years. That means raw spring price moves should not be naively mapped onto the contract; the adjusted series is what counts.

Source-of-truth ambiguity looks **low**. The only meaningful nuance is that historical adjusted series can be revised, but the market itself clearly points to the March 2026 official BLS release as the settlement event.

## Key assumptions

- March 2026 inflation behavior is closer to the recent moderate regime than to the 2021-2022 surge regime.
- No major late shock pushes multiple CPI components high enough to produce a 0.8%+ adjusted all-items print.
- Historical frequency remains a useful prior for a threshold event this extreme.

## Why this is decision-relevant

The price is near certainty on "yes." If the outside-view prior is anywhere near correct, this is a major market/prior mismatch rather than a small calibration gap.

## What would falsify this interpretation / change your mind

- Credible late pre-release nowcasts or previews clustering near **0.8%+** for seasonally adjusted headline CPI.
- Evidence of a broad March price surge across energy, shelter, and core services strong enough to overwhelm the prior.
- Any authoritative or near-authoritative indication that seasonal-adjustment effects for March 2026 are unusually supportive of a very large adjusted print.

## Source-quality assessment

- **Primary source used:** BLS CPI release family and BLS schedule page.
- **Most important secondary/contextual source used:** FRED historical CPIAUCSL series for base-rate calculation.
- **Evidence independence:** **medium**. The contextual series mirrors the same official CPI system, so it is not fully independent, but it serves a distinct purpose: historical-frequency verification rather than settlement.
- **Source-of-truth ambiguity:** **low**. Contract wording and BLS release schedule make the governing source clear.

## Verification impact

- **Additional verification pass performed:** yes.
- I first verified the direct BLS release mechanics and latest official print, then performed a second pass using historical series calculations to test whether a 0.8%+ March print is normal or exceptional.
- **Material effect on view:** yes, in the sense that the verification reinforced and hardened the low-probability view. It did not flip the direction, but it made me more confident that a near-95% market price is not justified by the outside view.

## Reusable lesson signals

- Possible durable lesson: extreme-probability official-stat markets can still be wildly miscalibrated when the threshold is rare and participants anchor on narrative rather than historical frequency.
- Possible missing or underbuilt driver: none from this run.
- Possible source-quality lesson: for CPI threshold markets, explicitly checking the BLS seasonal-adjustment guidance is worth doing because raw-price intuition can mislead.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**
- Review later for driver candidate: **no**
- Review later for canon or linkage issue: **no**
- One-sentence reason: this case suggests a reusable process lesson about forcing a historical-frequency and seasonal-adjustment check on high-confidence macro data markets.

## Recommended follow-up

Closest thing to a view-changing next source would be a reputable late CPI preview / nowcast published just before the BLS release. Without that, the base-rate case is already sufficient and additional generic searching is unlikely to move the estimate by 5 percentage points.
