---
type: source_note
case_key: case-20260415-868fc947
dispatch_id: dispatch-case-20260415-868fc947-20260415T090047Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: prediction-markets
entity: btc
topic: Polymarket contract wording and market-implied baseline
question: Will Binance BTC/USDT 12:00 ET Apr. 16 1-minute candle close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: prediction-market primary contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, rules, market-implied-probability, timing]
---

# Summary

The Polymarket event page provided both the market-implied baseline for the 72k threshold and the exact resolution wording. During the run, the 72,000 line was priced around 88%, indicating the market saw a strong but not guaranteed chance that Binance BTC/USDT remains above 72k at the specified noon ET minute on Apr. 16.

## Key facts extracted

- The 72,000 outcome was listed at about 88%.
- The event resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on Apr. 16 has a final close above 72,000.
- The page explicitly says the source is Binance BTC/USDT with 1m candles selected.
- The page also lists adjacent ladder prices: 70k around 98%, 74k around 54%, 76k around 15%.

## Evidence directly stated by source

- Market-implied probabilities across nearby price thresholds.
- Resolution wording and source-of-truth definition.
- Timing specificity: noon ET on Apr. 16, not daily close or any other exchange.

## What is uncertain

- Page scraping may not perfectly preserve every dynamic UI detail.
- Adjacent strike prices are contextual and do not directly settle the 72k contract.
- Polymarket contract text points to Binance website candle display, so there remains mild ambiguity about whether API and UI display are perfectly identical in every edge case.

## Why this source may matter

This is the governing contract page for the prediction market and therefore the authoritative source for what conditions need to hold.

## Possible impact on the question

The market baseline is already extreme on the Yes side, which raises the verification burden. The adjacent strike ladder implies traders see BTC as likely to stay above 72k but much less certain to remain above 74k, so the key near-term catalyst question is whether anything before noon ET could force a roughly 3% drawdown from current Binance spot.

## Reliability notes

High reliability for contract wording and observed market baseline. Medium reliability for scraped UI precision because live market prices can move and raw extraction may lag slightly.