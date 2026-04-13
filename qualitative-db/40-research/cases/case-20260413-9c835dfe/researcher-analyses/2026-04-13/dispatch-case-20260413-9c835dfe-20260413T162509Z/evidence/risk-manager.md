---
type: evidence_map
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: d9988cce-3672-4953-b04c-0077f20b7784
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: corporate-treasury
entity: bitcoin
topic: will-microstrategy-strategy-announce-a-purchase-of-more-than-1000-btc-between-april-7-and-april-13-2026-et
question: "Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 ET?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["strategy-company"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing", "resolution-risk"]
---

# Summary

The case leans Yes, but the only meaningful residual risk is not whether Strategy likes buying BTC; it is whether a qualifying official announcement exists inside the exact contract window and from the accepted source class.

## Question being evaluated

Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 ET?

## Current lean

Lean Yes, with residual contract-mechanics/timing tail risk.

## Prior / starting view

Starting view was that a 96% market price was probably directionally right, but too extreme unless the official announcement could be verified cleanly.

## Evidence supporting the claim

- Official Strategy purchases page exists on the current company domain and is the reference surface cited in the market description.
  - Source: `2026-04-13-risk-manager-strategy-purchases-page.md`
  - Why it matters: confirms authoritative source path and clean company-domain mapping.
  - Direct or indirect: indirect on the event, direct on source-of-truth.
  - Weight: medium.

- Market rules specify resolution from official MicroStrategy/Strategy or Michael Saylor information, and these weekly treasury-announcement markets commonly track recurring corporate disclosure behavior.
  - Source: `2026-04-13-risk-manager-polymarket-rules-page.md`
  - Why it matters: helps explain why market confidence is very high.
  - Direct or indirect: direct on contract mechanics, indirect on event probability.
  - Weight: medium.

## Evidence against the claim

- The available run environment did not expose a clean official announcement text or dynamic purchases-table entry for the specific April 7-13 event.
  - Source: source-note limitations in both notes.
  - Why it matters: prevents a fully settled risk-free Yes judgment.
  - Direct or indirect: direct on verification quality.
  - Weight: high.

- Narrow date-window announcement markets can fail on timing, wording, or source attribution even if underlying purchases occurred.
  - Source: market rules interpretation.
  - Why it matters: this is the main tail risk being underpriced by an extreme market.
  - Direct or indirect: direct on resolution mechanics.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- The Polymarket page extraction showed effectively 100% Yes, while assignment metadata gave a 0.96 current price. The difference is not decision-changing, but it is a reminder to trust assignment snapshot pricing over rounded web extraction.

## Conflict between inputs

There is no strong factual conflict among inputs. The main issue is evidence depth: official-source legitimacy is clear, but direct event verification in this environment remained incomplete.

## Key assumptions

- Strategy or Michael Saylor has already made, or will make before cutoff, a qualifying announcement.
- No hidden wording/timing wrinkle disqualifies what market participants appear to expect.

## Key uncertainties

- Whether a specific qualifying announcement text is already public and simply not visible through the available page extraction.
- Whether the exact threshold (>1000 BTC) is satisfied in the official announcement.

## Disconfirming signals to watch

- No official post by end of April 13 ET.
- Official post references holdings without a qualifying purchase announcement.
- Third-party references cannot be tied back to Strategy/Saylor.

## What would increase confidence

- Direct access to the full Strategy purchases table/body content showing the specific dated purchase.
- A visible Michael Saylor or Strategy corporate post explicitly announcing the >1000 BTC purchase within the window.

## Net update logic

The evidence kept the direction as Yes because the contract points to a well-defined official source ecosystem and the market is pricing a routine weekly-announcement pattern. But the lack of clean direct-event extraction kept me from matching the market's near-certainty; the residual discount is almost entirely timing/verification risk, not a broad directional disagreement about Strategy's BTC-buying behavior.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review with emphasis that residual downside is contract mechanics, not macro/Bitcoin thesis.
