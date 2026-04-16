---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: threshold-close-markets
entity: btc
topic: Bitcoin above $70,000 on April 20 resolution mechanics and market baseline
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / governing contract description
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/catalyst-hunter.md
tags: [polymarket, rules, resolution-source, market-baseline, btc]
---

# Summary
The Polymarket market page supplies both the current market-implied baseline and the governing resolution rule. For the $70,000 line, the visible price was 94¢/8¢ when fetched, consistent with the assignment's 0.93 current_price. The rules make this a narrow resolution market: the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 must have a final close strictly higher than 70,000.

## Key facts extracted
- The $70,000 outcome was trading around 94¢ Yes when fetched.
- The market page states this resolves from the Binance BTC/USDT market, not other exchanges or pairs.
- The qualifying observation is the final close of the 12:00 ET 1-minute candle on April 20, not the daily close, high, or an intraday touch.
- Price precision is determined by the source's displayed decimal precision.

## Evidence directly stated by source
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain
- The market page itself does not explain how Binance historical UI revisions or data-access quirks are handled if the live page becomes difficult to inspect later.
- The fetched page shows current odds but not a full order-book or recent price history for the specific line.

## Why this source may matter
This is the governing source-of-truth description for settlement mechanics, and it determines what counts and what does not count. It is decisive for distinguishing a close-above market from a touch-above market.

## Possible impact on the question
Because the contract uses a single minute-close on Binance at a specific ET timestamp, the main catalyst is not a broad multi-day “does BTC ever trade above 70k” narrative. The relevant question is whether BTC is still above 70k on Binance exactly at noon ET on April 20, which raises timing risk even when spot is comfortably above the threshold several days earlier.

## Reliability notes
High reliability for contract interpretation because it is the venue-specified rule surface. Lower reliability for broader market context because it is not an independent price-analysis source.