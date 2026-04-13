---
type: evidence_map
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
research_run_id: 549c76b8-37f0-48ab-b0c9-c37ef8e5992d
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: ai-model-releases
entity:
topic: "DeepSeek V4 released by contract deadline?"
question: "Will the next major DeepSeek V model be publicly accessible and clearly announced by DeepSeek by the contract deadline?"
driver: product-launches
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: limited-public-conflict
action_relevance: high
related_entities: []
related_drivers: ["product-launches", "operational-risk", "reliability", "media-narratives"]
proposed_entities: ["DeepSeek"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-36f15d57/researcher-analyses/2026-04-13/dispatch-case-20260413-36f15d57-20260413T175211Z/personas/base-rate.md"]
tags: ["evidence-map", "deepseek-v4", "release-audit"]
---

# Summary

The current lean is No / below-market Yes, mainly because the available evidence points to near-term possibility and active development, but not yet to a qualifying public launch under the contract's narrow wording.

## Question being evaluated

Will the next major DeepSeek V model be made available to the general public by the deadline, with a clear official DeepSeek announcement and public accessibility sufficient to satisfy the contract?

## Current lean

Lean No relative to market pricing; estimated Yes probability 35%.

## Prior / starting view

Starting outside-view prior was below 30% because major frontier-model flagship launches in a short, date-specific window are relatively uncommon, and contracts requiring public accessibility plus official announcement add friction.

## Evidence supporting the claim

- Recent TechNode report says V4 may launch this month and describes gray-test interface evidence showing new modes including Expert and Vision.
  - Source: `2026-04-13-base-rate-reporting-rumors.md`
  - Why it matters: suggests launch work is advanced and not purely speculative.
  - Direct or indirect: indirect for contract resolution; direct only for market expectations and product-prep state.
  - Weight: medium.
- Google News feed shows multiple outlets, including Reuters, discussing DeepSeek V4 and launch timing.
  - Source: `2026-04-13-base-rate-reporting-rumors.md`
  - Why it matters: independent press attention makes V4 development more credible than a single isolated rumor.
  - Direct or indirect: indirect.
  - Weight: low-to-medium.
- DeepSeek has an active official GitHub org and a pattern of public artifact releases, which makes eventual public release plausible.
  - Source: `2026-04-13-base-rate-official-surfaces.md`
  - Why it matters: shows DeepSeek is capable of public-facing releases rather than only private deployment.
  - Direct or indirect: contextual.
  - Weight: low.

## Evidence against the claim

- Official/public DeepSeek surfaces checked on 2026-04-13 do not yet show a clear V4 flagship announcement or public access path.
  - Source: `2026-04-13-base-rate-official-surfaces.md`
  - Why it matters causally: official confirmation/public access is the primary settlement path and is required by the contract.
  - Direct or indirect: direct for current non-confirmation state.
  - Weight: high.
- The contract excludes closed beta, private access, derivative naming, and preview/non-flagship releases.
  - Source: Polymarket market page text checked 2026-04-13.
  - Why it matters causally: many rumor-consistent outcomes still would not count.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.
- Secondary reporting is mostly rumor, screenshots, and expectation framing rather than hard evidence of general-public availability.
  - Source: `2026-04-13-base-rate-reporting-rumors.md`
  - Why it matters causally: reduces how much the market should move from prior.
  - Direct or indirect: direct on source quality.
  - Weight: medium-high.
- Remaining time to the stated April 15 ET deadline is short.
  - Source: assignment + session time check.
  - Why it matters causally: launch slippage risk is large in short windows.
  - Direct or indirect: direct timing constraint.
  - Weight: high.

## Ambiguous or mixed evidence

- Hugging Face visibility of V3.2-family items indicates DeepSeek may use intermediate naming conventions rather than jump directly to a clean flagship V4 release. This could either mean V4 is close or that the path to a qualifying release is less straightforward.
- GitHub absence of V4 is suggestive but not conclusive, since DeepSeek could release primarily through web/app/API.

## Conflict between inputs

The main disagreement is not factual but weighting-based:
- Bullish inputs interpret leaks and press attention as strong evidence of imminent launch.
- Bearish/base-rate interpretation treats those as insufficient because the contract is narrower than "coming soon" and the remaining time window is short.
What would resolve it: an official DeepSeek announcement plus confirmed general-public access.

## Key assumptions

- The market has overweighted imminence headlines relative to qualification risk.
- No hidden near-complete public rollout is already live but undiscovered on checked official surfaces.

## Key uncertainties

- Whether DeepSeek intends a broad public launch within days.
- Whether an open rolling waitlist or open beta would be used and clearly announced in qualifying fashion.
- Whether later reporting sources are genuinely independent or echo the same leak chain.

## Disconfirming signals to watch

- Official DeepSeek website/app/API naming V4 or V5 as successor to V3.
- Public signup/waitlist/open beta with broad access.
- Multiple credible outlets confirming general-public access rather than test/gray release.

## What would increase confidence

- A direct official DeepSeek announcement page.
- A public accessible product page or sign-up flow.
- Independent consensus reporting confirming the access is public and qualifies.

## Net update logic

I started from a skeptical outside view because narrow, date-specific flagship release contracts usually deserve more caution than rumor-driven markets give them. Recent reporting moved me up from a low prior because there is genuine smoke around V4. But the biggest weight remains on official non-confirmation, qualification friction, and the short remaining time window. That leaves a meaningful Yes chance, just well below the market.

## Suggested downstream use

Use this as an orchestrator synthesis input emphasizing contract qualification risk, timing friction, and the difference between "imminent" and "qualifying public release."