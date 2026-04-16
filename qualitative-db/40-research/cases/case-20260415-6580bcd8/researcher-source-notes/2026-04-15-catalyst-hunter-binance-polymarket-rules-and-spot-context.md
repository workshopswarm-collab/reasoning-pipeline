---
type: source_note
source_type: web
persona: catalyst-hunter
case_key: case-20260415-6580bcd8
date_created: 2026-04-15
status: active
links: []
tags: [bitcoin, btc, polymarket, binance, catalyst-hunter]
---

# Source summary

This note captures the direct settlement mechanics from the Polymarket market page and a spot-context verification pass from Binance API surfaces relevant to the April 17 noon ET resolution window.

## Source 1
- Name: Polymarket market page — Bitcoin above ___ on April 17?
- URL: https://polymarket.com/event/bitcoin-above-on-april-17
- Accessed: 2026-04-15 04:15 ET
- Type: primary market/rules surface

## Key extracted points
- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on April 17 has a final Close above 72,000.
- Otherwise it resolves No.
- Resolution source is Binance BTC/USDT with 1m Candles selected.
- The page showed the 72,000 line trading around 77 cents at access time, implying roughly 77% Yes.
- This is a narrow-resolution market: Binance only, BTC/USDT only, 1-minute candle only, noon ET only.

## Source 2
- Name: Binance spot ticker API — BTCUSDT
- URL: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
- Accessed: 2026-04-15 04:16 ET
- Type: direct exchange price surface

## Key extracted points
- BTCUSDT spot price was 73,856.76 at access time.
- This places spot roughly 1,856.76 above the 72,000 threshold about two calendar days before resolution.

## Source 3
- Name: Binance 24h ticker API — BTCUSDT
- URL: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
- Accessed: 2026-04-15 04:16 ET
- Type: direct exchange context surface

## Key extracted points
- Last price: 73,856.75
- 24h high: 76,038.00
- 24h low: 73,514.00
- 24h change: about -0.96%
- Observed 24h low remained above 72,000, which weakly supports the idea that the line is not immediately fragile, though this is only a short lookback and not sufficient on its own.

## Why this mattered
- These sources jointly establish the governing source of truth and the exact contract mechanics, while also showing current Binance spot is modestly but clearly above the line.
- The key catalyst insight is negative: absent a new macro or crypto-specific shock before Friday noon ET, the market likely needs only ordinary drift/holding behavior rather than a fresh bullish catalyst to finish above 72,000.
- The main repricing risk is not long-horizon Bitcoin thesis change; it is a short-window drawdown of about 2.5% or more into the specific settlement minute.

## Caveats
- Binance API spot/ticker surfaces are not themselves the exact final settlement candle display surface, though they are consistent with it and useful for context.
- A contract keyed to one exchange, one pair, one minute, and one timezone can be affected by intraday volatility even if broader directional view remains bullish.
