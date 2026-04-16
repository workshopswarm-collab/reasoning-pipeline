---
type: source_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close-market
entity: btc
topic: Polymarket contract wording and market-implied odds for BTC > 72k on Apr 17 noon ET
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page
source_type: market platform / contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/variant-view.md
tags: [polymarket, contract-rules, market-price, binance, noon-close]
---

# Summary

Polymarket’s event page directly states that this market resolves from the Binance BTC/USDT **1-minute candle close at 12:00 ET on Apr 17**, not from an intraday high, daily close, or another exchange. The same page shows the current market-implied probability around **87%** for the 72,000 threshold.

## Key facts extracted

- The event page lists the 72,000 line at **87%**.
- Resolution condition: **Yes** if the Binance BTC/USDT **1-minute candle for 12:00 ET** on the specified date has a final **Close** price **higher than 72,000**.
- Otherwise the market resolves **No**.
- Resolution source is explicitly Binance BTC/USDT with **1m** candles selected.
- The page explicitly warns that this is **Binance BTC/USDT**, not another venue or pair.
- Price precision is determined by Binance’s displayed precision.

## Evidence directly stated by source

Directly stated on the event page:
- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."

## What is uncertain

- The public event page is enough to identify the governing source and mechanics, but it does not itself provide a historical reconstruction of the eventual Apr 17 12:00 ET closing candle.
- The fetched HTML is not the same thing as a direct Binance candle query, so later verification still needs Binance data directly.

## Why this source may matter

This is the primary contract/rules source. It determines what counts and what does not count. For this case, the distinction is material because a variant thesis can arise from the market acting like this is an easy "price stays above threshold sometime" setup, while the actual contract is a single **timestamped close** condition.

## Possible impact on the question

This source supports a more cautious view than a generic bullish BTC narrative alone would imply. The market only needs to be wrong by one noon snapshot, not by the broader trend. That creates path and timing risk that can matter even if BTC is trading above 72k well before or after the relevant minute.

## Reliability notes

- High credibility for contract wording and displayed market odds because it is the market venue itself.
- Not independent from the market price; it is the source of that price.
- Strong for mechanism definition, weak for future price forecasting by itself.