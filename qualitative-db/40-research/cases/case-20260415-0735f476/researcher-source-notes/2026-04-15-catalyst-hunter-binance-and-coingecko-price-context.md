---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: threshold-close-markets
entity: btc
topic: Bitcoin spot level relative to 70000 threshold on April 15
question: How far above the contract threshold is BTC currently trading, and what near-term price context matters?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot APIs and CoinGecko price context
source_type: exchange API plus market-data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: mildly supportive
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/catalyst-hunter.md
tags: [binance, coingecko, spot-price, threshold-distance, btc]
---

# Summary
Live Binance data and CoinGecko context both showed BTC materially above the 70,000 threshold on April 15. Binance spot prints were around 74.6k, while recent Binance daily candles showed closes above 70k for multiple consecutive days and highs as high as 76,038 on April 14. CoinGecko showed roughly 74,664 with a modest positive 24h change, supporting the view that cross-venue context broadly matches Binance rather than showing a major exchange-specific dislocation.

## Key facts extracted
- Binance ticker price fetched: 74,613.01 BTC/USDT.
- Binance recent 1-minute closes near fetch time were around 74,627 to 74,677.
- Binance 24h high/low fetched: 75,281 high and 73,514 low.
- Binance 5-minute average price fetched: 74,629.54.
- CoinGecko spot context fetched: 74,664 USD with about +0.46% 24h change.
- Binance recent daily candles (last 10) show closes above 70,000 on multiple consecutive days, including 74,417.99, 74,131.55, and 74,576.13.

## Evidence directly stated by source
- Binance API ticker: BTCUSDT price 74613.01000000.
- Binance recent daily klines show an April 13 high of 76,038 and close of 74,131.55, and an April 14 close of 74,576.13.
- CoinGecko simple price endpoint reported bitcoin.usd = 74664 and usd_24h_change ≈ 0.456%.

## What is uncertain
- This is only a current snapshot, not proof of where BTC will be at noon ET on April 20.
- CoinGecko is contextual rather than governing for settlement.
- Near-term macro/news catalysts were not directly captured from a high-quality newsroom source in this note.

## Why this source may matter
The core timing question is whether there is enough cushion above 70k to survive ordinary volatility into the noon ET print. Current spot materially above the line reduces immediate threshold risk and suggests the market's high Yes probability is not crazy.

## Possible impact on the question
If BTC stays in the current 73.5k-75.3k neighborhood, the noon ET April 20 close-above condition likely resolves Yes. The main remaining risk is a several-thousand-dollar drawdown before that timestamp, not minor noise.

## Reliability notes
Binance is highly reliable and directly relevant because it is also the governing settlement venue. CoinGecko is useful as an independent contextual cross-check, but it is not the source of truth for settlement.