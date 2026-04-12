---
type: source_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
research_run_id: e55d5208-d3ed-470e-b218-d47cfed248d7
analysis_date: 2026-04-09
persona: catalyst-hunter
source_type: primary_and_contextual
source_name: Binance Spot API docs, Binance BTCUSDT API endpoints, Polymarket market rules
source_url:
  - https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints
  - https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
  - https://polymarket.com/event/bitcoin-above-on-april-10
tags: [binance, btcusdt, timing, resolution, catalyst]
---

# Summary
The governing source of truth is Binance BTC/USDT 1-minute candle close price for the 12:00 ET candle on 2026-04-10, as specified by Polymarket. Binance Spot API documentation confirms `GET /api/v3/klines` supports 1-minute candles and a `timeZone` parameter, while `startTime` and `endTime` remain UTC even when `timeZone` is supplied. A live adjacent-day check on 2026-04-09 showed that 12:00 ET corresponded to 16:00 UTC (EDT), and the 16:00 UTC 1-minute candle closed at 72,342.21, far above 68,000.

## Primary observations
- Polymarket rules explicitly say the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone.
- Binance docs say klines are uniquely identified by open time.
- Binance docs say `timeZone` changes interval interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- Since the relevant date is April 10 and New York is on EDT, 12:00 ET maps to 16:00 UTC.
- Live verification using Binance API for 2026-04-09 16:00 UTC returned a BTCUSDT 1-minute candle with close 72,342.21.
- Current Binance ticker snapshot during research showed BTCUSDT last price around 72,288.83.
- Binance API returned no future candles for 2026-04-10 16:00 UTC yet, which is expected and confirms the market is unresolved at research time.

## Why this matters
This case is mainly about timing mechanics, not broad BTC fundamentals. The nearest material catalyst before resolution is simply whether BTC suffers a >5.9% drawdown from roughly 72.3k to below 68k by tomorrow noon ET. With no scheduled binary event found in-scope that is likely to force such a move before deadline, the timing path still favors Yes.

## Extracted evidence
### Polymarket rule text
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."

### Binance API docs
- `GET /api/v3/klines`
- `timeZone STRING NO Default: 0 (UTC)`
- `If timeZone provided, kline intervals are interpreted in that timezone instead of UTC.`
- `Note that startTime and endTime are always interpreted in UTC, regardless of timeZone.`
- response field 5 is close price.

### Adjacent-day live verification
- 2026-04-09 15:59 UTC candle close: 72,141.99
- 2026-04-09 16:00 UTC candle close: 72,342.21
- This is the correct ET-noon alignment for April under EDT.

## Limitations
- Could not directly inspect Binance website candle UI within browser automation here; used Binance API docs and live API instead.
- No specific macro/news calendar catalyst was identified in-scope that looked likely to overwhelm the short horizon; absence of an obvious catalyst is not proof none exists.

## Reliability / source-quality note
- Primary source quality: high for resolution mechanics (Polymarket rule text + Binance API documentation).
- Market-state context quality: high for live price snapshot from Binance API.
- Independence: medium; the mechanics and live price both ultimately come from Binance-related surfaces, but that is appropriate because Binance is the governing source of truth.
- Ambiguity: medium-low after ET/UTC verification; remaining ambiguity is mainly whether Polymarket UI means the candle labeled 12:00 ET by Binance charting UI or the candle opened at 12:00 ET. Binance docs indicate candles are identified by open time, which supports using the candle that opens at 12:00 ET / 16:00 UTC.
