---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8bb1e3b4 | market-implied
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/market-implied.md]
tags: [polymarket, contract, resolution, bitcoin, btc]
---

# Summary

This source provides both the live market-implied probability for the 70,000 threshold and the exact contract wording. It is the governing market interface but not the ultimate resolution source.

## Key facts extracted

- The 70,000 line was trading around 88 cents Yes / 14 cents No at fetch time, implying about an 88% market-implied probability of closing above 70,000.
- The contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026.
- The relevant field is the final candle "Close" price, not intraday high, low, midpoint, or another exchange.
- The page states that price precision is determined by the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- The 70,000 outcome was shown at 87% in the market summary and 88 cents on the buy-Yes button; for this run I treat current_price=0.88 from assignment context as the baseline.

## What is uncertain

- The fetched web page is a dynamic market interface and may lag or show small display inconsistencies versus the assignment snapshot.
- The Polymarket page references Binance UI candles, but later settlement may rely on the same underlying Binance data rather than the visible frontend rendering.
- This source alone does not say whether Binance will be fully operational and accessible at settlement time.

## Why this source may matter

The market-implied persona has to begin here because price is the prior. The contract wording also determines what exact event has to happen: a Binance BTC/USDT 1-minute close above 70,000 at noon ET on April 20.

## Possible impact on the question

This source supports a high prior for Yes while also narrowing the risk to a few material failure modes: BTC price drawdown below 70,000 by the exact minute, Binance-specific print divergence, or some operational/source-of-truth issue.

## Reliability notes

Useful and necessary, but not sufficient alone. It is the best source for the market prior and contract wording; it should be paired with direct Binance market data and an independent contextual price source.