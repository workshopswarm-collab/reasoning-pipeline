---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: binance live BTCUSDT spot and recent 1m closes
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 20, 2026?
driver:
date_created: 2026-04-15
source_name: Binance public API BTCUSDT ticker and recent 1m klines
source_type: exchange data / governing source proxy
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: very-high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/market-implied.md
tags: [binance, btcusdt, governing-source, live-price]
---

# Summary

Direct Binance public API checks show BTC/USDT around 74,621 at the time of research, comfortably above the 70,000 threshold. Recent one-minute closes sampled from Binance were also all well above 70,000.

## Key facts extracted

- Binance ticker price response returned BTCUSDT price = 74621.00000000.
- Recent Binance 1m candles sampled were clustered roughly between 74,650 and 74,895 highs, with closes near 74,621 to 74,855.
- The current spot level is about 6.6% above the 70,000 threshold.

## Evidence directly stated by source

- API endpoint `ticker/price` returned `{\"symbol\":\"BTCUSDT\",\"price\":\"74621.00000000\"}`.
- Recent `klines` output showed 1m closes such as 74855.01, 74842.27, 74881.31, 74772.87, 74712.01, 74770.07, 74716.52, 74671.57, 74650.01, and 74621.00.

## What is uncertain

- This is a current-state verification, not a forecast guarantee for April 20 noon ET.
- The exact resolution candle is still several days away.
- Public API spot and kline endpoints are a practical governing-source proxy but the contract text specifically references the Binance trading interface candle display at resolution.

## Why this source may matter

This is the strongest direct evidence that the market's high Yes probability is grounded in current price distance from the threshold. If BTC is already materially above 70,000 on Binance, the market only needs that condition to persist through a single specific minute close on April 20.

## Possible impact on the question

Live Binance levels strongly support the market's optimistic baseline. They make a Yes resolution the default expectation unless there is a substantial selloff before the deadline or a resolution-surface mismatch.

## Reliability notes

High for current Binance state and highly relevant because Binance is the governing venue. Still not fully dispositive because the contract resolves on one future minute-close, not on current spot alone.
