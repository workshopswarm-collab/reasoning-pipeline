---
type: evidence_map
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
research_run_id: 145d8deb-fe30-4690-9512-123c43ccf99c
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: "Netting current above-threshold context against exact-noon close risk"
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-risk-manager-binance-spot-context.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/assumptions/risk-manager.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "exact-close-risk", "polymarket"]
---

# Summary

The evidence leans Yes because the governing venue currently has BTC/USDT materially above 74000, but the main risk-manager objection is that this is a single exact future minute close market, so timing/path risk is doing most of the work against a more bullish estimate.

## Question being evaluated

Will Binance BTC/USDT's 1-minute candle labeled 12:00 ET on April 17 have a final close above 74000?

## Current lean

Lean Yes, but with moderate confidence and a somewhat lower estimate than the market because exact-time close risk looks meaningfully underpriced.

## Prior / starting view

Starting baseline was the market-implied probability around 71-73%.

## Evidence supporting the claim

- Binance BTC/USDT current price is around 74912 on the governing venue and pair.
  - Source: Binance API source note.
  - Why it matters: the asset is already above the threshold, so no fresh breakout is required.
  - Direct or indirect: direct contextual evidence on the governing venue, but not direct evidence of the resolving minute.
  - Weight: high.

- Recent Binance 1-minute closes sit in the upper 74800s to low 74900s.
  - Source: Binance API source note.
  - Why it matters: recent microstructure is above the strike, not barely touching it.
  - Direct or indirect: direct contextual evidence.
  - Weight: medium-high.

- Polymarket itself prices the 74000 contract in the low 70s.
  - Source: Polymarket rules source note / assignment context.
  - Why it matters: the broader market also reads current conditions as favoring Yes.
  - Direct or indirect: indirect contextual evidence.
  - Weight: medium.

## Evidence against the claim

- The contract is not about current spot or any time above 74000; it is about one exact future 12:00 ET 1-minute close.
  - Source: Polymarket rules source note.
  - Why it matters causally: a modest overnight or morning drawdown can flip the result even if BTC spends much of the period above the strike.
  - Direct or indirect: direct contract evidence.
  - Weight: high.

- The current buffer above 74000 is only about 900 points, roughly 1.2%.
  - Source: netting of current Binance price against the strike.
  - Why it matters causally: BTC can move that much well within a sub-day window.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.

- Cross-exchange spot checks (CoinGecko about 74990, Coinbase spot about 74913.725) broadly agree on level, but they do not reduce governing-source timing risk much because only Binance BTC/USDT at the exact minute counts.
  - Source: external API checks.
  - Why it matters causally: the main uncertainty is not venue disagreement now; it is path into the resolving minute.
  - Direct or indirect: contextual evidence.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market price itself is supportive but may also reflect crowd overconfidence in generic spot-above-threshold logic.
- The lack of current source conflict is good, but that mostly removes one class of risk rather than proving the future minute close.

## Conflict between inputs

There is little factual conflict. The main tension is weighting-based: how much current above-threshold spot should translate into the exact noon ET close probability.

## Key assumptions

- The current above-threshold state on Binance will broadly persist into noon ET April 17.
- No material overnight or morning selloff breaks the current cushion.
- The ET-to-Binance candle mapping will be straightforward at resolution time.

## Key uncertainties

- Intraday BTC volatility between now and the resolving minute.
- Whether the current cushion is large enough for a close-only market.
- Whether any new macro or crypto-specific shock arrives before noon ET.

## Disconfirming signals to watch

- BTC/USDT loses 74000 on Binance before the morning of April 17.
- The pair trades around 74000 shortly before noon ET, making the result nearly coin-flip.
- Venue-specific weakness on Binance relative to other spot references.

## What would increase confidence

- Fresh Binance checks closer to the resolving window still showing a stable buffer above 74000.
- Evidence that the 12:00 ET mapping corresponds cleanly to a specific Binance UTC candle without ambiguity.
- Continued price action above 74500-75000 into late morning ET.

## Net update logic

What mattered most was that the correct venue and pair are already above the strike by a nontrivial margin. What kept the estimate from matching or exceeding the market is that the contract is narrow: only one future minute close matters. So I upweight current Binance context but downweight generic bullish inference because timing/path risk remains the dominant failure mode.

## Suggested downstream use

Use this as direct input for forecast update and Orchestrator synthesis, with emphasis on the distinction between supportive current-level evidence and unresolved exact-close timing risk.
