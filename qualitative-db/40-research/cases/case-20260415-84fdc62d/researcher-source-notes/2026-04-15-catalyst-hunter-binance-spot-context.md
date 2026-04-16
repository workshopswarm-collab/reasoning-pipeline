---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot and daily candles
source_type: exchange-api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json, catalyst-hunter.md#resolution-or-source-of-truth-interpretation]
tags: [binance, btcusdt, spot-price, daily-candles]
---

# Summary
Binance spot data showed BTC/USDT around $74.2k on 2026-04-15, roughly 6% above the $70k threshold with five calendar days to resolution. Recent daily candles show BTC closing above $70k in most of the last several sessions, though with intraday swings that are large enough to matter for a single-minute noon snapshot.

## Key facts extracted
- Binance ticker price on 2026-04-15 was about `74192.71` USDT.
- Recent daily closes from Binance were:
  - 2026-04-07: `71924.22`
  - 2026-04-08: `71069.93`
  - 2026-04-09: `71787.97`
  - 2026-04-10: `72962.70`
  - 2026-04-11: `73043.16`
  - 2026-04-12: `70740.98`
  - 2026-04-13: `74417.99`
  - 2026-04-14: `74131.55`
- On 2026-04-15 the session range printed roughly `73514` to `74786.72` at capture time.
- The market therefore has current spot cushion of about `$4.2k` versus the threshold.

## Evidence directly stated by source
- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74192.71000000"}`.
- Binance daily kline history showed repeated closes above $70k over the most recent week.

## What is uncertain
- Daily candles do not answer the exact noon-ET one-minute-close condition.
- BTC can move several thousand dollars intraday, so spot cushion is supportive but not dispositive.
- Binance API spot and kline endpoints are machine-readable references, but the contract points to the Binance trading interface candle display as the governing settlement surface.

## Why this source may matter
This is the closest direct evidence for the actual exchange and pair used in settlement. It shows both the level versus threshold and the recent realized volatility that matters for a narrow timed contract.

## Possible impact on the question
If BTC remains near the current regime, the contract should resolve Yes comfortably. The main risk is a sharp selloff or noon-specific wick that closes below $70k despite BTC broadly trading above that level during the surrounding days.

## Reliability notes
High relevance because it is the same exchange and pair named in the rules. Still, the exact settlement source is the Binance 1-minute candle close at noon ET, so this note is best treated as near-direct context rather than final settlement proof.
