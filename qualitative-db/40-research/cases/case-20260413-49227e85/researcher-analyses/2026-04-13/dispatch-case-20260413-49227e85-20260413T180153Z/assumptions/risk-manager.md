---
type: assumption_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
research_run_id: fe620ff5-0f3f-4111-a396-f7d111a57171
analysis_date: 2026-04-13
persona: risk-manager
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: deepseek-v4-release-status
question: "DeepSeek V4 released by April 15?"
driver: operational-risk
date_created: 2026-04-13
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: []
related_drivers: ["operational-risk", "reliability", "product-launches"]
proposed_entities: ["DeepSeek"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["timing-assumption", "public-availability", "release-criteria"]
---

# Assumption

If DeepSeek had actually made V4 available to the general public in a way that satisfies this contract, there would likely already be a clear first-party public announcement or public-access surface visible by 2026-04-13.

## Why this assumption matters

The market is highly date-sensitive and sits at a high implied probability. My NO-lean depends less on proving a launch cannot occur and more on judging that the absence of first-party public availability evidence this close to deadline is meaningful negative information.

## What this assumption supports

- A probability estimate below the market-implied baseline.
- The view that rumor, leaks, or private testing do not satisfy the contract.
- The interpretation that path risk is underpriced.

## Evidence or logic behind the assumption

- DeepSeek's official API docs still present V3.2 rather than V4.
- Recent independent reporting says V4 is still "nowhere in sight" as of 2026-04-12.
- The contract requires public accessibility and a clear public announcement from DeepSeek, not merely rumors or closed access.

## What would falsify it

- A dated DeepSeek first-party announcement naming V4 (or the next DeepSeek V successor) and making it publicly accessible before the deadline.
- A public open beta, public rolling waitlist, or universally accessible product page clearly launched by DeepSeek before the cutoff.

## Early warning signs

- A new official DeepSeek blog, docs page, API model listing, or app notice naming V4.
- Credible reporting that includes screenshots or direct evidence of public sign-up availability.
- Public waitlist or beta links that any user can access without private invitation.

## What changes if this assumption fails

The probability should move sharply upward, likely above market if the first-party evidence is clear and timely enough, because the contract is mostly bottlenecked by public-access and announcement criteria rather than technical quality.

## Notes that depend on this assumption

- Main finding at `personas/risk-manager.md`
- Evidence map at `evidence/risk-manager.md`