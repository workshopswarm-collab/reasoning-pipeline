---
type: evidence_map
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
research_run_id: 8357c265-76f4-4779-9bdb-36852971e867
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?"
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
downstream_uses: []
tags: ["evidence-map", "threshold-market", "timing-risk"]
---

# Summary

Evidence nets to a high-probability Yes, but not a trivial one. The market is mostly pricing current distance-from-threshold correctly, while likely underpricing the exact-minute path risk only modestly.

## Question being evaluated

Whether Binance BTC/USDT will have a final 12:00 ET one-minute candle close above 70000 on 2026-04-20.

## Current lean

Lean Yes.

## Prior / starting view

Starting from the market price of 0.88, the baseline was already strongly Yes but required stress-testing because extreme probabilities on narrow timestamp contracts can hide path risk.

## Evidence supporting the claim

- Live Binance ticker price around 74632-74643 during the run. Direct, high weight. This leaves roughly a 4630 cushion versus the threshold.
- Binance 24hr low around 73795. Direct/contextual, medium-high weight. Even the recent low stayed well above 70000.
- Polymarket contract mechanics are straightforward: only one exchange, one pair, one candle close, one threshold. Direct, medium weight. Simplicity reduces interpretive ambiguity.
- Binance docs define the kline close field and timezone handling. Direct, medium weight. This improves confidence that the noon ET candle can be mapped cleanly.

## Evidence against the claim

- The contract is path-sensitive to one exact minute. Direct structural risk, high weight. BTC can trade comfortably above 70000 for days and still lose on a sharp timestamp-specific downtick.
- Five calendar days remain. Contextual, medium weight. That is enough time for a 6%+ move in BTC, especially with crypto weekend volatility.
- Resolution depends on Binance specifically, not a broader BTC benchmark. Direct structural risk, medium weight. Exchange-specific prints or microstructure distortions could matter at the exact minute.

## Ambiguous or mixed evidence

- Binance timezone parameter improves interpretability, but Polymarket cites the Binance UI candle rather than the API endpoint directly. Likely same underlying data, but not completely formalized in the rules text.
- Nearby strike prices on Polymarket suggest the market sees a smooth distribution, but they do not independently verify the settlement minute itself.

## Conflict between inputs

No major factual conflict across checked inputs. The main disagreement is weighting-based: how much to penalize an otherwise favorable spot level for exact-minute timing risk.

## Key assumptions

- Current cushion above 70000 is large enough to survive ordinary volatility.
- Binance UI and API candle interpretation align for the relevant ET noon minute.
- No exchange-specific incident or sudden dislocation materially affects the settlement print.

## Key uncertainties

- Weekend and macro-driven BTC volatility over the remaining horizon.
- Whether the market is slightly overconfident because 88-89% compresses several nonzero tail risks.

## Disconfirming signals to watch

- BTC trading down toward 71000 before Apr 20.
- Any Binance outage, wick event, or microstructure anomaly near noon ET.
- Adjacent threshold markets repricing sharply lower.

## What would increase confidence

- BTC holding above 73000 into Apr 19-20.
- Continued calm realized volatility.
- Cleaner confirmation from Binance UI or an additional exchange-independent data monitor that the noon ET candle mapping is unambiguous.

## Net update logic

The evidence keeps the probability high because current spot is materially above threshold and recent realized range is also above it. The main downward adjustment versus a naive momentum read comes from exact-minute settlement risk and exchange-specific operational dependence.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input. The key message is not "BTC bullish" but "Yes favored, with nontrivial narrow-window tail risk that keeps confidence below the market's upper edge."
