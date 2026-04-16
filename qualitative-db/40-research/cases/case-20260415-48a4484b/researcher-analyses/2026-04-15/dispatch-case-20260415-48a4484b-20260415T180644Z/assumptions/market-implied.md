---
type: assumption_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
research_run_id: 173d30b9-3384-4ed8-a465-26d27fe522a5
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-16 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-48a4484b/researcher-analyses/2026-04-15/dispatch-case-20260415-48a4484b-20260415T180644Z/personas/market-implied.md"]
tags: ["settlement-assumption", "binance", "timezone", "noon-close"]
---

# Assumption

The operative settlement datapoint is the Binance BTC/USDT 1-minute candle that opens at 12:00:00 ET on April 16, 2026 (16:00:00 UTC), and the market resolves from that candle's final Close price.

## Why this assumption matters

The case is narrow and rule-sensitive: a wrong mapping between ET noon and the relevant Binance minute would produce the wrong answer even if the directional BTC view is otherwise correct.

## What this assumption supports

- The conclusion that the market is mainly pricing short-horizon BTC downside risk rather than contract ambiguity.
- The estimate that current trading above 74k makes a Yes outcome likely but not certain.
- The judgment that market-implied probability near 93.5% is a little rich but directionally sensible.

## Evidence or logic behind the assumption

- The Polymarket rules explicitly cite the Binance BTC/USDT 1-minute candle for 12:00 ET and the candle's final Close.
- Binance API exposes 1-minute klines with precise UTC timestamps, making ET-to-UTC conversion straightforward.
- Converting noon ET on April 16, 2026 yields 16:00 UTC, which matches the natural interpretation of the relevant one-minute bar.

## What would falsify it

- Evidence that Polymarket or its resolver uses a different candle label convention than Binance API open time.
- A published clarification that the resolver uses a UI-displayed bar selection not equivalent to the 16:00:00 UTC kline.
- Exchange data irregularity or source outage forcing fallback handling.

## Early warning signs

- Any published contract clarification changing the timestamp interpretation.
- Binance UI/API mismatch around the noon ET bar.
- Resolver disputes on similar minute-candle markets.

## What changes if this assumption fails

Confidence in the current market-implied reading should drop because part of the price could reflect underappreciated resolution-mechanics risk rather than pure BTC level risk.

## Notes that depend on this assumption

- Main finding: personas/market-implied.md