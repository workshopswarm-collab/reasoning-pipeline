---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market/rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, market-state]
---

# Summary

Polymarket’s market page provides the current market-implied probability and the operative contract wording. For the $70,000 line, the page showed roughly 85-86% Yes on 2026-04-14. The rules state the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, using the final Close price, not any other exchange or pair.

## Key facts extracted

- The relevant line is **70,000** for **Apr 20, 2026**.
- The market page showed the 70,000 contract around **85%** headline probability, with tradable quotes around **86¢ Yes / 16¢ No** at fetch time.
- Resolution is **not** based on a daily close, CME close, Coinbase print, or consolidated index.
- Resolution is explicitly tied to the **Binance BTC/USDT** market.
- The deciding print is the **final Close** of the **12:00 ET** one-minute candle on April 20.
- Price precision is determined by the source as displayed by Binance.

## Evidence directly stated by source

- “This market will resolve to ‘Yes’ if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final ‘Close’ price higher than the price specified in the title.”
- “The resolution source for this market is Binance, specifically the BTC/USDT ‘Close’ prices currently available at https://www.binance.com/en/trade/BTC_USDT with ‘1m’ and ‘Candles’ selected on the top bar.”
- “Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs.”

## What is uncertain

- The market page itself is not the source of truth for the final candle print; it only states the rules.
- The fetched page is a rendered market page and may show slightly stale displayed quotes relative to live market microstructure.
- The page does not itself clarify DST mechanics beyond saying 12:00 ET; April 20 should therefore be interpreted as 12:00 noon America/New_York, which is EDT on that date.

## Why this source may matter

This is the governing contract text and the direct source for the market-implied baseline. It defines the exact timestamp, venue, instrument, and print type that matter.

## Possible impact on the question

It materially narrows the problem: the question is not “Will BTC hold above 70k on average by April 20?” but whether Binance BTC/USDT specifically prints a final 12:00 ET one-minute close above 70,000 on April 20.

## Reliability notes

Useful as the contract source and for market pricing, but final settlement still depends on Binance’s actual candle data. The rules are clear enough that exchange mismatch risk is low, while timestamp interpretation still deserves explicit verification.