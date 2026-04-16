---
type: source_note
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page plus Binance API spot and 1m candles
source_type: primary_and_direct
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-89d9685e/researcher-analyses/2026-04-15/dispatch-case-20260415-89d9685e-20260415T181939Z/personas/base-rate.md]
tags: [binance, polymarket, contract-rules, spot-price, source-note]
---

# Summary

This note captures the direct resolution mechanics and current spot context for the April 16 BTC > 72,000 contract.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 in ET timezone (noon)** on the date in the title.
- The relevant field is the candle's final **Close** price.
- The threshold test is strictly whether that close is **higher than 72,000**.
- The contract is explicitly about **Binance BTC/USDT**, not other exchanges or other pairs.
- On 2026-04-15 around 14:08-14:20 ET, direct Binance API queries showed BTCUSDT trading around **74.2k-74.3k**, above the 72k threshold by roughly 2.2k+.
- Binance 1m kline timestamps retrieved during the check map cleanly to UTC times corresponding to the current ET afternoon, confirming the API can be used to interpret the relevant timing window.
- A direct Binance avgPrice pull also showed about **74.3k**, consistent with the ticker/klines check.

## Evidence directly stated by source

From Polymarket rules page:
- Yes resolves if the Binance 1 minute candle for BTC/USDT at **12:00 ET** on April 16 has a final close above 72,000.
- Resolution source is Binance BTC/USDT candles.
- Price precision is whatever Binance displays.

From Binance direct data pulls:
- ticker price check returned roughly **74.2k**.
- recent 1m klines also clustered around **74.2k-74.35k**.
- avgPrice endpoint returned roughly **74.314k**.

## What is uncertain

- These checks do **not** settle the market yet because the governing candle is the one at **2026-04-16 12:00 PM ET**, which had not occurred at research time.
- Intraday crypto volatility means BTC can move materially before tomorrow noon.
- There is some operational ambiguity in practice around whether users read Binance from UI candles or API candles, though both should normally reflect the same underlying market data.

## Why this source may matter

This is the core source set for the case because it covers both: 
1. the contract mechanics, and 
2. the direct exchange context against which the threshold should be judged.

## Possible impact on the question

Because spot is already materially above 72,000 one day before settlement, the outside-view starting point is that a one-day hold above the threshold is more likely than not and likely substantially so, absent a sharp drawdown before the noon ET reference candle.

## Reliability notes

- Polymarket rules page is authoritative for contract wording but not for future price.
- Binance is the named source of truth for settlement, so direct Binance market data is the most relevant direct evidence.
- The main residual risk is not source credibility but **future price movement** and any edge-case operational interpretation at the reference minute.