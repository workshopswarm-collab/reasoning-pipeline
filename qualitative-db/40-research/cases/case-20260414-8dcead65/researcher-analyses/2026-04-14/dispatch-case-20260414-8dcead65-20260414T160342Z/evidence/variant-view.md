---
type: evidence_map
case_key: case-20260414-8dcead65
dispatch_id: dispatch-case-20260414-8dcead65-20260414T160342Z
research_run_id: ec54cc43-d0f9-4685-b48d-3db8e30bf797
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-15
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-8dcead65/researcher-analyses/2026-04-14/dispatch-case-20260414-8dcead65-20260414T160342Z/personas/variant-view.md"]
tags: ["evidence-map", "btc", "polymarket", "binance"]
---

# Summary

The evidence nets to a strong Yes lean, but the main variant-view contribution is that the market's 97.9% confidence likely compresses the remaining short-horizon crash / venue-specific tail risk too aggressively.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle that closes at 12:00 ET on 2026-04-15 have a final close above 70,000?

## Current lean

Yes, with very high probability, but not quite as high as the market implies.

## Prior / starting view

Starting from the market price of 0.979, the baseline assumption was that Yes is overwhelmingly likely unless contract mechanics or current venue price checks reveal hidden fragility.

## Evidence supporting the claim

- **Current Binance price is far above threshold**  
  - Source: Binance `ticker/price`, `avgPrice`, and recent `klines`; source note `2026-04-14-variant-view-binance-api-and-polymarket-rules.md`  
  - Why it matters: a No outcome requires a substantial move down before tomorrow noon ET.  
  - Direct vs indirect: direct.  
  - Weight: very high.

- **Recent 1-minute candle sample never touched 70,000**  
  - Source: Binance `klines?limit=1000` sample summarized in source note.  
  - Why it matters: direct recent evidence that the threshold is well below currently observed minute closes.  
  - Direct vs indirect: direct.  
  - Weight: high.

- **Polymarket contract wording is straightforward once timezone is checked**  
  - Source: Polymarket rules page; source note.  
  - Why it matters: reduces interpretive ambiguity; the market is really about one exact Binance minute close and a strict greater-than threshold.  
  - Direct vs indirect: direct contract evidence.  
  - Weight: high.

## Evidence against the claim

- **Crypto can gap sharply on short horizons**  
  - Source: contextual market-structure logic rather than a separate quantified volatility study in this run.  
  - Why it matters: extreme Yes pricing can still be vulnerable to underweighted tail risk.  
  - Direct vs indirect: indirect/contextual.  
  - Weight: medium.

- **Venue-specific resolution dependence**  
  - Source: contract wording and Binance-specific settlement mechanics.  
  - Why it matters: even if broad BTC spot remains healthy, a Binance-specific print or operational irregularity could matter at the exact minute.  
  - Direct vs indirect: direct contract logic, indirect outcome mechanism.  
  - Weight: low-to-medium.

## Ambiguous or mixed evidence

- The lack of a successful independent contextual-news pull in this run means there is less outside-of-Binance triangulation than ideal, though the governing source of truth is Binance itself.
- Because the market resolves on a single minute tomorrow, current price cushion is highly informative but not dispositive.

## Conflict between inputs

There is no strong source conflict. The disagreement is primarily weighting-based: how much residual crash / exact-minute venue risk should be left after observing BTC about 7-8% above the threshold with less than one day to go?

## Key assumptions

- The relevant residual risk is tail-event risk rather than ordinary drift.
- Binance API and chart/UI should align closely enough for current-state verification.
- No hidden contract exception overrides the plain-language rules excerpt.

## Key uncertainties

- Whether any catalyst emerges before 2026-04-15 12:00 ET.
- Whether Binance experiences any price-feed or operational anomalies near resolution.
- Whether short-horizon BTC downside volatility is being underappreciated by the market.

## Disconfirming signals to watch

- BTC/USDT falling rapidly toward 72,000 or below before the resolution window.
- Binance-specific operational instability.
- Any rule clarification indicating a different source surface than expected.

## What would increase confidence

- Another verification pass tomorrow morning showing BTC still comfortably above 70,000.
- Confirmation that Binance chart/UI close and API close conventions align cleanly for the noon ET candle.

## Net update logic

The evidence keeps the answer strongly on Yes, but the main update versus the market is to shave a few points off extreme confidence because this is a one-minute, one-venue, date-specific contract. The market's basic story is right; the possible mistake is overconfidence, not direction.

## Suggested downstream use

Use as an orchestrator synthesis input and forecast-weighting check; the key takeaway is "agree on direction, mildly disagree on confidence."