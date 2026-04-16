---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and Binance SOLUSDT API check
source_type: market page plus exchange API
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, spot-price]
---

# Summary

This note captures the contract mechanics from the live Polymarket market page and a direct Binance API spot/daily-price check relevant to whether the current 92% market price for SOL above 80 on April 19 is plausible.

## Key facts extracted

- Polymarket shows the `80` line at roughly 92% Yes on the April 19 ladder as of the fetch on 2026-04-16.
- The market resolves using the Binance SOL/USDT 1-minute candle for `12:00` in ET timezone on April 19, specifically the final `Close` value.
- The contract is not based on other exchanges or other trading pairs.
- Binance public API spot check returned `SOLUSDT = 85.24000000` on 2026-04-16.
- Binance 1-day klines for the last 7 sessions show recent closes of roughly 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and 85.24, indicating SOL has recently spent sustained time above 80 rather than barely touching it.

## Evidence directly stated by source

From Polymarket market page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the SOL/USDT 'Close' prices currently available at https://www.binance.com/en/trade/SOL_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance SOL/USDT, not according to other exchanges or trading pairs."

From Binance API:
- Current spot returned by `/api/v3/ticker/price?symbol=SOLUSDT` was `85.24000000`.
- Recent daily kline closes from `/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=7` are all above 80 in the returned sample.

## What is uncertain

- The Binance website UI page itself did not extract cleanly through web fetch, so the direct exchange verification here relies on Binance public API rather than the exact website candle widget named in the contract.
- A noon ET 1-minute close on April 19 can still differ materially from current spot if crypto sells off sharply before resolution.
- Public API spot and daily klines are helpful context, but they do not directly settle the exact noon ET 1-minute close yet because the event has not occurred.

## Why this source may matter

This is the governing resolution mechanics source plus a direct exchange-data check. Together they tell us both what must happen for Yes and whether the current market price is directionally consistent with the current price regime.

## Possible impact on the question

The evidence supports the idea that the market's high Yes probability is grounded in current observable price levels: SOL is already several dollars above the strike with only a short time window left. That said, the precise settlement condition is narrow enough that short-horizon volatility remains the main reason not to treat 92% as certainty.

## Reliability notes

- Polymarket is authoritative for contract wording but not for future price realization.
- Binance public API is a strong direct exchange-data source and highly relevant, though the contract explicitly points to the Binance trading interface candle display as the settlement surface.
- Evidence independence is only moderate because both key facts ultimately hinge on one market contract and one exchange source, but for a date-specific crypto-price market that pairing is the most relevant available evidence.