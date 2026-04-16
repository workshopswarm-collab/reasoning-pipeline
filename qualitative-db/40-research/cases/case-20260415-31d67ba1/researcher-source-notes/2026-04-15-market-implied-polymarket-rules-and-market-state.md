---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market listing / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-price, btc]
---

# Summary

Polymarket shows the Apr 17 BTC-above ladder with the 70,000 line trading around 97.2% Yes, and the rules specify resolution from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr 17 using the final Close price.

## Key facts extracted

- Market title: Bitcoin above ___ on April 17?
- Relevant rung: 70,000.
- Visible market price for 70,000 rung: about 97.2% Yes at fetch time.
- Resolution condition: Yes iff the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 17 has a final Close strictly higher than 70,000.
- Resolution source is Binance BTC/USDT, not another exchange or trading pair.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- The contract is keyed to Binance BTC/USDT 1m candle close at 12:00 ET.
- The threshold comparison is strictly “higher than” 70,000.
- Other exchanges and pairs do not govern settlement.

## What is uncertain

- The Polymarket page is not itself the final authoritative settlement print; it only states the rule and current market odds.
- The page does not prove what the Binance print will be at settlement time.

## Why this source may matter

This is the governing market/rules surface and therefore the best source for what must happen for the contract to resolve Yes or No.

## Possible impact on the question

The market is pricing the threshold as highly likely, but the source also makes clear that a short-lived BTC selloff is enough to flip settlement if the exact Binance 12:00 ET 1-minute Close falls to 70,000 or below.

## Reliability notes

Useful as the contract-definition source and for market-implied probability. Less authoritative on the eventual answer than Binance itself, because Binance is the named source of truth for settlement.