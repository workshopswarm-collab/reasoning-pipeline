---
type: source_note
case_key: case-20260413-63496469
dispatch_id: dispatch-case-20260413-63496469-20260413T173535Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-66k-on-april-14
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 66000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance BTCUSDT API and Polymarket market rules
source_type: primary-plus-resolution-rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10 ; https://polymarket.com/event/bitcoin-above-on-april-14
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-63496469/researcher-analyses/2026-04-13/dispatch-case-20260413-63496469-20260413T173535Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, resolution-rules, timing-check]
---

# Summary

This source check establishes both the governing settlement mechanics and the current spot reference level most relevant to the case. Binance is the explicit source of truth for settlement, and Polymarket specifies that the deciding observation is the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14, using the final Close price.

## Key facts extracted

- Polymarket rules state the market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 14 has a final Close strictly higher than 66,000.
- The contract is exchange-specific: Binance BTC/USDT only, not other exchanges or pairs.
- Binance spot BTCUSDT was approximately 72,423.78 at verification time on 2026-04-13.
- Recent Binance 1-minute candles around verification time were all around 72.4k-72.5k, far above 66,000.
- Binance exchange info for BTCUSDT showed the pair as TRADING and the price filter tick size as 0.01, which matters for precision and exact close interpretation.

## Evidence directly stated by source

- Direct resolution wording from Polymarket: final close of the Binance 1-minute candle at 12:00 ET is the source of truth.
- Direct market structure from Binance: live BTCUSDT price and recent 1-minute candles.

## What is uncertain

- The source note does not by itself establish what exogenous catalyst could move BTC down by more than 8% before noon ET on April 14.
- The Binance API verification was done in UTC; the case still requires a timezone mapping from 12:00 ET on April 14 to the corresponding Binance minute candle at 16:00 UTC if EDT remains in effect.
- Short-lived exchange dislocations, extraordinary macro shocks, or exchange-specific operational problems could still matter despite the large cushion.

## Why this source may matter

This is the main source-of-truth check. For a narrow date/time crypto market, settlement mechanics and the current spot-to-strike distance are the highest-value inputs. The market is primarily about whether price stays above a threshold rather than discovering some hidden fundamental.

## Possible impact on the question

The source strongly supports a high Yes probability because the current Binance BTCUSDT level is roughly 6.4k above the strike with less than one day to resolution. The main remaining uncertainty is not ordinary drift but whether a meaningful downside catalyst or operational anomaly hits before the precise settlement minute.

## Reliability notes

- Binance is authoritative for this contract because Polymarket explicitly names it as the resolution source.
- Polymarket page text is a direct statement of rules but fetched as raw page content; still useful because it matches the assignment’s quoted market description.
- Evidence independence is limited because the central question is mechanically tied to one named source of truth. That is acceptable here because the contract itself is source-specific.