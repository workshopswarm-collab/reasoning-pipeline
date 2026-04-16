---
artifact_type: source_note
source_type: primary_and_context
persona: catalyst-hunter
case_key: case-20260413-600f720f
title: Polymarket BTC $76k Apr 13-19 market page plus spot-price context check
source_date: 2026-04-13
source_urls:
  - https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
  - https://www.coingecko.com/en/coins/bitcoin
entity:
  - btc
related_entities:
  - bitcoin
driver: []
related_drivers: []
proposed_entities: []
proposed_drivers:
  - bitcoin-spot-price-momentum
---

# Summary
The Polymarket market is a date-bounded threshold question: whether Bitcoin reaches $76,000 during Apr 13-19. The useful primary-source facts are the current market price (~0.75 from assignment context) and the market framing itself. The market page did not yield a clearly machine-readable explicit resolution source in lightweight fetch, so governing source-of-truth remains somewhat ambiguous and should be flagged in the main finding. A contextual source check from CoinGecko indicated Bitcoin spot was materially below $76,000 on Apr 13, implying the contract depends on a meaningful upside move during the resolution window rather than already being effectively settled.

# Key extracted facts
- Assignment current_price is 0.75, so market-implied probability is 75%.
- Market title: "Will Bitcoin reach $76,000 April 13-19?"
- CoinGecko context check showed BTC spot below $76,000 at time of review, so threshold had not already obviously been crossed when reviewed.
- The case is mostly about path and catalyst timing over a short window, not long-run Bitcoin fundamentals.

# Source quality notes
- Primary source quality: moderate. Polymarket is primary for contract framing and market-implied probability, but the exact settlement source was not fully legible from the lightweight page extraction.
- Context source quality: moderate. CoinGecko is a strong market-data aggregator for confirming broad spot-price context, but not necessarily the contract’s governing settlement source.
- Independence: partial. These sources are independent in function (contract venue vs market-data context), though neither alone resolves the short-window crossing question prospectively.

# Why this matters
This establishes that the market was not trivially settled and that any bullish view must rely on near-term catalysts or momentum continuation sufficient to push BTC up to the threshold within the specified week.

# Limits
I did not obtain a definitive explicit settlement-feed citation from the Polymarket page via lightweight extraction, so contract-source ambiguity remains an audit point for the main note.