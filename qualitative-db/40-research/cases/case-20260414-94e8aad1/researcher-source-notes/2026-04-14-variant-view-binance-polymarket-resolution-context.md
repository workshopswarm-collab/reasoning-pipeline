---
type: source_note
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and Binance API spot/1m references
source_type: primary-market-rules-plus-direct-exchange-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-94e8aad1/researcher-analyses/2026-04-14/dispatch-case-20260414-94e8aad1-20260414T175223Z/personas/variant-view.md]
tags: [polymarket, binance, resolution-criteria, btc]
---

# Summary

This source note captures the contract mechanics and current exchange context that matter most for the case. The key variant-view takeaway is that the market is probably directionally right, but the contract is narrower than a generic “BTC stays strong” thesis: only the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 16 matters.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close strictly higher than 70,000.
- The source of truth is Binance, not a cross-exchange average and not another BTC pair.
- Price precision is determined by the decimals shown in the Binance source.
- On 2026-04-14 around 13:53 ET, Binance direct endpoints showed BTCUSDT around 74.65k.
- Binance recent 1-minute klines confirmed the exchange provides discrete 1-minute close values suitable for contract settlement.
- Binance 24h ticker context showed BTCUSDT had traded as high as about 76,038 and as low as about 72,053.78 over the prior 24 hours.

## Evidence directly stated by source

From Polymarket rules:
- settlement uses the Binance BTC/USDT Close price on the 12:00 ET 1-minute candle
- the threshold is 70,000
- strict comparison is “higher than”

From Binance direct data:
- last trade / reference price was roughly 74.65k at the time checked
- recent 1-minute candles were publishing normally
- 24h range remained entirely above 70k at the time checked

## What is uncertain

- The market resolves on April 16 noon ET, not at current time, so price can still move materially before settlement.
- The exact mapping between “12:00 in the ET timezone” and Binance’s UTC-timestamped kline display can create operational interpretation risk if Polymarket later references the website UI rather than raw API conventions.
- A sharp macro or crypto-specific drawdown before noon ET April 16 could still push BTC below 70k even from current levels.

## Why this source may matter

This is the core evidence floor for the case because it verifies both the governing contract language and the direct exchange surface that will determine resolution. It also sharpens the variant view: the realistic alternative is not “BTC is secretly weak right now,” but “the market may be slightly overconfident because a narrow time-specific settlement can still be tripped by short-horizon volatility or source-interpretation issues.”

## Possible impact on the question

The direct evidence supports a high Yes probability, since spot BTCUSDT is materially above 70k and even the recent 24h low remained above 70k. But it does not justify near-certainty because the contract is a single-minute, exchange-specific, date-specific snapshot.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the eventual price print itself.
- Binance is the stated settlement source and therefore the authoritative price surface.
- Evidence independence is moderate rather than high because both pieces are tightly coupled: Polymarket explicitly delegates truth to Binance.
- The remaining residual risk is mostly operational/timing interpretation plus ordinary BTC volatility over the next ~46 hours.
