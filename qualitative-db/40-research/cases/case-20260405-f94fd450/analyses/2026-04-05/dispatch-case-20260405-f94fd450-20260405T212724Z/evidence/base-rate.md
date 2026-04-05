---
type: evidence_map
case_key: case-20260405-f94fd450
dispatch_id: dispatch-case-20260405-f94fd450-20260405T212724Z
research_run_id: 60b08e4e-34dc-4e1c-8bb2-180411cf9154
analysis_date: 2026-04-05
persona: base-rate
domain: geopolitics
subdomain: conflict-resolution
entity: Iran-UAE
topic: case-20260405-f94fd450 | base-rate
question: Will Iran strike UAE again in March?
driver: rule-sensitive settlement audit
date_created: 2026-04-05
agent: Orchestrator
status: complete
confidence: medium-high
conflict_status: low factual conflict, moderate rule-interpretation sensitivity
action_relevance: high
related_entities: [Iran, UAE, Fujairah, Dubai airport]
related_drivers: [resolution mechanics, attribution threshold, timing window, base-rate rarity]
upstream_inputs: []
downstream_uses: [agent finding]
tags: [evidence-map, high-difficulty, geopolitics, resolution-audit]
---

# Summary

The net evidence strongly favors **Yes** because credible reporting indicates actual Iranian drone impacts on UAE soil in March, not merely interceptions, and separate reporting ties the March attacks directly to launches from Iran. The main audit sensitivity is contractual: only impacts count, proxies do not, and timing/origin must be consensus-confirmable.

## Question being evaluated

Whether Iran initiated a qualifying drone, missile, or air strike on UAE soil or an official UAE diplomatic site within the March 2026 ET window, under the market’s exclusions.

## Current lean

Lean yes, with very high probability that the correct settlement is yes.

## Prior / starting view

Outside-view prior before checking case-specific evidence: genuine state-on-state Iranian strikes on UAE soil are rare, and many reported March incidents were likely interceptions that would not count. So the base-rate starting view was meaningfully below the market unless a clean impact and attribution record existed.

## Evidence supporting the claim

- **Polymarket rules note** (`source-notes/2026-04-05-base-rate-polymarket-rules.md`)
  - Why it matters: defines the hurdle precisely; a single confirmed impact on UAE territory from Iranian military forces is enough.
  - Direct or indirect: direct on mechanics, not event occurrence.
  - Weight: very high for interpretation.
- **BBC impact reporting** (`source-notes/2026-04-05-base-rate-bbc-uae-impacts.md`)
  - Why it matters: reports drone attacks causing fires at Fujairah oil facilities and a drone-related incident near Dubai airport on 16 March.
  - Direct or indirect: direct on qualifying impact to UAE territory/infrastructure.
  - Weight: very high.
- **Khaleej Times / The National series** (`source-notes/2026-04-05-base-rate-uae-reporting-march-series.md`)
  - Why it matters: repeatedly attributes launches to Iran / from Iran, satisfying the contract’s origin requirement better than BBC alone.
  - Direct or indirect: direct on attribution/origin; mixed on qualifying impact.
  - Weight: high.

## Evidence against the claim

- The contract excludes interceptions, and much of the March reporting consists of intercepted missiles/drones rather than successful impacts.
  - Why it matters: if all widely corroborated March UAE incidents were only interceptions, the market should resolve no despite heavy attempted attack volume.
  - Direct or indirect: direct contractual counterpoint.
  - Weight: medium.
- Some available reports are local or outlet-summarized rather than a single obvious authoritative settlement source.
  - Why it matters: consensus-of-credible-reporting language can create residual ambiguity around which exact incidents count.
  - Direct or indirect: indirect / audit risk.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- The National’s report of an apparent Iranian drone strike on a Kuwaiti tanker anchored off Dubai is directionally supportive, but legally/resolution-wise less clean than Fujairah infrastructure because the object struck was not itself UAE state property.
- Dubai airport reporting references a “drone-related incident”; that is supportive but slightly less crisp than the Fujairah infrastructure hit.

## Conflict between inputs

No major factual conflict found. The main issue is weighting and interpretation: some sources emphasize interceptions, while BBC provides the clearest statement of actual impacts. What would resolve any residual doubt would be a direct official UAE statement explicitly confirming Iranian impacts on UAE territory on the relevant dates.

## Key assumptions

- BBC’s reported Fujairah and Dubai incidents are part of the same Iran-origin attack campaign described by UAE-focused reporting, not separate unattributed events.
- Consensus of credible reporting does not require identical wording across outlets so long as multiple credible reports support timing, attribution, and impact.

## Key uncertainties

- Whether final settlement reviewers require especially explicit wording tying the impact event itself, not just the campaign, to Iranian military forces originating from Iranian territory.
- Whether any reviewer treats the airport incident wording as too indirect and relies mainly on Fujairah.

## Disconfirming signals to watch

- Credible reporting or settlement commentary saying all March UAE incidents were intercepted and no confirmed Iranian munition actually impacted UAE territory.
- A convincing attribution dispute showing the impact events were not confirmed to originate from Iran proper.

## What would increase confidence

- A direct UAE Defence Ministry or WAM statement saying Iranian drones/missiles hit Fujairah or Dubai infrastructure on specified March dates.
- A Reuters/AP style synthesis explicitly stating that Iranian strikes impacted UAE territory, not merely that launches were attempted.

## Net update logic

The starting base-rate skepticism was overcome because the issue is not whether Iran usually strikes UAE soil, but whether it already did so within the window. Once BBC provided clear impact reporting and UAE-focused outlets separately confirmed Iran-origin launches through March, the remaining uncertainty became rule-audit rather than event plausibility. That moved the estimate from a low prior to a very high yes probability.

## Suggested downstream use

Use as orchestrator synthesis input and settlement-audit support. Main practical use is to justify why a base-rate prior should be overridden here: rare event base rate lost to direct qualifying-event evidence.
