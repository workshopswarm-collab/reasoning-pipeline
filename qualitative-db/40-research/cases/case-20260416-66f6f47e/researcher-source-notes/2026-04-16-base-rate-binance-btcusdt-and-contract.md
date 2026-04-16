---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-daily-close-window
entity: btc
topic: Binance BTC/USDT spot level versus April 21 noon ET close-above threshold contract
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 21 be above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance public market data API plus Polymarket contract rules page
source_type: primary_and_governing_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, binance, polymarket, btc, threshold-market]
---

# Summary

This note captures the governing contract mechanics from the Polymarket market page and a direct spot check of Binance BTC/USDT pricing relevant to the April 21 noon ET close-above-72000 market.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final Close above 72000.
- The governing source is explicitly Binance BTC/USDT with 1m candles, not another exchange or pair.
- A direct Binance API spot check on 2026-04-16 returned BTCUSDT price `73764.37`.
- Recent Binance daily candles in late March through mid-April show BTC frequently trading in the high-60k to mid-70k range, with multiple daily closes and highs above 72000 by mid-April.
- Recent 4h and 1h Binance candles show BTC trading materially above 72000 during the latest observed window.

## Evidence directly stated by source

- Contract rule: resolve Yes only if the April 21 12:00 ET Binance 1-minute candle Close is higher than 72000.
- Binance ticker check: BTCUSDT spot was above 72000 at time of review.
- Binance recent candles: BTC has already been spending meaningful time above the threshold, so the event no longer requires a large upside move from current levels.

## What is uncertain

- The market depends on one exact timestamped 1-minute Close, not whether BTC trades above 72000 at other times.
- Spot and recent candles do not prove what the April 21 12:00 ET close will be.
- Exchange-specific operational or data-display issues could still matter at settlement even if BTC broadly remains above 72000 elsewhere.

## Why this source may matter

This is the core mechanism evidence. The main question is not whether BTC can reach 72000 from below; it is whether BTC can remain above 72000 at one specified Binance minute close several days from now.

## Possible impact on the question

Because BTC is already above 72000 with several days remaining, the outside-view prior moves toward Yes relative to a case where BTC were far below the line. But the contract is still narrower than a generic "trades above 72k this week" claim because all material conditions must hold: correct exchange, correct pair, correct timestamp, and final 1-minute Close above the threshold.

## Reliability notes

- Binance data is the direct governing market source for settlement mechanics and the most important primary source here.
- The Polymarket page is the authoritative rule surface for how the contract maps to Binance data.
- Independence is limited because both points are part of the same mechanism stack rather than independent macro evidence.
- For direction, this is still strong because the contract is tightly tied to a specific exchange print.