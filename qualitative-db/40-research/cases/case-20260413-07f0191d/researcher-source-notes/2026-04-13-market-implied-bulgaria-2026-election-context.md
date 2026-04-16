---
type: source_note
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: Bulgaria 2026 parliamentary election ranking context
question: Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Wikipedia + POLITICO poll-of-polls + CIK access check
source_type: mixed contextual and resolution-source check
source_url: https://en.wikipedia.org/wiki/2026_Bulgarian_parliamentary_election
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/personas/market-implied.md]
tags: [bulgaria, election, gerb, market-implied, provenance]
---

# Summary

This note preserves the main externally accessible context used to assess whether a 96% market price for GERB-SDS finishing **second** is plausible. The accessible evidence points the other way: GERB-SDS appears to be the leading bloc in available election-context summaries rather than a second-place candidate.

## Key facts extracted

- The market description says the election is scheduled for **19 April 2026** and resolves by seats won, with vote totals and then alphabetical order used as tie-breakers.
- The market description also names the **Bulgarian Central Election Commission (CIK)** as the official fallback source if credible-reporting consensus is ambiguous.
- The accessible Wikipedia election page states the 2026 Bulgarian parliamentary election is scheduled for **19 April 2026**.
- That same page lists **GERB-SDS** as having been the largest parliamentary force from the prior election context and presents the 2026 contest around GERB-SDS as a lead contender, not an obvious second-place candidate.
- The accessible POLITICO Bulgaria poll/trend page shows GERB-SDS at **23.6%**, ahead of nearby major competitors shown around **14–15%**.
- Direct access to CIK from this environment was blocked by Cloudflare, but the site itself was reachable enough to confirm that CIK is the intended official authority surface.

## Evidence directly stated by source

- Wikipedia directly stated the election date as **19 April 2026**.
- Wikipedia directly listed GERB-SDS among the main parties and showed it with the strongest prior-election seat position in the article excerpt available.
- POLITICO directly displayed GERB-SDS at **23.6%**, with Vazrazhdane/Revival and PP-DB/DPS lower in the mid-teens on the fetched page excerpt.
- The contract directly states CIK is the official government source if consensus reporting is ambiguous.

## What is uncertain

- The fetched POLITICO page is a contextual aggregation surface, not the final election result.
- Wikipedia is not authoritative and may contain errors or vandalism.
- Because CIK was Cloudflare-blocked in this environment, I could not directly inspect the exact official election subpage or registration/results page from the primary source.
- I did not retrieve a fully independent Bulgarian domestic pollster page in this run due tool-access/search limitations, so the contextual polling picture is useful but not as independently triangulated as ideal.

## Why this source may matter

The main question is whether the market price is embedding a view that GERB-SDS is overwhelmingly likely to finish second. The accessible public context instead suggests GERB-SDS is more likely being treated as a first-place party, making a 96% second-place price look inconsistent with the basic public information set.

## Possible impact on the question

If GERB-SDS is publicly viewed as the frontrunner rather than the runner-up, the market price of 0.96 for "finish second" is likely stale, inverted, mislabeled, or otherwise not efficiently reflecting the available public evidence.

## Reliability notes

- Best direct resolution guidance comes from the contract wording naming **CIK** and from the explicit seat-based ranking rules.
- Best contextual competitive evidence in this run comes from the POLITICO poll/trend page.
- Wikipedia is useful for election timing and party-position context but should not be treated as authoritative on its own.
- Overall reliability for directional inference is **medium**, but enough to reject a 96% confidence-in-second-place interpretation absent contrary authoritative evidence.