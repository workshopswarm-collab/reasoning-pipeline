---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-13
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 68000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket rules page and Binance spot/API check
source_type: market rules + exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-de71fc13/researcher-analyses/2026-04-13/dispatch-case-20260413-de71fc13-20260413T130158Z/personas/base-rate.md]
tags: [polymarket, binance, btc, source-note, resolution-rules]
---

# Summary

This source note combines the market's governing rules with a same-day direct Binance spot/API check. Together they establish both the resolution mechanics and the current distance from the 68,000 threshold.

## Key facts extracted

- Polymarket rules say the market resolves **Yes** if the Binance BTC/USDT **1-minute candle for 12:00 ET** on 2026-04-13 has a final **Close** price strictly **higher than 68,000**.
- The market is specifically about **Binance BTC/USDT**, not another exchange or pair.
- Price precision is determined by Binance's displayed/source precision.
- A direct Binance API spot check around analysis time returned recent BTCUSDT 1-minute candles with closes around **71,090 to 71,173**.
- Binance server time endpoint was reachable and returning live data during the check.
- CoinGecko simple price endpoint also showed BTC around **71,120 USD**, which is directionally consistent with the Binance spot level.

## Evidence directly stated by source

From Polymarket rules page:
- Resolution source is Binance.
- Relevant observation is the **12:00 ET** 1-minute candle.
- Outcome condition is **final Close > 68,000**.

From direct Binance API check:
- Recent live BTCUSDT prints were materially above 68,000 during the analysis window.

## What is uncertain

- The decisive candle had not yet occurred at analysis time, so this does not directly settle the market.
- BTC could still move below 68,000 before the noon ET close.
- I did not directly fetch the future 12:00 ET candle because it did not yet exist.

## Why this source may matter

This is the governing source-of-truth plus a direct same-day spot verification. It sharply constrains the question: for No to occur, BTC must fall by more than 3,000 from the observed ~71.1k level before the noon ET close on the same day.

## Possible impact on the question

The combined evidence strongly favors Yes on a base-rate view because same-day intraday drops of more than ~4% into a specific noon 1-minute close are possible but uncommon absent a material shock. This supports a high but not 100% probability for Yes.

## Reliability notes

- Polymarket rules page is authoritative for contract mechanics.
- Binance API is effectively direct for the exchange price series that underlies resolution, though the exact final settlement surface is the Binance trade/candle display/rule-specified series at noon ET.
- CoinGecko is secondary/contextual only and was used as a consistency check, not as the governing source.