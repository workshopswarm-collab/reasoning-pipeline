---
type: evidence_map
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: 650a5f85-0f84-4bcf-9184-5b7a92c66a57
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
driver: operational-risk
date_created: 2026-04-16
agent: variant-view
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "threshold-market", "binance", "touch-market"]
---

# Summary

The evidence nets to a Yes lean, but the strongest credible variant view is that the market is somewhat overpricing a touch that has come close without completing.

## Question being evaluated

Will Binance SOL/USDT print any 1-minute candle high of 90.00 or greater between 2026-04-13 00:00 ET and 2026-04-19 23:59 ET?

## Current lean

Lean **Yes**, but below market confidence.

## Prior / starting view

Starting baseline was the market-implied **74% Yes**, which suggested the crowd believed a touch was more likely than not but not close to certain.

## Evidence supporting the claim

- **Binance 24h ticker last price 88.91, high 89.15**
  - Direct source: Binance API.
  - Why it matters causally: the named settlement venue is already trading within about 1.2% of the strike.
  - Direct or indirect: **direct**.
  - Weight: **high**.

- **Full Binance 1-minute window check found max high 89.15**
  - Direct source: Binance kline API over the contract window.
  - Why it matters causally: the market has already nearly touched the target; only a modest additional move is needed.
  - Direct or indirect: **direct**.
  - Weight: **high**.

- **CoinGecko contextual range high about 88.87**
  - Secondary source: CoinGecko range API.
  - Why it matters causally: confirms broader spot context is also trading near the threshold rather than Binance being a one-off outlier.
  - Direct or indirect: **contextual**.
  - Weight: **medium**.

## Evidence against the claim

- **No confirmed Binance >=90 print yet in the relevant window**
  - Direct source: same Binance kline pull.
  - Why it matters causally: the event remains incomplete despite a near-touch.
  - Direct or indirect: **direct**.
  - Weight: **high**.

- **Repeated rejection just below 90 during the focused verification pass**
  - Direct source: Binance minute candles around the peak period.
  - Why it matters causally: round-number resistance or exhausted momentum can matter in short-dated touch markets.
  - Direct or indirect: **direct**.
  - Weight: **medium**.

- **Short remaining window means near-miss can still fail**
  - Logic from contract timing and crypto volatility.
  - Why it matters causally: less time remains for another attempt; close is not resolution.
  - Direct or indirect: **interpretive**.
  - Weight: **medium**.

## Ambiguous or mixed evidence

- Broader crypto strength helps the Yes case, but a weekend or macro-led risk-off move could erase the remaining gap quickly.
- Being near the strike cuts both ways: it implies plausibility of touch and also confirms that the market may already be pricing in much of the good news.

## Conflict between inputs

There is little factual conflict. The main disagreement is **weighting-based**:
- market-style intuition may overweight “only ~1% away”
- the variant view weights “still not done, and exact thresholds fail more often than spot intuition suggests”

Evidence that would resolve this would be fresh Binance prints nearer settlement, especially any clean break above 89.5 or a retreat back toward the mid-80s.

## Key assumptions

- Near-touch status should not be treated as equivalent to completion.
- No unseen contract nuance makes API highs irrelevant versus chart highs.
- Current momentum is real but not guaranteed to continue.

## Key uncertainties

- Whether Solana gets another upward impulse before the window closes.
- Whether Binance chart/display conventions at the exact threshold could matter if a 90-area wick occurs.
- How much event-time remains after this run relative to likely volatility catalysts.

## Disconfirming signals to watch

- Binance SOL/USDT breaks above 89.5 and holds.
- Multiple fresh high attempts into 90 with expanding volume.
- Broader crypto complex moves risk-on again before the window ends.

## What would increase confidence

- A fresh direct Binance check closer to the end of the market window.
- Confirmation from Binance chart UI if a 90-area wick appears.
- Evidence on whether comparable near-touch crypto markets tend to complete over similarly short remaining windows.

## Net update logic

The evidence moved the starting view slightly **down** from the 74% market baseline because the strongest direct evidence says the event is **close but not complete**, and the most important neglected point is that this market resolves on an exact venue-specific touch, not on generalized bullishness.

## Suggested downstream use

Use as **orchestrator synthesis input** and **decision-maker review** for how much confidence discount to apply when a crypto touch market is near the strike but unresolved.