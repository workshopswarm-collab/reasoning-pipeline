---
type: evidence_map
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
research_run_id: 283687c8-f7b4-4ad3-b5c1-16bfeefe0ee1
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: april-13-19-bitcoin-price-thresholds
question: "Will Bitcoin reach $76,000 April 13-19?"
driver:
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium
conflict_status: low_direct_conflict_high_path_uncertainty
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["threshold-touch-resolution-method"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "threshold-market", "path-risk"]
---

# Summary

BTC is already trading close enough to $76,000 that a threshold hit this week is plausible, but the market price of 75% still looks somewhat too confident given unresolved settlement-source ambiguity and the fact that the threshold had not yet been observed in the checked data.

## Question being evaluated

Will Bitcoin reach $76,000 at any point during Apr 13-19, 2026?

## Current lean

Moderate lean Yes, but with meaningful fragility and less confidence than the market implies.

## Prior / starting view

Starting view was that 75% might be reasonable if BTC were already effectively on the threshold, but a risk-manager pass should discount that if the evidence is mostly proximity rather than confirmed threshold prints on the governing source.

## Evidence supporting the claim

- Binance daily data shows Apr 13 high of 74,900 and Apr 14 high of about 75,430 in fetched data.
  - Source: source note on Binance BTCUSDT daily range.
  - Why it matters causally: only about 570 points remained to reach the threshold, which is a small move for BTC over a multi-day window.
  - Direct or indirect: direct price evidence.
  - Weight: high.

- CoinGecko snapshot around $75,375 corroborates that BTC is already in near-threshold territory.
  - Source: CoinGecko source note.
  - Why it matters causally: cross-checks that BTC is not far below 76k, reducing odds that the Binance read was anomalous.
  - Direct or indirect: direct spot-context evidence, though aggregated.
  - Weight: medium.

- The contract window still had several days remaining after the checked Apr 14 data.
  - Source: assignment context / market timeframe.
  - Why it matters causally: more time materially raises touch probability versus a same-day binary.
  - Direct or indirect: direct contract-timing relevance.
  - Weight: medium.

## Evidence against the claim

- No checked source yet confirmed an actual 76,000 print on the governing settlement source.
  - Source: combined research outcome.
  - Why it matters causally: being close is not enough for a touch market; threshold markets resolve on actual prints, not narrative momentum.
  - Direct or indirect: direct disconfirming consideration.
  - Weight: high.

- Polymarket webpage fetch did not expose usable detailed rules/source-of-truth text in the extracted content.
  - Source: direct fetch of event page.
  - Why it matters causally: settlement-source ambiguity increases risk that mainstream spot proxies imperfectly map to final resolution.
  - Direct or indirect: direct contract-interpretation risk.
  - Weight: medium.

- BTC threshold-touch markets are path dependent: a reversal of less than 1% from the checked levels would be enough to miss.
  - Source: net analysis from price proximity.
  - Why it matters causally: the thesis depends on continued upward excursion, not merely elevated level.
  - Direct or indirect: indirect scenario/risk analysis.
  - Weight: medium.

## Ambiguous or mixed evidence

- Polymarket page text suggests the rules section governs resolution, but the readable extraction did not supply the exact source list. That means the market framing supports a threshold-touch interpretation, while the missing exact rule text preserves nontrivial ambiguity.

## Conflict between inputs

There is no major factual conflict among inputs. The disagreement is mainly weighting-based: how much confidence should near-threshold spot evidence justify when the exact settlement source was not independently verified in accessible text?

## Key assumptions

- Major spot venues are directionally informative for the settlement source.
- Cross-venue price dispersion near 76k will not be large enough to change the answer materially.
- Remaining week volatility is sufficient to generate at least one touch if current momentum persists.

## Key uncertainties

- Exact governing source of truth for resolution.
- Whether BTC already printed 76k on some relevant venue after the fetched timestamp.
- Whether recent momentum persists or stalls just below threshold.

## Disconfirming signals to watch

- Explicit rule text showing a narrow settlement source that has not printed 76k.
- Sharp rejection back toward low 74k or below.
- Continued trading under 76k as the week advances, reducing remaining time value.

## What would increase confidence

- A directly verified rule citation naming the source of truth.
- A confirmed cross-venue or settlement-source print at or above 76k.
- Additional independent market data showing highs converging near or above threshold.

## Net update logic

The evidence moved the view from a generic market-anchor posture to a slightly more skeptical Yes lean. Proximity strongly supports the directional case, but unresolved resolution mechanics and the absence of a confirmed threshold print keep the probability below the market-implied 75%.

## Suggested downstream use

Use as orchestrator synthesis input and decision-maker review, especially for calibrating whether the market is pricing too much confidence into a still-unconfirmed threshold touch.