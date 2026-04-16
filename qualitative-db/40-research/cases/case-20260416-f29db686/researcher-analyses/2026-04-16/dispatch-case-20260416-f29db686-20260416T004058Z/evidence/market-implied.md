---
type: evidence_map
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
research_run_id: 874a6599-6007-41da-8b60-f216653853c9
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "threshold-contract"]
---

# Summary

The evidence nets to a modest yes lean and suggests the market is roughly efficient rather than stale. The key pro-market fact is that Binance BTCUSDT is already above the threshold. The key anti-market fact is that the contract resolves on one specific minute tomorrow, so modest spot cushion does not eliminate short-horizon downside.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on Apr. 17 close above 74,000?

## Current lean

Lean yes, but not overwhelmingly.

## Prior / starting view

Start from the live market prior of about 60.5% yes.

## Evidence supporting the claim

- **Binance spot and recent 1m klines above 74,000**  
  Source: `2026-04-16-market-implied-binance-btcusdt-spot-and-klines.md`  
  Why it matters causally: same exchange and pair as settlement source; current state is already above the threshold.  
  Direct or indirect: direct.  
  Weight: high.

- **Cross-venue context around mid-74k from CoinGecko and Kraken**  
  Captured during verification pass in runtime command output.  
  Why it matters causally: reduces concern that Binance is showing an isolated aberrant print.  
  Direct or indirect: indirect/contextual.  
  Weight: medium.

- **Polymarket ladder shape is internally coherent**  
  Source: `2026-04-16-market-implied-polymarket-rules-and-ladder.md`  
  Why it matters causally: neighboring strikes were priced sensibly (72k ~91%, 74k ~61%, 76k ~23%), which suggests the crowd is pricing a plausible short-horizon BTC distribution rather than a stale outlier number.  
  Direct or indirect: indirect/contextual.  
  Weight: medium.

## Evidence against the claim

- **Only a modest cushion above threshold at the time checked**  
  Source: Binance note plus runtime price checks.  
  Why it matters causally: a roughly 1% move lower over ~39 hours is very plausible for BTC.  
  Direct or indirect: direct.  
  Weight: high.

- **Narrow resolution minute risk**  
  Source: Polymarket rules note.  
  Why it matters causally: the contract can fail even if BTC trades above 74,000 for much of the period, as long as the specific noon ET close prints below.  
  Direct or indirect: direct to contract interpretation.  
  Weight: high.

## Ambiguous or mixed evidence

- BTC near 74.8k could be read as strong support for yes, but because the contract is threshold-and-time-specific, the same fact also highlights fragility if momentum weakens.

## Conflict between inputs

There is no major source conflict. The main tension is weighting-based: whether current above-threshold spot should dominate, or whether one-minute resolution fragility should keep the estimate near market rather than meaningfully above it.

## Key assumptions

- Current above-threshold Binance spot remains informative for tomorrow's noon print.
- No major crypto or macro shock occurs before settlement.
- Binance settlement mechanics behave normally.

## Key uncertainties

- Overnight BTC volatility.
- Any Binance-specific operational or microstructure anomaly near the settlement minute.
- Whether the market has better tacit flow information than visible public spot checks reveal.

## Disconfirming signals to watch

- BTCUSDT losing 74,000 support on Binance before noon ET.
- Rapid downside move in global crypto beta overnight.
- Binance-specific price dislocation or data anomaly.

## What would increase confidence

- Continued trading above 74,000 into the morning of Apr. 17.
- A larger cushion, e.g. sustained 75.5k+ trading on Binance.
- Stable cross-exchange alignment with Binance into settlement day.

## Net update logic

Starting from the market's ~60.5% yes prior, direct Binance evidence above 74,000 supports the crowd's baseline and argues against contrarian no. But because the cushion is not large and the contract resolves on one exact minute, the update is only small. This yields a probability slightly above market, not a decisive gap.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this persona stayed close to market rather than forcing a strong contrarian take.
