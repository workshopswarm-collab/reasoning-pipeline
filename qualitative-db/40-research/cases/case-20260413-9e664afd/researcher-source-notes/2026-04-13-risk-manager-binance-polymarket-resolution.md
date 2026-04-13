---
type: source_note
case_key: case-20260413-9e664afd
dispatch_id: dispatch-case-20260413-9e664afd-20260413T164930Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-9e664afd | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-14 close above 70000?
driver: operational-risk
date_created: 2026-04-13T12:52:00-04:00
source_name: Binance API plus Polymarket market rules page
source_type: primary_and_contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9e664afd/researcher-analyses/2026-04-13/dispatch-case-20260413-9e664afd-20260413T164930Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution, timing, btc]
---

# Summary

The key direct evidence for this case is straightforward: Binance spot BTC/USDT was trading around 72.3k at approximately 12:51 ET on 2026-04-13, while the Polymarket market rules specify that resolution depends only on the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-14. That makes the thesis directionally favorable for Yes, but the risk-manager takeaway is that the contract is narrow and path-independent: only one minute close on one venue matters.

## Key facts extracted

- Binance API `ticker/price` returned BTCUSDT around 72,314.69 on 2026-04-13 around 12:51 ET.
- Binance API `klines?interval=1m&limit=1` showed the current 1-minute candle opening at 12:51:00 ET and closing at 12:51:59.999 ET, confirming the API timestamps map cleanly to ET when converted from UTC.
- Polymarket rules state the market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-14 has a final close strictly higher than 70,000.
- Polymarket rules also specify this is Binance BTC/USDT specifically, not another exchange or pair, and that price precision follows the source.

## Evidence directly stated by source

- Binance direct market data indicates current spot is materially above 70,000.
- Polymarket directly states the governing resolution condition and source of truth.

## What is uncertain

- This source set does not itself predict tomorrow's noon ET close; it only establishes current level, timing mapping, and settlement mechanics.
- There remains ordinary BTC intraday downside risk plus venue-specific or data-display risk between now and resolution.

## Why this source may matter

This source pair is enough to define the contract mechanics and establish that the current spot cushion versus 70,000 is meaningful but not dispositive. The main risk is not misunderstanding the threshold; it is underestimating 24-hour volatility or any Binance-specific settlement wrinkle.

## Possible impact on the question

The evidence supports a Yes-lean because BTC is already above the threshold by more than 2,000, but it also highlights the narrow failure mode: a selloff or noon-specific dip below 70,000 on Binance alone is sufficient for No.

## Reliability notes

- Binance API is the closest direct source-of-truth surface available in this environment, though the market text references the Binance trading UI candles rather than the REST API explicitly.
- Polymarket rules page is a high-value contextual source for contract interpretation.
- Independence is moderate rather than high because both sources reference the same underlying venue mechanics.