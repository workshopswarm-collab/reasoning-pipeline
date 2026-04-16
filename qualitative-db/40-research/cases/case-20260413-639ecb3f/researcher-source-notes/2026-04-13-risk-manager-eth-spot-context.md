---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-13
source_name: CoinGecko, Binance, and Kraken spot-price checks
source_type: market data / exchange context
source_url: https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [liquidity, sentiment]
upstream_inputs: []
downstream_uses: []
tags: [market-data, spot-price, ethereum, context]
---

# Summary

Direct spot checks show ETH already trading very near the $2,400 target on 2026-04-13, which is the main support for a high probability of a touch during the April 13-19 window. At the same time, being near the target is not equivalent to certainty, because crypto can reverse sharply and the exact settlement source may not match every exchange print.

## Key facts extracted

- CoinGecko simple price endpoint returned ETH at `2348.43` USD.
- Binance ticker returned `2361.40000000` for `ETHUSDT`.
- Kraken ticker returned last trade `2358.97000` for ETH/USD, with session high `2359.23000`.
- Across these sources, ETH was roughly 1.6% to 2.2% below $2,400 at time of check.
- The target therefore appears close enough to be reachable in normal crypto volatility over a week, but not already satisfied at the instant sampled.

## Evidence directly stated by source

- Multiple live market-data endpoints place ETH in the mid-2350s to low-2360s.
- Independent venues are broadly consistent on spot level.

## What is uncertain

- These are contextual spot sources, not necessarily the exact governing resolution source for Polymarket settlement.
- Single snapshots do not tell us realized volatility distribution over the rest of the week.
- Binance ETHUSDT is a USDT pair, so it is a useful contextual reference but not perfect for any USD-specific settlement source.

## Why this source may matter

This is the core directional support for a yes-lean on a $2,400 touch: ETH does not need a large move to get there. But it also frames the main risk-manager objection to overconfidence: a small remaining gap can still matter when a market price already implies a high likelihood.

## Possible impact on the question

The spot context pushes probability materially above 50% and probably into a high-probability zone. It does not by itself justify near-certainty, because the path still requires an additional upward move and the exact resolution source remains only partially specified from the contract surface captured here.

## Reliability notes

- High recency and decent cross-source consistency.
- Independence is moderate because all sources reflect the same underlying market regime.
- Best used as contextual price evidence, not as the sole resolution authority.