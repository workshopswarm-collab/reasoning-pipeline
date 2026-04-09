---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: case-20260409-21554cf3 | risk-manager
question: Will the price of Ethereum be above $2,100 on April 9?
driver: operational-risk
date_created: 2026-04-09T03:36:00-04:00
source_name: Binance ETHUSDT 1m klines API and spot ticker
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=10
source_date: 2026-04-09
credibility: high
recency: high
stance: supports yes
certainty: medium
importance: high
novelty: low
agent: risk-manager
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, ethusdt, resolution-source, exact-candle, timezone-check]
---

# Summary

Binance is the governing source of truth for this market. Direct checks of Binance's public ETHUSDT 1-minute kline API and spot ticker show ETH trading materially above $2,100 during the hours leading into noon ET, reducing but not eliminating the chance of a noon close below the threshold.

## Key facts extracted

- The market rules explicitly say resolution is based on the Binance ETH/USDT 1-minute candle for 12:00 ET on April 9, using the final close price.
- Binance's public kline API returns 1-minute candles with millisecond UTC timestamps and close prices.
- A direct API pull of the most recent 10 candles at approximately 2026-04-09 03:35 ET showed ETH/USDT closes between about 2181.00 and 2183.67.
- A direct spot ticker pull at approximately 2026-04-09T07:35:51Z showed ETHUSDT at 2183.31.
- Timezone mapping check: a kline open timestamp of 2026-04-09T07:35:00Z corresponds to 2026-04-09T03:35:00-04:00, confirming that noon ET on this date maps to 16:00 UTC because New York is on EDT.
- A direct query for the 2026-04-09 16:00 UTC candle currently returns zero rows because that candle has not happened yet; this confirms the exact candle still lies ahead and cannot yet be directly settled.

## Evidence directly stated by source

- Binance API values directly state recent ETHUSDT trade prices and 1-minute close values.
- Binance timestamps directly support the ET-to-UTC alignment needed for the contract.

## What is uncertain

- The contract resolves on a single future 1-minute close, not the current spot price.
- Intraday volatility between now and 12:00 ET could still move ETH below $2,100 at the governing minute.
- The Polymarket rules refer users to the Binance trading interface rather than the API specifically, so there is a modest implementation ambiguity even though both should reflect the same underlying exchange data.

## Why this source may matter

This is the core authoritative source class for the case. It directly addresses the required single-source authority, exact-candle verification framework, and timezone alignment check.

## Possible impact on the question

Because the authoritative venue currently shows ETH roughly $80+ above the threshold several hours before the governing candle, the direct evidence leans Yes. The remaining risk is path and timing risk into one exact minute rather than source ambiguity about which exchange matters.

## Reliability notes

- Primary/authoritative source quality is high because Binance is named in the market rules.
- Independence is low if used alone because both current price and candle data come from the same source family.
- The main residual risk is not source credibility but exact-timestamp settlement and short-horizon price volatility.