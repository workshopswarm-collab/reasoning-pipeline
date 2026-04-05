---
type: domain_overview
domain: crypto
subdomain: exchanges
topic: crypto exchange research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs: []
downstream_uses: []
related_entities: []
related_drivers: [liquidity, regulation, operational-risk]
tags: [domain/crypto, subdomain/exchanges, overview]
---

# Overview summary

Crypto exchanges are the access-and-market-plumbing subdomain of crypto: trading venues, custody, fiat rails, listing power, settlement flow, and withdrawal rights. They deserve a standalone overview because exchange structure is one of the clearest chokepoints between crypto-native activity and the broader financial system.

## Why this subdomain matters

This subdomain matters because a large share of crypto market behavior is mediated through exchange concentration, custody terms, regulatory exposure, and access to fiat and stablecoin liquidity. Researchers need a structural note for venue power and market plumbing rather than treating exchanges as interchangeable trading interfaces.

## Core conclusions

- Exchanges are not just marketplaces; they are custody, access, and liquidity infrastructure.
- Withdrawal rights and reserve confidence matter as much as nominal trading access.
- Listing power, market concentration, and jurisdictional exposure can reshape asset behavior across the sector.
- Exchange risk often propagates faster than protocol-level changes because it sits closer to user access and market liquidity.

## Main evidence clusters

- trading liquidity and market concentration
- custody and withdrawal structure
- fiat rails and banking access
- stablecoin integration and settlement flow
- regulatory exposure and jurisdictional risk
- listing, delisting, and market-access decisions

## Important recurring objects

- centralized exchanges
- broker and custody platforms
- banking partners and payment rails
- stablecoin issuers and settlement partners
- market makers and liquidity providers
- regulators and compliance authorities

## Important recurring drivers

- liquidity
- regulation
- operational-risk
- sentiment

## Common conflicts or failure modes

- treating reported volume as equivalent to durable market quality
- ignoring custody concentration and withdrawal risk
- assuming venue access is uniform across jurisdictions
- reading exchange-specific distress as isolated when the venue is systemically connected

## Missing coverage

- better venue-quality and market-depth comparison notes
- stronger banking and fiat-access source maps
- clearer treatment of proof-of-reserves limits and custody opacity
- more explicit linkage between exchange concentration and asset-level fragility

## Most fragile assumptions

- that exchange liquidity is stable under stress
- that users can always move assets freely across venues and chains
- that regulatory actions against major venues remain local rather than systemic

## Recommended next research steps

- keep venue-specific incidents and legal actions in `40-research/`
- use this note for exchange-structure orientation rather than rolling company news
- deepen substructure only where repeated retrieval demand justifies exchange-type or region-specific breakdowns
