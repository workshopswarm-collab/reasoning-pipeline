---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and market rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, binance, market-implied-probability]
---

# Summary

This source establishes both the contract mechanics and the current market-implied probability for the specific 70,000 threshold.

## Key facts extracted

- The market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026.
- The relevant field is the final candle `Close` price, not intraminute high/low and not another exchange.
- The condition is strict: the close must be higher than 70,000.
- The event page showed the 70,000 line trading around 86 cents / 85% implied probability at fetch time.
- Neighboring thresholds on the same page were roughly 94% for 68,000 and 73% for 72,000, which helps bracket the market's near-term BTC distribution.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- The 70,000 threshold was shown at about 85% / Buy Yes 86¢.

## What is uncertain

- The page is not itself the authoritative settlement source; Binance is.
- The exact displayed market price can move after fetch time.
- The page does not itself provide the final April 20 candle outcome, only the rule and current pricing.

## Why this source may matter

This is the governing contract surface for what counts, what does not count, and what the market is currently pricing.

## Possible impact on the question

It materially narrows the forecast problem. The question is not whether BTC trades above 70k at any point, nor whether major reference prices stay above 70k generally. It is whether Binance BTC/USDT prints a noon ET 1-minute close above 70,000 on April 20.

## Reliability notes

Useful and necessary for contract interpretation, but settlement authority still sits with the referenced Binance data surface rather than Polymarket's own summary page.
