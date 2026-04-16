---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: ethereum
entity: ethereum
topic: eth-2400-apr13-19-market-and-price-context
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Polymarket market page + CoinGecko current price + CryptoCompare recent daily history
source_type: market page and market-data aggregators
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [base-rate finding, base-rate assumption note, base-rate evidence map]
tags: [source-note, ethereum, polymarket, coingecko, cryptocompare, evidence-floor]
---

# Summary

This combined source note captures the contract framing, current market-implied probability for the 2,400 threshold, and recent ETH/USD price context needed for an outside-view estimate.

## Key facts extracted

- The Polymarket page for "What price will Ethereum hit April 13-19?" showed the 2,400 outcome trading around **76%** on 2026-04-13.
- The same page states the market has multiple threshold buckets, so the 2,400 price is one outcome in a weekly high-water-mark ladder rather than a simple spot-close contract.
- CoinGecko simple price API returned Ethereum spot around **$2,348.43** on 2026-04-13.
- CryptoCompare daily history showed the latest close around **$2,357.03** and recent daily highs climbing to about **$2,358.08**.
- Reaching 2,400 from a 2,348-2,357 spot level requires roughly a **1.8%-2.2%** upside move in the remaining week.
- In the recent 30-day data, ETH had already traded above 2,400 on at least one day in mid-March, showing the threshold is close enough to recent realized range to be plausible.
- A simple empirical check on recent CryptoCompare history produced a rough scaled 6-day hit rate around **75%** for analogous move size / horizon conditions; this is a rough heuristic, not a formal forecast model.

## Evidence directly stated by source

Directly stated by Polymarket page:
- 2,400 outcome currently around 76%.
- Market resolves based on what price Ethereum hits during April 13-19, not necessarily the weekly close.

Directly stated by CoinGecko / CryptoCompare data:
- Current spot is in the mid-2,300s.
- Recent realized daily prices and highs have already approached the threshold closely.

## What is uncertain

- The Polymarket page fetched cleanly, but the extracted FAQ text was not ideal for full rule detail; it clearly indicated the laddered outcome pricing but not the exact settlement source text in the fetched snippet.
- The recent empirical hit-rate check is only a rough outside-view heuristic and depends on limited sample history plus a scaling assumption.
- I do not have a fully authoritative primary-source resolution page beyond the market page itself in this run.

## Why this source may matter

This source matters because the weekly hurdle is small relative to current spot and recent realized volatility. For a base-rate lens, the key question is not whether ETH has a bullish story, but whether a roughly 2% intrawweek move is common enough from this starting level to justify a probability near or above market.

## Possible impact on the question

These sources support a view that 2,400 is a realistic threshold and probably somewhat more likely than not from current levels. They also support treating the market price as broadly reasonable rather than obviously inflated, because the required move is small and within recent normal ETH behavior.

## Reliability notes

- Polymarket is reliable for current market-implied pricing but not by itself for independent truth about future price paths.
- CoinGecko and CryptoCompare are strong contextual sources for current and recent market data, though they are still secondary aggregators rather than a single official exchange tape.
- Together they are adequate for this low-difficulty, short-horizon case because the question is essentially about a near-term price threshold and not a complex interpretive event.