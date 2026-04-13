---
type: source_note
case_key: case-20260413-63496469
dispatch_id: dispatch-case-20260413-63496469-20260413T173535Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-63496469 | market-implied
question: Will the price of Bitcoin be above $66,000 on April 14?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance Spot API and BTC/USDT market data
source_type: exchange API / official market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-63496469/researcher-analyses/2026-04-13/dispatch-case-20260413-63496469-20260413T173535Z/personas/market-implied.md]
tags: [binance, btcusdt, kline, settlement-source, source-note]
---

# Summary

This source note records the direct Binance surfaces most relevant to settlement mechanics for the Polymarket contract.

## Key facts extracted

- Binance Spot API documentation says `GET /api/v3/klines` returns candlestick bars and that the response field at index 4 is the `Close price`.
- The docs state klines are uniquely identified by open time.
- The docs also state `startTime` and `endTime` are interpreted in UTC, even if `timeZone` is provided.
- Converting the contract settlement time of 2026-04-14 12:00 ET gives 2026-04-14 16:00 UTC.
- A direct API pull for the analogous 2026-04-13 12:00 ET minute candle returned a close of `71902.91000000`, comfortably above 66,000.
- A direct API pull for the current BTCUSDT ticker returned `72461.53000000` on 2026-04-13 during this run.
- Binance 24hr ticker showed a day high of `72600.00000000` and low of `70505.88000000`, still well above 66,000.

## Evidence directly stated by source

- Binance Spot API docs define the kline endpoint and specify the close-price field used for the candle.
- Binance live market-data endpoints report current BTCUSDT spot levels far above the contract threshold.

## What is uncertain

- The contract resolves on the 2026-04-14 12:00 ET 1-minute candle close, which had not yet occurred at research time.
- A large intraday drawdown before settlement remains possible, though current levels leave a substantial cushion above 66,000.
- There is some operational dependence on Binance displaying/finalizing the relevant 1m candle normally at settlement time.

## Why this source may matter

This is the governing source family for settlement. It directly informs both contract interpretation and whether the market’s extreme probability is justified by current price distance from the threshold.

## Possible impact on the question

If Binance continues to print BTCUSDT near current levels, the market should resolve Yes. The only realistic path to No is a large spot selloff or a settlement/source handling issue before 2026-04-14 12:00 ET.

## Reliability notes

- Source quality is high because Binance is the explicit resolution source for the contract and the API docs define the candle structure directly.
- Independence is limited because both rule interpretation and live price context are Binance-linked surfaces rather than fully independent institutions.
- Operational mismatch risk exists because Polymarket references the Binance chart UI, while this note also uses Binance API documentation and endpoints; however, both point to the same exchange’s official market data family and should be directionally consistent for audit purposes.
