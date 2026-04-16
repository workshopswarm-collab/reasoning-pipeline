---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Binance / Kraken spot snapshot plus CME contextual page
source_type: exchange data + contextual institutional reference
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: medium
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/catalyst-hunter.md]
tags: [binance, kraken, cme, spot, verification]
---

# Summary

A quick verification pass on live exchange/reference surfaces showed ETH trading around $2,333-$2,334 at the time of checking, well below $2,400. That does not contradict the Polymarket resolution because the market is triggered by any qualifying Binance 1-minute high during the week, not by the current price at the time of review.

## Key facts extracted

- Binance public ticker returned ETHUSDT price `2333.01000000`.
- Kraken public ticker returned last trade around `2333.87000`, daily high `2417.01000`, and daily open `2370.00000`.
- CME’s Ether overview page is not a direct resolution source, but it is useful contextual confirmation that institutional ETH derivatives remain active and that short-dated crypto options are often used around market-moving events.

## Evidence directly stated by source

- Binance API response: `{"symbol":"ETHUSDT","price":"2333.01000000"}`
- Kraken API response included `"h":["2417.01000","2417.01000"]`, indicating the venue had already traded above $2,400 intraday, though Kraken is not the governing resolution source.
- CME overview text emphasizes that shorter-term contracts are used to manage risk around market-moving events and weekly expiries.

## What is uncertain

- Binance ticker is only a current spot snapshot, not the historical 1-minute high record needed to prove the exact threshold-crossing candle.
- Kraken’s daily high is contextual only because the market rules exclude non-Binance venues.
- CME content is thematic context, not event-specific evidence for this market.

## Why this source may matter

This note supports an extra verification pass: it checks whether current spot behavior is obviously inconsistent with the market state and whether there is broader venue context consistent with a threshold breach having happened earlier.

## Possible impact on the question

The note does not govern settlement, but it modestly reinforces that a brief threshold breach was plausible: another major exchange printed a daily high above $2,400 even though current price later fell back into the low $2,330s.

## Reliability notes

- Binance and Kraken API outputs are direct machine-readable exchange data, but only Binance counts for settlement here.
- Kraken is independent contextual evidence, helpful mainly as a plausibility check.
- CME is high-credibility context but low direct relevance to this narrow resolution question.