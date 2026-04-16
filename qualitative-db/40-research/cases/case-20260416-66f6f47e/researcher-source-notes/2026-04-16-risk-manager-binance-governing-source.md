---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: threshold-close-markets
entity: btc
topic: Binance BTC/USDT governing source and current spot context
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API and market rules surface
source_type: primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: slightly_supportive
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, governing-source, btc, source-note]
---

# Summary

This source note captures the governing-resolution surface and current Binance BTC/USDT context for the Apr 21 noon-ET close-above-72000 market.

## Key facts extracted

- The Polymarket rules specify the governing source directly: Binance BTC/USDT, using the 1-minute candle at 12:00 ET on Apr 21, 2026, and the final **Close** value.
- Current Binance BTC/USDT spot fetched via Binance API on 2026-04-16 14:17 UTC was approximately **73,712.59**.
- Binance 24h stats at the same fetch showed:
  - 24h high: **75,425.00**
  - 24h low: **73,309.85**
  - 24h change: **-0.82%**
- Current spot is therefore about **1,712.59** above the 72,000 threshold, roughly **2.4%** above the required level.

## Evidence directly stated by source

- Binance API directly states current BTCUSDT spot and recent 24h range.
- Polymarket rules directly state that the market resolves from the Binance BTC/USDT 1-minute candle close at 12:00 ET, not from another exchange, not from a daily close, and not from an intraperiod high.

## What is uncertain

- This source does not say where BTC will trade on Apr 21 at 12:00 ET.
- API spot and 24h range are only contextual evidence, not settlement evidence.
- I did not directly capture the future qualifying 12:00 ET candle because it has not occurred yet.

## Why this source may matter

This is the most important direct source for contract interpretation and present-state anchoring. It identifies the exact operational condition that must hold and limits the market to one exchange, one pair, one timestamp, and one price field.

## Possible impact on the question

The current level being comfortably above 72k supports a modestly bullish view, but the contract is fragile to timing because only one 1-minute close at one future timestamp matters. That means path risk and noon-ET timing risk remain material even though spot is currently above the line.

## Reliability notes

- High reliability for governing-source interpretation because Binance is the named resolution source and Polymarket rules explicitly reference it.
- Medium relevance for directional forecasting because current spot can move materially before Apr 21 noon ET.