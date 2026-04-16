---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT noon ET close-above-72000 resolution mechanics and current price context
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page and Binance API
authority_level: mixed
source_type: primary_plus_direct_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/base-rate.md
tags: [source-note, polymarket, binance, btc, resolution-mechanics]
---

# Summary

This source note captures the contract mechanics from the Polymarket market page and a direct Binance price check used to frame the base-rate view.

## Key facts extracted

- Polymarket rules state the market resolves **Yes** only if the **Binance BTC/USDT 1-minute candle for 12:00 ET on April 17** has a final **Close** price **higher than 72,000**.
- The rules explicitly say the governing source is Binance BTC/USDT with **"1m"** and **"Candles"** selected.
- The contract is **not** about other exchanges or other BTC pairs.
- On 2026-04-15, direct Binance API checks showed BTC/USDT around **74,659.41** spot and **74,631.98** 5-minute average price.
- Recent Binance daily klines from April 5-14 show BTC/USDT trading above 72,000 on multiple recent days, including highs up to roughly 76,038 and daily closes above 72,000 on several sessions.

## Evidence directly stated by source

From the Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

From Binance API direct checks:
- ticker price: 74,659.41
- 5-minute average price: 74,631.98

## What is uncertain

- The governing observation is the specific **12:00 ET one-minute close on April 17**, which has not yet occurred.
- Daily klines and current spot are contextual only; they do not settle the contract.
- Web extraction from Binance's main chart page failed, so the direct governing-source contextual check here relies on Binance API data rather than the exact chart UI referenced in the rules.

## Why this source may matter

- It identifies the precise settlement mechanism and prevents confusing this with a touch/high market or with a daily close on another exchange.
- It also shows the market is currently in-the-money relative to the threshold, which is the key outside-view input for a short-dated close-above contract.

## Possible impact on the question

- Because BTC/USDT is already materially above 72,000 with roughly two days remaining, the outside-view prior should start from "stay above a nearby threshold over a short horizon" rather than from a cold start.
- The main residual risk is short-horizon volatility causing BTC to fall below 72,000 exactly at the governing minute.

## Reliability notes

- Polymarket rules page is the best available source for contract wording and source-of-truth instructions.
- Binance API is a direct Binance data surface and is strong contextual evidence for current price state, though it is not itself the exact chart interface named in the rule text.
- Independence is limited because both contract framing and current-price context ultimately point back to Binance as the governing market surface.