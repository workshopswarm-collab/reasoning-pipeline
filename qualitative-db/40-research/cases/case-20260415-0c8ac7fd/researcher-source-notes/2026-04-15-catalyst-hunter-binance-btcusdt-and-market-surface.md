---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT current level versus Apr 17 noon ET 72k threshold and governing market rules
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 72000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API ticker and 1m klines plus Polymarket event rules
source_type: exchange_api_and_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/catalyst-hunter.md
tags: [binance, polymarket, source-note, btc, threshold-market]
---

# Summary

This source note captures the direct governing resolution mechanics from the Polymarket market surface and a direct Binance price check showing BTC/USDT trading materially above the 72,000 threshold roughly two days before settlement.

## Key facts extracted

- Polymarket rules state the market resolves **Yes** if the **Binance BTC/USDT 1-minute candle at 12:00 ET on Apr 17** has a final **Close** price **higher than 72,000**.
- The rules explicitly say this is about **Binance BTC/USDT**, not other exchanges or pairs.
- A direct Binance API ticker check returned **BTCUSDT = 74,704.00** on 2026-04-15.
- A direct Binance 1-minute kline pull for the latest 20 candles showed closes mostly in the **74,3xx-74,7xx** range, with a latest printed close of **74,704.00**.
- A CNBC market surface fetch provided contextual confirmation that the day range was approximately **73,567 to 74,800**, consistent with BTC trading comfortably above 72,000.

## Evidence directly stated by source

- Governing rule: final answer depends on the **12:00 ET one-minute candle close** on Apr 17.
- Direct Binance current-price evidence: BTC/USDT was above the threshold by about **$2,700** at the time checked.
- Direct recent-kline evidence: BTC was not just briefly above 72k; it was trading in a sustained band well above it in the sampled recent minutes.

## What is uncertain

- The market does **not** resolve on Apr 15 current price; it resolves specifically on the **Apr 17 12:00 ET close**.
- BTC can move materially over 48 hours, so current price alone does not settle the market.
- I did not directly verify macro/news catalysts from Reuters because Reuters fetch was blocked by JS/401 in this environment.

## Why this source may matter

This is the most important direct evidence set for this case because it combines the governing source-of-truth mechanics with a current direct observation from Binance, the same exchange named in the contract.

## Possible impact on the question

The direct evidence strongly supports a high Yes probability because BTC is already trading well above the threshold with about two days remaining. The main remaining risk is not source ambiguity but price retracement into the specific Apr 17 noon ET one-minute close.

## Reliability notes

- Binance API data is highly relevant because Binance is the named governing source.
- Polymarket rules page is highly relevant for contract interpretation.
- CNBC is only a contextual secondary source here, not a governing source.
- Evidence independence is moderate rather than high because the contextual price surface is still observing the same underlying BTC market regime rather than an independent causal dataset.
