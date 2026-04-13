---
type: source_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-13
question: Will the price of Bitcoin be above $70,000 on April 13?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market rules and Binance spot/API surfaces
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-13
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/variant-view.md]
tags: [polymarket, binance, resolution-check, btc]
---

# Summary

The governing contract is explicitly tied to the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-13, using the candle's final Close price. Polymarket's public rules clearly specify Binance BTC/USDT, 1m candles, 12:00 in ET timezone, and close-price comparison against the threshold. A contextual verification pass against live Binance spot/API surfaces shows BTC/USDT trading around 71,603.23 at research time, which places spot modestly above the 70,000 threshold but does not itself settle the contract because the settlement depends on the specific noon ET 1-minute candle close.

## Key facts extracted

- Polymarket rules: market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on the specified date has a final Close above the threshold.
- The relevant threshold for this outcome is 70,000.
- The rules explicitly exclude other exchanges and other trading pairs.
- Price precision is determined by Binance source precision.
- At research time, a Binance API spot price check returned BTCUSDT at 71,603.23.
- A UTC conversion check for 12:00 ET on 2026-04-13 maps to 16:00:00 UTC.
- A direct historical-kline API query for the future target minute necessarily returned no candle yet (`[]`), which is expected and confirms the minute has not occurred at research time.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance API contextual checks:
- `ticker/price?symbol=BTCUSDT` returned `71603.23000000` during the run.
- `klines?...startTime=1776096000000&limit=1` returned `[]` before the target minute occurred.

## What is uncertain

- The specific 12:00 ET candle close had not occurred yet at research time.
- Spot price above 70k before noon does not guarantee the noon-minute close will remain above 70k.
- Public web/API presentation could differ slightly in surface formatting even if underlying Binance data are consistent.

## Why this source may matter

This is the core source-of-truth bundle for a date-sensitive, rule-sensitive crypto market. The main uncertainty here is not what source governs; it is whether BTC/USDT will remain above the threshold at the exact governing minute close.

## Possible impact on the question

This source bundle strongly supports a high Yes probability because live Binance spot is already materially above 70,000, but it also highlights the key variant risk: only the exact noon ET 1-minute close matters, so late volatility can still flip the outcome.

## Reliability notes

- Polymarket rules page is authoritative for contract mechanics.
- Binance is authoritative for settlement data under those rules.
- Evidence independence is medium rather than high because the contextual price verification comes from the same exchange family named in the rules, but that is appropriate for a source-of-truth market.
- The main residual risk is timing/measurement, not source credibility.
