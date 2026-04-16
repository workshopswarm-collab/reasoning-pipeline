---
type: evidence_map
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
research_run_id: 0f8cbc22-0665-4ff4-9849-ba3df3431a0f
analysis_date: 2026-04-15
persona: base-rate
domain: politics
subdomain: surveillance-law
entity: u-s-congress
topic: "whether Section 702 was already reauthorized by Public Law 118-49"
question: "Will FISA Title VII including Section 702 be reauthorized before it expires?"
driver: legal
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["u-s-congress", "u-s-house-of-representatives", "u-s-senate", "white-house"]
related_drivers: ["legal"]
proposed_entities: []
proposed_drivers: ["congressional-process"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "fisa", "section-702"]
---

# Summary

The evidence net is strongly affirmative because the contract itself points to Public Law 118-49 as qualifying legislation, and official law text plus current codification indicate Section 702 was indeed continued by that law before the operative expiration.

## Question being evaluated

Did legislation reauthorizing FISA Title VII including Section 702 pass both chambers and become law before expiration, in a way that should make this market resolve Yes by April 19, 2026?

## Current lean

Strong lean Yes.

## Prior / starting view

Cold outside-view prior for major surveillance reauthorization before deadline would normally be below certainty because Congress often cuts these close and national-security reforms face meaningful procedural friction.

## Evidence supporting the claim

- The market description explicitly says qualifying legislation includes Public Law 118-49.
  - Source: market contract text.
  - Why it matters causally: if true, much of the event may already be locked in.
  - Direct or indirect: direct rule evidence.
  - Weight: very high.

- Official govinfo public-law text shows Public Law 118-49 was enacted on April 20, 2024 and amends Section 702 / 50 U.S.C. 1881a.
  - Source: researcher-source-notes/2026-04-15-base-rate-public-law-118-49.md
  - Why it matters causally: proves enacted qualifying legislation exists.
  - Direct or indirect: direct official evidence.
  - Weight: very high.

- Current codification of 50 U.S.C. 1881a indicates Section 702 remained in force after the 2024 law.
  - Source: researcher-source-notes/2026-04-15-base-rate-current-codification.md
  - Why it matters causally: supports that this was a real reauthorization, not merely reform language around a lapsed authority.
  - Direct or indirect: strong contextual/legal verification.
  - Weight: high.

- Enrolled bill text for H.R. 7888 corroborates the legislative vehicle and amendment pathway.
  - Source: researcher-source-notes/2026-04-15-base-rate-enrolled-bill-amendment.md
  - Why it matters causally: provides a second official provenance chain from bill to public law.
  - Direct or indirect: direct official corroboration.
  - Weight: medium-high.

## Evidence against the claim

- Congress.gov was not directly accessible in this run because of anti-bot blocking, so the named primary resolution source could not be checked firsthand.
  - Why it matters causally: leaves a small source-of-truth execution gap.
  - Direct or indirect: direct verification limitation.
  - Weight: medium.

- The strongest disconfirming possibility is contract-interpretation risk: if the market were somehow intended to ask about a fresh 2026 reauthorization rather than counting the already-enacted 2024 law, Yes would be less secure.
  - Why it matters causally: would change the reference event.
  - Direct or indirect: interpretive.
  - Weight: medium.

## Ambiguous or mixed evidence

- The exact sunset mechanics are somewhat awkward to surface from raw statute HTML and law text without a cleaner Congress.gov tracker page.
- But that ambiguity appears operational rather than substantive; the available official sources still point the same way.

## Conflict between inputs

There is little factual conflict. The only meaningful tension is between a literal reading of the contract text, which appears already satisfied by Public Law 118-49, and any hypothetical narrower interpretation that would exclude that same law despite explicit contract language.

## Key assumptions

- Public Law 118-49 is resolution-qualifying as the market text says.
- Current codification accurately reflects that Section 702 remained authorized after the 2024 enactment.

## Key uncertainties

- Whether the market operators could impose a narrower settlement interpretation than the quoted contract language suggests.
- Whether Congress.gov would present any materially different sunset framing than the official-law and codified-text sources used here.

## Disconfirming signals to watch

- Any official clarification from Polymarket narrowing what counts.
- Any Congress.gov source showing Public Law 118-49 did not actually extend Title VII in the relevant way.

## What would increase confidence

- Direct successful access to the specific Congress.gov tracker page named in the market rules.
- A resolution-admin note explicitly confirming that Public Law 118-49 satisfies the market.

## Net update logic

The base rate for last-minute congressional reauthorization alone would not justify near-certainty. The reason the estimate moves far above that cold prior is that this does not look like a fresh unresolved legislative race; it looks like a market whose qualifying event was already delivered by 2024 law and reflected in current codification. Once that is recognized, ordinary legislative-friction priors matter much less.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- resolution audit / settlement check