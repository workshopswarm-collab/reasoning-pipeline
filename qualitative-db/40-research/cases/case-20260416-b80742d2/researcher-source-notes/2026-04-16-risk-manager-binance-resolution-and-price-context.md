---
type: source_note
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: xrp
topic: xrp-above-1pt3-on-april-19
question: Will the Binance XRP/USDT 1-minute candle for 12:00 PM ET on 2026-04-19 close above 1.30?
driver: operational-risk
date_created: 2026-04-15T21:52:00-04:00
source_name: Binance spot API + Polymarket market rules
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [xrp]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-mechanics, price-threshold, source-note]
---

# Summary

This note captures the source-of-truth mechanics and direct market context for the XRP > 1.30 on April 19 contract. The key direct evidence is that Binance spot XRP/USDT is already trading around 1.401 on 2026-04-15/16 UTC and recent Binance candles have stayed materially above 1.30, but the contract resolves on one specific 1-minute candle at 12:00 PM ET on April 19 rather than on any broader daily average or cross-exchange print.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance XRP/USDT 1-minute candle for 12:00 in the ET timezone on April 19 has a final Close price higher than 1.30.
- Polymarket rules specify Binance XRP/USDT as the resolution source, not other exchanges or other XRP pairs.
- Binance spot API returned XRPUSDT around 1.4013 at research time.
- Binance 24h ticker showed lastPrice 1.4013, 24h high 1.4086, 24h low 1.3503, indicating spot remained comfortably above the 1.30 threshold during the recent day.
- Binance recent daily candles show closes above 1.32 for the last several sessions, with the last 10 daily closes all above 1.32.
- A direct API check of the most recent 1000 five-minute klines found zero closes at or below 1.30; the minimum close in that sample was about 1.3221.
- Binance documentation states klines are uniquely identified by open time and that the API supports a timezone parameter. The docs also note startTime and endTime are interpreted in UTC even if a timezone is provided.

## Evidence directly stated by source

- Polymarket directly states the exact contract mechanics and resolution source.
- Binance directly states the current spot price and recent historical kline values.
- Binance developer docs directly state that klines are identified by open time and expose timezone handling for kline interpretation.

## What is uncertain

- The final settlement appears intended to rely on the Binance web trading interface with 1m candles selected, while the API documentation clarifies kline mechanics but does not itself guarantee exact equivalence to any future front-end display nuance.
- The contract references the 12:00 ET candle, which creates narrow time-window risk: a temporary drawdown into noon on April 19 could still resolve No even if XRP trades above 1.30 for most of the surrounding period.
- No independent external catalyst source was successfully retrieved in this run due search-tool limitations, so context on upcoming XRP-specific event risk is thinner than ideal.

## Why this source may matter

This source set is the core evidence floor for the case because it combines the governing settlement text with the direct exchange data the contract points to.

## Possible impact on the question

If Binance spot remains near the current regime, Yes is favored. The main residual risk is not broad trend uncertainty alone but a path-specific failure: a sharp intraday drop or exchange-specific dislocation exactly into the noon ET candle on April 19.

## Reliability notes

- High credibility for direct exchange price and contract wording.
- Medium independence because the mechanics and price both ultimately route through Binance and Polymarket rather than multiple independent observers.
- Good for settlement interpretation; only moderate for broader catalyst forecasting.