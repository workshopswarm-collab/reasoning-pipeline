---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: markets
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: Polymarket market page
source_type: market page / contract page
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413-600f720f-20260413T233138Z/personas/base-rate.md]
tags: [polymarket, contract, source-note]
---

# Summary

This source establishes the live market framing and provides the governing contract surface, but the fetched readable page did not expose the detailed rules text directly. The assignment context provides the relevant market metadata including title, slug, close time, and current price of 0.75 for the threshold question "Will Bitcoin reach $76,000 April 13-19?"

## Key facts extracted

- Market title: "Will Bitcoin reach $76,000 April 13-19?"
- Current price in assignment context: 0.75, implying roughly 75% market probability.
- Primary market URL is the Polymarket event page.
- The page confirms this is a multi-outcome weekly BTC price-hit market and says the formal rules live in the page's Rules section.
- The fetched page content warns users to review the rules carefully, which reinforces that Polymarket's own rule text is the governing contract surface even though the readable extractor did not expose the full rule body.

## Evidence directly stated by source

- The event exists at the given Polymarket URL.
- Resolution criteria are said to be defined in the Rules section on that page.
- The market is a weekly "what price will Bitcoin hit" contract.

## What is uncertain

- The exact settlement source text was not retrievable from the public readable fetch.
- The exact exchange/index reference for the weekly high is therefore not independently visible from this fetch alone.
- Because of that, source-of-truth ambiguity is not zero even though the market is operationally straightforward.

## Why this source may matter

This is the primary contract surface and the source of the market-implied probability baseline. It anchors both the interpretation of the question and the resolution mechanics.

## Possible impact on the question

If Polymarket defines "reach" in the standard way for its weekly price-hit markets, the relevant condition is whether the governing BTC/USD source prints at or above $76,000 at any point during the specified window. That makes observed market highs and source-of-truth clarity the key factual inputs.

## Reliability notes

Useful as the primary contract surface, but only medium reliability for detailed rule interpretation here because the accessible fetch did not expose the full Rules text or the underlying settlement source explicitly.