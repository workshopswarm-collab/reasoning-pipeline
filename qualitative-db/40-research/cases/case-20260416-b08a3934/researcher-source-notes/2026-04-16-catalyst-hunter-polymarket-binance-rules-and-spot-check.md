---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page plus Binance API spot and 1m kline endpoints
source_type: primary_rule_plus_primary_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b08a3934/researcher-analyses/2026-04-16/dispatch-case-20260416-b08a3934-20260416T023832Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, settlement, btc, source-note]
---

# Summary

This source note captures the governing settlement mechanics from the Polymarket page and a direct spot-check of Binance BTC/USDT pricing via public API endpoints accessible from the runtime.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT **1 minute candle for 12:00 ET on April 17, 2026** has a final **Close** above 72,000.
- The named source of truth is Binance BTC/USDT with **1m** candles, not another exchange or pair.
- At runtime check on 2026-04-15 22:43 ET / 2026-04-16 02:43 UTC, Binance public API returned BTCUSDT spot around **75,171.90** and latest one-minute closes around **75.0k-75.2k**.
- That places spot roughly **3.2k above** the market strike with about **13 hours 17 minutes** remaining until the settlement candle opens and closes.

## Evidence directly stated by source

From Polymarket rules page:
- Yes iff the Binance 1 minute candle for BTC/USDT at 12:00 ET on the specified date has final Close above the threshold.
- Resolution source is Binance.
- Price precision is determined by Binance source precision.

From Binance API spot checks:
- `api/v3/ticker/price?symbol=BTCUSDT` responded 200 with price 75171.90000000.
- `api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5` responded 200 with recent one-minute closes around 75048.63, 75131.00, 75114.90, 75184.71, 75193.18.

## What is uncertain

- The exact settlement candle is still in the future; current spot only indicates distance from strike, not final resolution.
- Binance web UI was WAF-challenged from this runtime, so the direct accessible verification surface was the public API rather than the webpage UI named in the rules text.
- No strong independent catalyst source was found in-tool that obviously implies a >$3k adverse move into noon ET tomorrow.

## Why this source may matter

This is the key source set because it defines what counts for settlement and confirms the market is currently materially above the threshold, making the remaining question mostly about near-term downside catalysts and path risk rather than ambiguity about the contract.

## Possible impact on the question

If Binance BTC/USDT remains near current levels, Yes is favored. The main residual risk is a sharp overnight-to-noon ET downside move exceeding roughly 4% from current levels, or an operational/interpretive issue around the exact noon ET one-minute candle.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the final price itself.
- Binance public market-data API is a strong direct source for BTC/USDT pricing, though the rules text specifically names the Binance trading UI candle display as the resolution surface.
- Evidence independence is moderate: both sources point to the same settlement mechanism rather than offering separate causal evidence.
- Operational access friction to Binance web UI is itself modestly relevant because UI-vs-API surface differences are worth acknowledging in rule-sensitive markets, even if no discrepancy is apparent here.
