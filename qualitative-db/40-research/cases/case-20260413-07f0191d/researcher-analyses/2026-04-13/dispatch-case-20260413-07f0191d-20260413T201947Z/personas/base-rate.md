---
type: agent_finding
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 5ce06f01-c313-4c0b-8dad-fa0dc11eba92
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: "2026 Bulgarian parliamentary election"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: no
certainty: medium
importance: high
novelty: high
time_horizon: days
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["bulgaria", "gerb-sds", "pp-db", "revival", "dps"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "bulgaria", "parliamentary-election", "second-place", "source-sensitive"]
---

# Claim

GERB-SDS looks much more likely to finish first than second in the 19 April 2026 Bulgarian parliamentary election, so the probability that GERB-UDF (GERB-SDS) finishes exactly second appears low rather than near-certain.

## Market-implied baseline

The market price is 0.96, implying roughly a 96% probability that GERB-UDF (GERB-SDS) finishes second.

## Own probability estimate

I estimate roughly **8%** that GERB-SDS finishes second.

## Agreement or disagreement with market

I **strongly disagree** with the market.

Base-rate and available current context point the other way:
- GERB-SDS was the clear first-place party in the October 2024 parliamentary election.
- The best accessible March-April 2026 polling compilation still shows GERB-SDS leading in projected seats across multiple firms.
- In those polls, the real fight for second is usually among PP-DB, DPS, and sometimes Revival, not GERB-SDS.

A 96% probability for GERB-SDS to finish second would usually require direct evidence that GERB-SDS is consistently running second in seats. I did not find that. Instead, the accessible evidence suggests GERB-SDS is the modal first-place finisher.

## Implication for the question

On an outside-view basis, this contract currently looks mispriced unless there is some hidden market-labeling issue, coalition-mapping issue, or late-breaking evidence not visible in the sources I could verify. If forced to trade only on the research gathered here, I would treat "GERB-SDS finishes second" as a low-probability outcome.

## Key sources used

1. **Primary resolution / contract source (authoritative for what counts):**
   - Polymarket market page and contract text: `https://polymarket.com/event/bulgarian-parliamentary-election-2nd-place`
   - Source note: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-base-rate-polymarket-contract.md`

2. **Key contextual source (secondary, but highly relevant):**
   - Wikipedia election overview and polling compilation: `https://en.wikipedia.org/wiki/2026_Bulgarian_parliamentary_election`
   - Source note: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-base-rate-wikipedia-election-overview.md`

3. **Vault driver context:**
   - `qualitative-db/30-drivers/elections.md`

4. **Supporting provenance artifacts for this run:**
   - Assumption note: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/assumptions/base-rate.md`
   - Evidence map: `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/evidence/base-rate.md`

**Evidence-floor compliance:** I used three meaningful source surfaces for this high-resolution-risk case: (1) the governing contract text, (2) a broad secondary election/polling compilation, and (3) driver/electoral-system context from the vault, plus an explicit additional verification pass using direct fetch / local parsing of the polling table and attempts to access the official CIK site.

## Supporting evidence

The strongest evidence against a GERB-SDS second-place finish is the combined historical-plus-current outside view:

- **Historical baseline:** In the October 2024 election, GERB-SDS finished first with 25.52% and 66 seats; PP-DB, Revival, and DPS were behind it.
- **Recent polling pattern:** The March-April 2026 polling table available on the election page consistently places GERB-SDS first in projected seats. Specific examples:
  - Sova Harris (2-6 Apr 2026): GERB-SDS 55 seats; PP-DB 33; DPS 28; Revival 23.
  - Gallup (20-30 Mar 2026): GERB-SDS 70 seats; PP-DB 33; DPS 32; Revival 20.
  - Alpha Research (19-26 Mar 2026): GERB-SDS 64 seats; PP-DB 33; DPS 29; Revival 21.
  - MarketLinks (17-21 Mar 2026): GERB-SDS 66 seats; PP-DB 40; DPS 31; Revival 16.

For a party to be 96% likely to finish second, I would expect polls showing it clustered near second. The accessible evidence instead shows it as the leading party.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **source-quality fragility**, not a clear substantive counter-signal.

Specifically:
- I was unable to directly access the Bulgarian Central Election Commission site during this run because it returned 403s to fetch attempts.
- The polling evidence came through Wikipedia's compilation page rather than direct pollster releases for each survey.
- If Wikipedia's poll table is stale, erroneous, or mismapped to the current ballot/coalition labels, my estimate could be too low.

I did **not** find a credible direct source saying GERB-SDS is actually the favorite for second rather than first. So the best concrete disconfirming point is that my evidence set is less independent than ideal.

## Resolution or source-of-truth interpretation

