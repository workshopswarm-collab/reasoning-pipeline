---
type: source_note
case_key: case-20260415-d129d0ec
dispatch_id: dispatch-case-20260415-d129d0ec-20260415T014044Z
analysis_date: 2026-04-15
persona: risk-manager
domain: geopolitics
subdomain: prediction-market-resolution
entity: ukraine
topic: russia-military-action-against-kyiv-municipality-by-april-17
question: What exactly counts for this market and what source-of-truth logic governs resolution?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market-contract
source_url: https://polymarket.com/event/russia-military-action-against-kyiv-municipality-by-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: Orchestrator
related_entities: [ukraine, russia]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-d129d0ec/researcher-analyses/2026-04-15/dispatch-case-20260415-d129d0ec-20260415T014044Z/personas/risk-manager.md]
tags: [market-rules, resolution, source-of-truth, kyiv]
---

# Summary

The market is narrower than a generic "attack on Kyiv" headline. It requires a Russian-initiated drone, missile, or air strike directed at **Kyiv municipality** within the specified window, with explicit inclusions and exclusions.

## Key facts extracted

- Qualifying action: aerial bombs, drones, or missiles launched by Russian Armed Forces on Kyiv municipality's ground territory.
- Surface-to-air missiles are explicitly excluded.
- Artillery, small arms, FPV/ATGM strikes, ground incursions, naval shelling, cyberattacks, and similar non-listed operations do not count.
- Intercepted missiles/drones can still count if they constitute a strike against Kyiv municipality during the timeframe, even if they do not land there or cause damage.
- A strike anywhere within the terrestrial territory of Kyiv municipality counts.
- Primary source of truth: consensus credible reporting from major international media and national broadcasters/newspapers.
- Fallback in ambiguity: official statements from the Ukrainian Air Force and Ukrainian government authorities, including Kyiv City State Administration and the Mayor of Kyiv.
- If the date/time cannot be confirmed by consensus of credible reporting by the end of the third calendar date after the window, the market resolves No even if later confirmation appears.

## Evidence directly stated by source

The contract text itself directly defines inclusion/exclusion and hierarchy of sources.

## What is uncertain

- "Kyiv municipality" can be misread in news coverage as broader Kyiv region/oblast or metro area unless the reporting is specific.
- Consensus reporting may lag real events, which matters because the contract has an explicit late-confirmation cutoff.

## Why this source may matter

This source governs the entire interpretation. A market view can be directionally wrong if it treats any Ukraine-wide drone event, any Kyiv-oblast event, or any air alert as sufficient.

## Possible impact on the question

The rules increase downside risk to overconfident Yes pricing because multiple conditions must all hold: Russian aerial strike type, directed at Kyiv municipality, within window, and confirmable via the specified source hierarchy.

## Reliability notes

This is the governing contract text and therefore the highest-authority interpretive source for what counts.