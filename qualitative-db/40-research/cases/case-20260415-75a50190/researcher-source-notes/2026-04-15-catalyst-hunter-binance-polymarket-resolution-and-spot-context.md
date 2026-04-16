---
type: source_note
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 ET on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance spot/API reference checks
source_type: primary_and_contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution, btc]
---

# Summary

This source note captures the governing market mechanics from the Polymarket market page and current Binance BTC/USDT spot context checked directly via Binance public API. The market is explicitly about the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21, 2026, not a daily close, not another exchange, and not another pair.

## Key facts extracted

- Polymarket rules say the market resolves YES if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final close strictly higher than 72,000.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Price precision is whatever Binance shows for the source candle.
- On 2026-04-15, the Polymarket 72,000 line was trading about 80-81% YES.
- Binance public API check on 2026-04-15 showed BTCUSDT last price 74,830.15.
- Binance 24h stats check showed high 75,281, low 73,514, open 74,140, last 74,830.15.
- Daily kline check for the prior 10 daily candles showed BTC has spent multiple consecutive recent days closing above 72,000 except for one notable dip to 70,740.98 on April 10 UTC daily candle.

## Evidence directly stated by source

From Polymarket market page rules:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

Direct Binance API outputs checked 2026-04-15:
- ticker price: 74,830.15
- 24h high/low: 75,281 / 73,514
- recent daily closes include 72,962.70, 73,043.16, 74,417.99, 74,131.55, 74,830.15

## What is uncertain

- The exact 12:00 ET one-minute candle on April 21 is still nearly six days away, so current spot only anchors distance-to-threshold, not settlement.
- Intraday volatility could easily exceed the ~3.8% cushion between current spot and 72,000.
- A sharp macro or crypto-specific risk event before April 21 could push BTC back below threshold.

## Why this source may matter

This is the governing source-of-truth surface for contract interpretation plus the most direct current evidence about how far BTC sits above the threshold today. It also clarifies that the relevant catalyst horizon is specifically "by next Tuesday noon ET" rather than a looser weekly or end-of-day framing.

## Possible impact on the question

This source materially supports a YES lean because spot is currently well above the threshold and recent daily closes have mostly been above it. It also narrows the relevant catalyst set: only events capable of producing a >3-4% downside move before or into Tuesday noon ET should materially threaten YES from here.

## Reliability notes

- Polymarket market rules are authoritative for the contract wording but not for final observed settlement data itself.
- Binance is the stated settlement source and therefore authoritative for the eventual price observation.
- Binance API spot checks are highly relevant contextual evidence for current distance from strike, but they do not directly settle the future event.
- Independence is limited because both the contract and the price source point back to Binance mechanics; that is fine for a narrow date-price market but should be acknowledged.