---
type: domain_overview
domain: crypto
subdomain: defi
topic: defi research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs: []
downstream_uses: []
related_entities: []
related_drivers: [liquidity, tokenomics, operational-risk, regulation]
tags: [domain/crypto, subdomain/defi, overview]
---

# Overview summary

DeFi is the onchain financial-intermediation subdomain of crypto: lending, decentralized exchange activity, collateral systems, stablecoin plumbing, derivatives, and protocol-native leverage. It deserves a standalone overview because its evidence stack, failure modes, and market structure differ meaningfully from base protocol research or exchange-access research.

## Why this subdomain matters

This subdomain matters because DeFi is where crypto shifts from asset ownership into credit creation, liquidity formation, leverage, and settlement behavior. Researchers need a structural note for onchain financial systems so they do not collapse all crypto activity into token price action or general protocol adoption.

## Core conclusions

- DeFi systems should be evaluated as financial infrastructure, not just application activity.
- Liquidity, collateral quality, and stablecoin dependence are central to DeFi durability.
- Yield and usage can be reflexive, so apparent growth must be separated from sustainable demand.
- Smart-contract and governance risk are part of the economic structure, not side risks.

## Main evidence clusters

- lending and borrowing markets
- DEX liquidity and routing activity
- stablecoin dependence and collateral structure
- leverage, liquidations, and reflexive demand
- governance and protocol-upgrade design
- smart-contract security and exploit history

## Important recurring objects

- lending protocols
- decentralized exchanges
- stablecoins and collateral assets
- governance tokens
- bridges, oracles, and liquid staking infrastructure
- treasuries and protocol foundations

## Important recurring drivers

- liquidity
- tokenomics
- operational-risk
- regulation
- ecosystem-growth

## Common conflicts or failure modes

- treating nominal TVL or activity as proof of durable demand
- ignoring concentration in a few collateral assets or stablecoins
- underweighting exploit, bridge, oracle, or governance risk
- confusing token-incentivized activity with persistent product-market fit

## Missing coverage

- better DeFi metrics playbooks beyond headline TVL
- stronger notes on stablecoin and collateral concentration
- more explicit exploit-history and oracle-risk summaries
- clearer separation of protocol value capture from token speculation

## Most fragile assumptions

- that high yield implies healthy organic demand
- that liquidity is durable under stress
- that onchain composability always improves resilience rather than contagion

## Recommended next research steps

- keep protocol- or event-specific DeFi developments in `40-research/`
- use this note for structural orientation across lending, DEX, and collateral systems
- deepen substructure only where repeated retrieval demand justifies protocol-specific decomposition
