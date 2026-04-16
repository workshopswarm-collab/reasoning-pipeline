---
type: evidence_map
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
research_run_id: c31fcb20-d245-45e8-a49b-ef7526559069
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold", "binance", "timing-risk"]
---

# Summary

The evidence leans clearly to Yes because BTC on the governing venue is already materially above the threshold, but the market's extreme confidence still embeds assumptions about several more days of stability and about one exact future minute close.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 20, 2026 have a final close above 70,000?

## Current lean

Lean Yes, high but not extreme certainty.

## Prior / starting view

Starting from the market baseline near 89.5%, the default expectation was that Yes is favored but may be slightly overconfident because this is a narrow future close condition rather than a broad level or touch condition.

## Evidence supporting the claim

- **Current Binance BTC/USDT spot is around 74,932.85**.
  - Source: Binance public API source note.
  - Why it matters: the governing venue is already about 7% above the threshold.
  - Direct or indirect: direct contextual evidence from governing source.
  - Weight: high.

- **Recent sampled 1-minute Binance closes are all comfortably above 70,000**.
  - Source: Binance public API source note.
  - Why it matters: there is no immediate sign of hovering near the cutoff.
  - Direct or indirect: direct contextual evidence from governing source.
  - Weight: medium.

- **Polymarket rules specify a single Binance 12:00 ET close-above test and the market currently prices 70,000 around 89.5%-93%.**
  - Source: Polymarket rules/source note and assignment current_price.
  - Why it matters: confirms both exact mechanism and crowd baseline.
  - Direct or indirect: direct rules evidence plus market-confidence context.
  - Weight: medium.

## Evidence against the claim

- **This is a future close market, not a touch market.**
  - Source: Polymarket rules.
  - Why it matters causally: BTC can trade above 70,000 now and still close below it at the exact resolution minute.
  - Direct or indirect: direct rules evidence.
  - Weight: high.

- **Several days remain before settlement.**
  - Source: assignment timing and market rules.
  - Why it matters causally: crypto can move several percent in a few days, and the market only needs one badly timed drawdown to fail.
  - Direct or indirect: direct timing fact, indirect risk implication.
  - Weight: medium-high.

- **Evidence set is not highly independent.**
  - Source: run conditions.
  - Why it matters causally: primary evidence is rules + governing exchange state, but external contextual reporting fetches were weak/blocked, limiting cross-source validation.
  - Direct or indirect: workflow/source-quality risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market's own high confidence is informative but partly circular because it is the object being evaluated.
- Current large cushion strongly supports Yes, but does not fully answer exact-noon close risk.

## Conflict between inputs

No major factual conflict. The main issue is weighting: whether current cushion dominates, or whether single-minute future-close fragility deserves a larger discount.

## Key assumptions

- Current Binance price cushion is durable enough through April 20 noon ET.
- No large macro or crypto-specific shock compresses BTC below the threshold into the resolution minute.
- Binance remains the operative and accessible resolution surface without material ambiguity.

## Key uncertainties

- Short-horizon BTC volatility over the next several days.
- Whether noon ET on April 20 coincides with a transient downdraft.
- Lack of a strong independent contextual market source in this run.

## Disconfirming signals to watch

- BTC falls toward 71,000-72,000 on Binance before April 20.
- Evidence of acute risk-off macro surprise or crypto-specific dislocation.
- Confusion or change around how the noon ET candle is surfaced on Binance.

## What would increase confidence

- Continued Binance closes comfortably above 70,000 as April 20 approaches.
- Independent reporting confirming stable bullish BTC conditions rather than fragile spike behavior.
- A clean pre-resolution verification pass closer to the event time.

## Net update logic

The main upward force is simple: the governing venue is already far enough above threshold that Yes should be favored. The main downward force is mechanism-specific: this resolves on one exact future minute close, so timing fragility matters more than in touch markets. That combination supports a high Yes probability, but below the most aggressive market pricing.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review