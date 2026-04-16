---
type: evidence_map
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 5003c593-4325-43a8-b5af-de4b229c1c65
analysis_date: 2026-04-13
persona: variant-view
domain: politics
subdomain: bulgarian-parliamentary-election
entity:
topic: "GERB second-place likelihood under emerging first-place challenger"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["progressive-bulgaria", "pp-db-vs-db-ballot-taxonomy"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["second-place", "polling", "taxonomy-risk", "source-of-truth"]
---

# Summary

The netted evidence supports GERB as the most likely second-place finisher, but the confidence should be slightly below the market's extreme pricing because the challenger field and ballot taxonomy remain imperfectly verified.

## Question being evaluated

Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?

## Current lean

Yes, probably. GERB appears very likely to remain top-two and there is a plausible non-consensus path where it specifically finishes second behind a new anti-establishment / Radev-aligned vehicle rather than first.

## Prior / starting view

Starting view from the market price was that the market had near-settled on GERB second as the obvious answer. Variant-view task was to test whether that confidence rested on stale consensus or on a real mechanism.

## Evidence supporting the claim

- PolitPro poll trend shows PB first at 30.8% and GERB second at 20.7%, with DB 10.9%, DPS 10.0%, and Revival 7.0%.
  - Source: `researcher-source-notes/2026-04-13-variant-view-politpro-poll-trend.md`
  - Why it matters: directly presents the core mechanism for GERB second rather than first.
  - Type: indirect but highly relevant contextual polling evidence.
  - Weight: high.

- Wikipedia election page shows current-seat baseline of GERB 66, PP-DB 36, Revival 33, DPS 29, BSP-OL 19, APS 17, ITN 17, MECh 11, Velichie 10, PB 0, and confirms the election date as 19 April 2026.
  - Source: `researcher-source-notes/2026-04-13-variant-view-wikipedia-election-page.md`
  - Why it matters: confirms a fragmented field where GERB starts from a strong structural position; also confirms timing.
  - Type: contextual field-structure evidence.
  - Weight: medium.

- POLITICO context page keeps GERB in the low-20s and ahead of PP-DB and DPS in the mid-teens.
  - Source: `researcher-source-notes/2026-04-13-variant-view-politico-poll-of-polls.md`
  - Why it matters: independent cross-check that GERB remains clearly competitive for top-two.
  - Type: indirect contextual evidence.
  - Weight: medium.

## Evidence against the claim

- Source-of-truth ambiguity remains before votes are actually counted. The market resolves by seats, with tie-breaks by votes, and falls back to the Bulgarian CEC if consensus reporting is ambiguous.
  - Why it matters: polling-based confidence can still be misplaced if seat conversion or label mapping surprises.
  - Type: contract / settlement risk.
  - Weight: medium.

- Poll taxonomy risk around PB versus PP-DB versus DB is not cleanly resolved in the sources gathered.
  - Why it matters: if these labels are overlapping, split inconsistently, or not ballot-valid in the way aggregators imply, confidence in GERB-specific second place should be lower.
  - Type: interpretive / mapping risk.
  - Weight: high.

- The official CIK site could not be directly fetched in this environment due to 403 blocks, so direct commission verification of the ballot list was incomplete.
  - Why it matters: weakens confidence relative to a clean official-source pass.
  - Type: verification gap.
  - Weight: medium.

## Ambiguous or mixed evidence

- Wikipedia includes PB as a contesting actor, which supports the variant mechanism, but Wikipedia is not authoritative.
- POLITICO's page is independently useful but may not be optimized for the exact domestic coalition labels relevant to this market.

## Conflict between inputs

The main conflict is not factual disagreement on GERB being a major actor; it is interpretive disagreement over whether the polling frame genuinely supports a clean PB-first / GERB-second structure under the exact ballot labels the market will use. This is mostly a taxonomy-based and source-of-truth-based conflict.

## Key assumptions

- PB is a real, separately meaningful ballot actor in the way recent reporting implies.
- GERB remains structurally above the old opposition pack even if it loses first place.
- Consensus reporting, if used before official final tallies, will still rank GERB second rather than collapsing labels in a way that changes the ordering.

## Key uncertainties

- Exact official ballot taxonomy.
- Whether recent aggregators are overfitting thin or low-quality underlying data.
- Whether seat conversion, not just vote share, could create a surprise rank order.

## Disconfirming signals to watch

- Direct official or broad consensus reporting showing GERB third or worse.
- Final independent polling average with GERB in the same band as PP-DB/DB or DPS.
- Clarification that PB is misclassified or not relevant to the market's ranking options.

## What would increase confidence

- Clean CIK access confirming the registered ballot actors and official reporting process.
- A second strong domestic polling aggregator showing the same PB-first / GERB-second structure.
- Late pre-election consensus reporting that GERB is firmly top-two across major outlets.

## Net update logic

The variant mechanism mattered most: the strongest reason the market may be right is not that GERB is dominant, but that the anti-GERB side may be reorganizing around a new frontrunner while the remaining opposition fragments stay below GERB. I downweighted pure headline consensus because the source-of-truth layer was not fully accessible and label mapping remains messy. That leaves a high but not near-certain yes.

## Suggested downstream use

Use as an orchestrator synthesis input with explicit emphasis on taxonomy risk and official-source verification needs at resolution time.