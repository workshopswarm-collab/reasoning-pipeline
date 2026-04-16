---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity:
topic: case-20260415-3f432366 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market description / contract wording
source_type: contract_specification
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/base-rate.md]
tags: [polymarket, contract, resolution, source-note]
---

# Summary

The contract resolves on one very specific observation: the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-17. This is narrower than a daily-close or "trades above 72k at some point" market.

## Key facts extracted

- "Yes" resolves if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final close strictly higher than 72,000.
- Otherwise the market resolves "No."
- The stated resolution source is Binance, specifically the BTC/USDT close prices available on the Binance trading interface with `1m` and `Candles` selected.
- The contract is explicitly about Binance BTC/USDT, not other exchanges and not other pairs.
- Price precision follows the number of decimal places in the source.

## Evidence directly stated by source

- The exact time window that matters.
- The exact exchange and pair that matter.
- The exact field that matters (`Close`, not high/low/last print elsewhere).
- The strict inequality condition (`higher than` 72,000).

## What is uncertain

- Whether Binance UI and API ever diverge transiently in displayed final candle values due to rendering, rounding, or revision mechanics.
- Whether there are any unusual exchange incidents near the resolution minute; the contract text does not elaborate contingency handling beyond naming Binance.

## Why this source may matter

This source governs settlement mechanics. It sharply limits what evidence is decision-relevant and prevents over-reliance on daily closes, other exchanges, or broader Bitcoin narratives.

## Possible impact on the question

Because the contract keys off a single minute close, short-horizon volatility matters more than it would in a day-close market. Even if the broader trend is bullish, the "No" path can still happen via a brief downtick at the exact noon ET minute.

## Reliability notes

This is the authoritative contract description for interpretation, but it is not itself the settlement datapoint. Reliability for wording is high; reliability for eventual numeric answer depends on Binance's own published candle at the specified minute.