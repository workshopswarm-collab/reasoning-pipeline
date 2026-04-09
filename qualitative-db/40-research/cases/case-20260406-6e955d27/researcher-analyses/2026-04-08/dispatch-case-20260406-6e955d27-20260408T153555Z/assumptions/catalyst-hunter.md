---
type: assumption_note
case_key: case-20260406-6e955d27
dispatch_id: dispatch-case-20260406-6e955d27-20260408T153555Z
research_run_id: 3aa63e3c-17da-4378-9171-e8d83418faba
analysis_date: 2026-04-08
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-66-000-on-april-6
question: "Will the price of Bitcoin be above $66,000 on April 6?"
driver: operational-risk
date_created: 2026-04-08
agent: catalyst-hunter
status: active
certainty: high
importance: medium
time_horizon: "resolved historical check"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/personas/catalyst-hunter.md"]
tags: ["assumption", "resolution-mechanics", "binance", "timezone"]
---

# Assumption

The relevant resolution candle is the Binance BTCUSDT 1-minute candle that **opens at 12:00:00 ET on 2026-04-06** and closes at 12:00:59 ET, with its final reported `close` field determining settlement.

## Why this assumption matters

The market wording says "the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon)" and resolves on the final "Close" price. If the contract instead meant the minute ending exactly at noon or some differently indexed chart convention, the operational interpretation could shift.

## What this assumption supports

- The conclusion that the correct settlement reference is the candle with open time 12:00 ET.
- The high-confidence Yes view based on the returned close price of 69,938.59.

## Evidence or logic behind the assumption

- Binance kline documentation identifies candles by **open time**.
- The market rule names the 12:00 ET 1-minute candle rather than a trade print at noon.
- On standard charting conventions, a 1-minute candle labeled 12:00 covers the period 12:00:00-12:00:59.
- The adjacent candle check is consistent with this interpretation: the 11:59 candle closes at the 12:00:00 boundary, while the 12:00 candle closes at 12:00:59.

## What would falsify it

- Explicit Polymarket adjudication text saying the 12:00 ET candle means the candle ending at noon rather than the candle beginning at noon.
- Clear Binance UI labeling showing a contradictory minute index for historical 1-minute candles in this market context.

## Early warning signs

- Evidence that Polymarket moderators historically use a different candle-label convention than Binance API open-time indexing.
- Evidence that Binance web UI historical candles diverge from API kline indexing for timezone-selected views.

## What changes if this assumption fails

The conclusion likely would still remain Yes in this case unless the alternative minute's close were below 66,000. Here the adjacent 11:59 ET candle close was 69,968.87 and the 12:01 ET candle close was 69,959.11, so a one-minute indexing dispute would still not threaten the Yes outcome.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260406-6e955d27/researcher-analyses/2026-04-08/dispatch-case-20260406-6e955d27-20260408T153555Z/personas/catalyst-hunter.md