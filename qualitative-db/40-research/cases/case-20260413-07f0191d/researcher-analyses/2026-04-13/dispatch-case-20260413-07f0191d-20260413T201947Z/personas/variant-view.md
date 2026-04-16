---
type: agent_finding
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 5003c593-4325-43a8-b5af-de4b229c1c65
analysis_date: 2026-04-13
persona: variant-view
domain: politics
subdomain: bulgarian-parliamentary-election
entity:
topic: "GERB-UDF (GERB-SDS) second-place finish risk"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: yes
certainty: medium
importance: high
novelty: medium
time_horizon: days
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["progressive-bulgaria", "pp-db-vs-db-ballot-taxonomy"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["bulgaria", "second-place", "contract-interpretation", "evidence-floor-met"]
---

# Claim

GERB-SDS is the most likely second-place finisher, but the best variant framing is that this is not mainly a "GERB is obviously safe" story. It is a "new frontrunner may have emerged while the rest of the opposition remains fragmented" story. I assign **89%** to GERB-SDS finishing second.

**Evidence-floor compliance:** high-difficulty / rule-sensitive case; I used three meaningful sources plus an additional verification pass. Provenance preserved via three source notes, one assumption note, and one evidence map.

## Market-implied baseline

The market price is **0.96**, implying roughly **96%** probability that GERB-SDS finishes second.

## Own probability estimate

**89%**.

## Agreement or disagreement with market

I **roughly agree directionally** with the market that GERB-SDS is the likeliest second-place finisher, but I think **0.96 is somewhat too confident**.

The strongest reason for partial disagreement is **taxonomy and source-of-truth fragility**. The evidence I found supports a race structure where a new actor, Progresivna Bulgaria (PB), may be leading, with GERB second and the rest of the field clearly behind. If that structure is correct, GERB second is very plausible. But the exact mapping among **PB, PP-DB, and DB** is not fully clean in the accessible sources, and the official Bulgarian election commission page was not directly retrievable from this environment. That keeps me below the market's near-settled confidence.

## Implication for the question

The key implication is that GERB does **not** need to be the strongest party to cash this market. A credible variant path is: **PB first, GERB second, everyone else behind**. That is the main underweighted mechanism supporting a yes answer.

## Key sources used

**Primary / governing source-of-truth surface**
- Market contract text in assignment: market resolves by **seat count**, with ties broken by valid votes and then alphabetical order; if consensus reporting is ambiguous, fallback is the **Bulgarian Central Election Commission (CIK)**.
- CIK is therefore the governing official source of truth, even though direct fetch access was blocked in this runtime.

**Key contextual / secondary sources**
- `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-variant-view-politpro-poll-trend.md`
  - Poll aggregator; contextual, not authoritative.
  - Directly relevant to rank-order mechanism.
- `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-variant-view-wikipedia-election-page.md`
  - Contextual field map and timing check; not authoritative.
- `qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-source-notes/2026-04-13-variant-view-politico-poll-of-polls.md`
  - Independent contextual cross-check; imperfect taxonomy fit.

**Direct vs contextual evidence**
- Direct settlement logic: contract wording and CIK fallback rule.
- Contextual evidence: polling/ranking sources showing GERB likely top-two and possibly specifically second.

## Supporting evidence

1. **PolitPro poll trend** shows the exact variant mechanism: **PB 30.8%, GERB 20.7%, DB 10.9%, DPS 10.0%, Revival 7.0%**, with a projected parliament of **PB 93, GERB 63, DB 33, DPS 30, Revival 21**. If even roughly right, GERB is much more likely to finish second than third.
2. **Wikipedia's 2026 election page** independently confirms the election date (**19 April 2026**) and a fragmented field with GERB starting from the largest current parliamentary bloc (66 seats), ahead of PP-DB, Revival, and DPS in the present-seat baseline.
3. **POLITICO's Bulgaria polling context** independently keeps GERB in a clear upper tier, ahead of PP-DB and DPS in the extracted snapshot, which supports GERB as very likely top-two even if its exact rank changes.
4. **Contract mechanics** help the yes case because the market is about **second-most seats**, not coalition bargaining power or media narrative. GERB can lose first place and still resolve yes.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **the unresolved label / ballot-taxonomy issue**: if PB versus PP-DB versus DB is being inconsistently represented across aggregators, the market may be leaning too hard on a race structure that is less clean than it appears. The strongest concrete disconfirming source is the absence of a directly accessible official CIK verification pass in this environment, combined with the fact that my supporting non-official sources are all contextual rather than authoritative settlement sources.

I did **not** find a strong independent source affirmatively showing GERB outside the top two. The best disconfirming case is therefore **source-quality and mapping risk**, not a rival polling consensus that clearly puts GERB third.

## Resolution or source-of-truth interpretation

What counts:
- The relevant outcome is the party/coalition with the **second-greatest number of seats** in the 19 April 2026 Bulgarian parliamentary election.
- If tied on seats, the tie-break is **valid votes**, then alphabetical order of abbreviations if still tied.
- If consensus reporting is ambiguous, the market resolves based solely on official results reported by **CIK**.

What does **not** count:
- Government-formation leverage, coalition talks after the vote, or who enters cabinet.
- Narrative claims about who "won politically" absent the seat ranking.
- Polling itself; polls are only pre-resolution evidence.

How the contract wording affects my view:
- The contract is narrow and rank-based, which actually favors the yes case if GERB sits in a durable top-two band.
- Because the market can resolve on **consensus reporting first**, but fall back to **CIK** if ambiguous, any late taxonomy confusion in media reporting could matter. That is why I discount the market slightly from 96% to 89%.

**Date / deadline / timezone verification:** the election is scheduled for **19 April 2026**; market close and resolution time in the assignment are **2026-04-18 20:00 ET**, i.e. the eve of election day in U.S. time. This means the market is being priced before official votes exist, increasing the importance of contract wording and reporting-source discipline.

## Key assumptions

- PolitPro's PB-first / GERB-second structure reflects a real ballot-valid electoral configuration rather than a taxonomy artifact.
- GERB remains clearly above the older challenger pack (PP-DB/DB, DPS, Revival) in the final pre-election ranking.
- No seat-conversion surprise pushes GERB below second despite a decent national vote share.

## Why this is decision-relevant

This is a high-priced market near resolution. The main decision question is not just whether GERB is likely second, but whether the market is **overconfident** relative to the quality of available proof. My read is: **yes is still favored, but not quite to 96%** because the official-source layer remains partially unverified and the challenger taxonomy is messy.

## What would falsify this interpretation / change your mind

- Direct official or broad credible consensus reporting showing GERB running **third or lower** in seats or vote share.
- Clean evidence that **PB is misclassified, not separately ballot-valid, or not relevant** to the market's rank ordering the way current aggregators imply.
- A strong final polling average from an independent Bulgarian source showing GERB bunched with or below DPS / PP-DB / Revival rather than clearly above them.

## Source-quality assessment

- **Primary source used:** the market contract's explicit source-of-truth logic, with **CIK** as governing fallback official source.
- **Most important secondary/contextual source:** PolitPro Bulgaria poll trend, because it supplies the main variant mechanism for GERB finishing second.
- **Evidence independence:** **medium**, not high. The non-official sources are independent enough to be useful, but all are contextual and none is a direct official settlement source.
- **Source-of-truth ambiguity:** **medium-high** before the vote, because consensus reporting may use inconsistent party labels and I could not directly fetch CIK from this runtime.

## Verification impact

Yes, I performed an **additional verification pass** because the market is priced at an extreme probability and the case is date-sensitive and rule-sensitive.

That extra pass **did not materially change the directional view**, but it **did lower my confidence modestly** by reinforcing that GERB likely remains top-two while leaving unresolved the official ballot / taxonomy clarity needed to justify a 96% price.

## Reusable lesson signals

- **Possible durable lesson:** in party-system markets, second-place contracts can be misread if analysts focus on who is first rather than on whether one legacy party sits in a stable top-two band.
- **Possible missing or underbuilt driver:** none confidently identified beyond ordinary elections/polling mechanics.
- **Possible source-quality lesson:** pre-election rank-order markets with coalition-label ambiguity deserve explicit ballot-taxonomy checks, not just poll checks.
- **Confidence reusable:** medium.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**
- Review later for driver candidate: **no**
- Review later for canon or linkage issue: **yes**
- One-sentence reason: the recurring issue here is not a new driver but a likely **entity/linkage gap** around PB and the unstable mapping among PB / PP-DB / DB in election-market research.

## Recommended follow-up

- At synthesis/resolution time, perform a clean official CIK check on the registered ballot labels and the ranked seat results.
- If available, add one strong domestic Bulgarian polling or election-reporting source to test whether the PB-first / GERB-second structure is real or just aggregator noise.