What counts:
- The market resolves to the party or coalition winning the **second-greatest number of seats** in the 2026 Bulgarian National Assembly election.
- Ranking is by **seats first**.
- If seats are tied, the tiebreak is **valid votes**; if still tied, **alphabetical order of listed abbreviations**.
- If consensus reporting is ambiguous, the fallback source of truth is the **official Bulgarian Central Election Commission (CIK)**.

What does **not** count:
- Mere vote-share ranking without translating to seats.
- Narrative/media framing about who "won" the campaign unless it maps to actual seat ranking.
- Coalition stories that do not affect the contract's explicit coalition-dissolution rule.

How the wording affects my view:
- Because the contract is specifically about **second place in seats**, the relevant question is whether GERB-SDS looks like a second-place seat finisher. The accessible evidence instead points to GERB-SDS as a first-place seat finisher.
- I explicitly verified the relevant date and timing: the election is scheduled for **19 April 2026**, and the market resolves by consensus reporting with fallback to CIK if ambiguity remains.

## Key assumptions

- The compiled polling table is directionally accurate.
- GERB-UDF on the market corresponds in practice to the GERB-SDS coalition whose seat total is being discussed in public reporting.
- No major coalition dissolution or ballot-label issue will materially alter seat attribution under the contract.
- No extraordinary late swing occurs in the final days before the election.

## Why this is decision-relevant

The market is at an extreme probability (96%), so even a modestly credible case that the true probability is much lower is highly decision-relevant. If the current evidence is directionally correct, then the market is not just slightly off; it is potentially inverted relative to the likely finishing order.

## What would falsify this interpretation / change your mind

I would revise materially upward if I found any of the following:
- direct, recent pollster releases showing GERB-SDS genuinely running second in seats rather than first;
- credible independent reporting that public consensus already treats GERB-SDS as the likely second-place finisher;
- clear contract-interpretation evidence that the market's GERB-UDF label maps to a different seat-attribution outcome than the polling tables imply;
- evidence of coalition dissolution or candidate-registration changes that make the current seat ranking expectations misleading.

## Source-quality assessment

- **Primary source used:** Polymarket contract text / market page for what counts at resolution.
- **Most important secondary/contextual source:** Wikipedia's 2026 Bulgarian parliamentary election page, especially the polling table and prior-result summary.
- **Evidence independence:** **Low to medium.** The main empirical evidence is a compiled page that cites multiple polls, but I did not directly validate each pollster release.
- **Source-of-truth ambiguity:** **Medium.** The contract clearly names CIK as fallback official source, but I could not directly access CIK during the run, and the case is date-sensitive and consensus-reporting-dependent.

## Verification impact

I performed an **additional verification pass** because the market was at an extreme probability and the case is high-resolution-risk.

That pass included:
- direct fetch/parsing of the Wikipedia page to confirm the polling table content rather than relying only on a summary extract;
- explicit review of the contract wording on the market page;
- attempted direct access to CIK pages, which failed with 403s.

This extra verification **did not materially change** my directional view. It increased confidence that the polling compilation really does show GERB-SDS leading, while also lowering confidence somewhat because official-site access was blocked.

## Reusable lesson signals

- **Possible durable lesson:** Extreme market probabilities on foreign-election rank-order markets deserve a direct contract-and-polling sanity check; mislabeled or misunderstood rank-order markets can produce very large apparent dislocations.
- **Possible missing or underbuilt driver:** none confidently identified from this single run.
- **Possible source-quality lesson:** For election-rank markets, direct access to the official election authority and at least one direct pollster release is especially valuable when the market price is extreme.
- **Confidence that any lesson here is reusable:** medium.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: This case may reflect a recurring evaluation pattern for extreme-probability rank-order election markets, and there is also a linkage / canonical-gap issue because relevant Bulgaria and party slugs do not appear to be cleanly available in `20-entities/` for this run.

## Recommended follow-up

- Directly verify one or more underlying pollster releases if time permits.
- Check CIK once accessible for official registration / ballot naming and any clarification relevant to coalition attribution.
- Have another researcher test the possibility that the market UI or label mapping is inverted or otherwise misleading.
- Pending better contrary evidence, treat GERB-SDS finishing second as a low-probability path.

## Canonical-mapping check

I checked for clean canonical slugs locally and did **not** find obvious existing `20-entities/` pages for Bulgaria, GERB-SDS, PP-DB, Revival, or DPS. I therefore left canonical linkage fields empty and recorded these in `proposed_entities` rather than forcing uncertain canonical mappings.

## Verification impact on final estimate

Final estimate remained **8%**, with the main reason unchanged: the outside view still says GERB-SDS is much more likely to finish first than second.