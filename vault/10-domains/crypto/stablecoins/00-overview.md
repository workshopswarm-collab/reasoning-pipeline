---
type: domain_overview
domain: crypto
subdomain: stablecoins
topic: stablecoins research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs:
  - vault/40-research/source-notes/by-domain/crypto/2026-03-25-stablecoin-basics.md
downstream_uses: []
related_entities: []
related_drivers: [liquidity, regulation, operational-risk, trade]
tags: [domain/crypto, subdomain/stablecoins, overview]
---

# Overview summary

Stablecoins are the settlement-and-collateral subdomain of crypto: reserve-backed dollar proxies, redemption systems, payment rails, exchange settlement, and DeFi collateral plumbing. They deserve a standalone overview because they sit at the boundary between crypto-native liquidity and traditional money-like infrastructure.

## Why this subdomain matters

This subdomain matters because stablecoins are often the actual liquidity layer beneath trading, DeFi activity, cross-border payments, and onchain settlement. Researchers need a structural note for issuer concentration, reserve credibility, redemption mechanics, and chain distribution rather than treating stablecoins as just another token category.

## Core conclusions

- Stablecoins are core market infrastructure, not peripheral wrappers around crypto activity.
- Reserve quality and redemption confidence are central to category stability.
- Issuer concentration creates system-level fragility because a few products mediate a large share of settlement flow.
- Stablecoins should be analyzed across payments, trading, regulation, and DeFi rather than from only one angle.

## Main evidence clusters

- reserve backing and asset composition
- redemption mechanics and confidence
- issuer concentration and market share
- chain distribution and DeFi collateral use
- exchange and payment settlement usage
- regulation and banking-system interaction

## Important recurring objects

- issuers and related corporate entities
- reserve assets and custody arrangements
- redemption channels and banking partners
- exchanges and DeFi protocols using stablecoins as settlement or collateral
- regulators and money-transmission authorities

## Important recurring drivers

- liquidity
- regulation
- operational-risk
- trade
- tokenomics

## Common conflicts or failure modes

- treating peg stability as proof of structural safety
- ignoring redemption capacity and banking dependence
- underweighting issuer concentration and collateral concentration
- confusing payment usage, trading usage, and DeFi usage as if they implied the same durability

## Missing coverage

- stronger issuer-specific reserve and redemption notes
- better chain-distribution and settlement-flow tracking
- clearer source hierarchy for reserve attestations versus market commentary
- more explicit links between stablecoin regimes and exchange / DeFi dependence

## Most fragile assumptions

- that a stablecoin is safe if the price looks stable most of the time
- that reserves are equally liquid and reliable under stress
- that regulatory treatment will converge cleanly across jurisdictions

## Recommended next research steps

- keep issuer-specific incidents and policy developments in `40-research/`
- use this note for stable structural orientation around settlement, collateral, and reserve systems
- deepen substructure only where repeated retrieval demand justifies issuer- or chain-specific breakdowns
