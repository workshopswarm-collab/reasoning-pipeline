---
type: source_note
case_key: case-20260413-de71fc13
dispatch_id: dispatch-case-20260413-de71fc13-20260413T130158Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-de71fc13 | market-implied
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-13 close above 68000?
driver: reliability
date_created: 2026-04-13
source_name: Binance spot API BTCUSDT ticker and 1-minute klines
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
source_date: 2026-04-13
credibility: high
recency: high
stance: supports_yes
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, primary-source, 1m-candle, settlement]
---

# Summary

Binance's live spot API shows BTC/USDT trading around 71.1k shortly after 09:00 ET on 2026-04-13, materially above the 68k threshold that governs the market. The recent 1-minute candles from the same Binance API also show a stable tape near 71k rather than a price hovering close to the strike.

## Key facts extracted

- Binance `ticker/price` returned BTCUSDT at `71171.41000000`.
- Binance `klines` for the last 10 one-minute intervals showed closes from about `71074.91` to `71208.05`.
- The visible exchange server time during retrieval was `2026-04-13T13:02:52Z`, which is `09:02:52 ET`, about 2 hours 57 minutes before the noon ET resolution candle.
- The 09:00-09:03 ET candles (13:00-13:03 UTC) all remained above 71k.

## Evidence directly stated by source

- Current BTC/USDT price on Binance was above 68k by more than 3k.
- Minute-candle closes immediately before and after 09:00 ET were also above 68k.
- Binance is the direct exchange and pair named in the market rules, so this is not merely contextual price evidence; it is the same source family used for settlement.

## What is uncertain

- The contract resolves on the final close of the 12:00 ET candle, not the current price near 09:00 ET.
- Intraday volatility between 09:00 ET and 12:00 ET could still push BTC/USDT below 68k by the settlement minute.
- The market rules reference the Binance web chart surface with 1m candles selected; API values are highly relevant but are still a verification proxy rather than the exact UI surface named in the rule text.

## Why this source may matter

This is the strongest direct evidence because it verifies the exact exchange and trading pair the contract uses, and it shows the market is currently far in-the-money relative to the 68k threshold.

## Possible impact on the question

This source strongly supports a high Yes probability and helps explain why Polymarket priced the contract at an extreme level. Because the spot is more than 4.6% above the threshold with only a few hours left, a No outcome would likely require a sizable same-morning drawdown.

## Reliability notes

- Primary/authoritative for underlying price observation: yes.
- Exact settlement surface match: partial, because the rule text names the Binance trading UI candle close while this note uses Binance API endpoints.
- Independence: low, since the ticker and klines are both Binance-derived, but that is acceptable here because Binance is the governing source of truth.