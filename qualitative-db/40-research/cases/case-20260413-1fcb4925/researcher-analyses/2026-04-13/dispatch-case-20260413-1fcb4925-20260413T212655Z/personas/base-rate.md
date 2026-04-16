---
type: agent_finding
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
research_run_id: 187da139-4dd6-4a29-bf47-91b827dcc916
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: "2026 Bulgarian parliamentary election"
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: disagree
certainty: medium
importance: high
novelty: high
time_horizon: "through election day and reporting window"
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["progressive-bulgaria", "rumen-radev", "gerb-sds", "pp-db", "revival", "movement-for-rights-and-freedoms", "central-election-commission-of-bulgaria"]
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-source-notes/2026-04-13-base-rate-polymarket-contract-and-resolution.md", "qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-source-notes/2026-04-13-base-rate-wikipedia-election-overview.md"]
downstream_uses: []
tags: ["base-rate", "bulgaria", "parliamentary-election", "pb", "first-place", "evidence-floor-met", "verification-pass"]
---

# Claim

I do **not** think the available evidence supports the market's near-certainty that Progressive Bulgaria (PB) will win the most seats in the 2026 Bulgarian parliamentary election. My outside-view estimate is that PB is a plausible disruptive entrant, but a newly formed coalition with **0 incumbent seats** should not be treated as a ~96% first-place seat winner without much stronger independently verified late polling or seat-model evidence.

## Market-implied baseline

The market-implied probability from `current_price: 0.9595` is **95.95%**.

## Own probability estimate

My own estimate is **35%**.

## Agreement or disagreement with market

I **disagree sharply** with the market.

Why:
1. **Outside-view prior:** in fragmented parliamentary systems, brand-new coalitions can surge, but winning the **most seats** outright is a much narrower and harder event than being relevant or breaking into parliament.
2. **Structural baseline:** the accessible election overview still shows **GERB–SDS** as the dominant incumbent bloc on **66 current seats**, while PB is shown on **0 current seats**.
3. **Verification gap:** I was able to verify that PB is on the ballot and tied to former president Rumen Radev in accessible election context, but I did **not** verify an independent late-source consensus showing PB clearly first. For a 95.95% price in a high-risk, date-sensitive case, that gap matters a lot.

## Implication for the question

The question is not whether PB matters electorally. The question is whether PB wins **the most seats**. On current accessible evidence, PB looks like a serious contender at most, not something close to locked. The market appears to be pricing a case-specific narrative far more aggressively than the visible structural evidence justifies.

## Key sources used

1. **Primary resolution / direct contract source:**
   - `qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-source-notes/2026-04-13-base-rate-polymarket-contract-and-resolution.md`
   - Based on: Polymarket market page for Bulgaria Parliamentary Election Winner.
   - Role: defines what counts, source-of-truth logic, election date, tie-breakers, and reporting hierarchy.

2. **Key secondary/contextual source:**
   - `qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-source-notes/2026-04-13-base-rate-wikipedia-election-overview.md`
   - Based on: Wikipedia 2026 Bulgarian parliamentary election page.
   - Role: field structure, current seat baseline, ballot presence of PB, and system mechanics.

3. **Independent confirmation embedded in the contextual source's references:**
   - The extracted election page cites an **Associated Press** item for the caretaker government setting the election for **19 April 2026**.
   - I treat this as limited independent confirmation of the election date, not of PB's winning chances.

**Compliance / evidence-floor note:**
- Evidence floor target for this case was **at least three meaningful sources unless directly settled by an authoritative source**.
- I met this only **partially** in quality terms: one direct governing source, one meaningful contextual source, and one limited independent confirmation on the election date/reporting chain.
- Because direct web access to CIK and some media endpoints was blocked by anti-bot protections, I am lowering confidence and preserving that limitation explicitly rather than pretending the evidence stack is cleaner than it is.

## Supporting evidence

- The contract clearly resolves on **winning the most seats**, not merely winning votes, media attention, or narrative momentum.
- The accessible election overview shows PB as a **new coalition** with **0 current seats**, while GERB–SDS remains the largest current parliamentary bloc.
- In proportional representation systems with a threshold and fragmented competition, new entrants face structural friction converting attention into an outright first-place seat win.
- The market is at an extreme **95.95%** probability, which raises the verification standard. The available accessible evidence does not clear that bar.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that PB is not a random tiny entrant: the accessible election overview links it to **former president Rumen Radev**, which is exactly the sort of case-specific factor that could overwhelm an ordinary new-party base rate. If there are Bulgarian-language late polls or seat models showing PB already clearly first, my current estimate is too low.

## Resolution or source-of-truth interpretation

What counts:
- the party or coalition that wins the **greatest number of seats** in the Bulgarian National Assembly on **19 April 2026**
- if seats tie, the tiebreak is **valid votes**, then **alphabetical order of abbreviation**
- if a named coalition dissolves, settlement uses the constituent party with the largest pre-election seat count
- the primary reporting logic is **consensus of credible reporting**, with fallback to the **Central Election Commission of Bulgaria (CIK)** if ambiguous

What does **not** count:
- generic popularity without seat conversion
- narrative dominance
- current parliamentary size alone
- unofficial chatter without credible reporting support

Date / deadline / timezone check:
- election date verified as **19 April 2026**
- market deadline for unresolved ambiguity is **31 October 2026, 11:59 PM ET**
- market close / resolve timestamp in assignment: **2026-04-18 20:00 ET**, i.e. before election day local completion, which makes reporting-chain interpretation important after voting starts

Primary source of truth:
- **Central Election Commission of Bulgaria (CIK)** if reporting is ambiguous.

Fallback source-of-truth logic:
- consensus of credible reporting first; CIK governs if consensus is ambiguous.

## Key assumptions

- A new coalition should not be priced near certainty to win first place without unusually strong direct evidence.
- The accessible evidence stack is missing some information, but not enough to justify assuming that a ~96% market price is automatically correct.
- Structural incumbency and seat-conversion friction still matter in Bulgaria's fragmented parliamentary setting.

## Why this is decision-relevant

This is exactly the kind of market where vivid narrative can swamp the outside view. If traders are treating PB's entrance as equivalent to already having the election won, the market may be overpaying for salience and underweighting structural difficulty.

## What would falsify this interpretation / change your mind

I would move materially upward if I saw any of the following:
- multiple independent late polls showing PB clearly **first** rather than merely competitive
- credible seat models showing PB with a durable seat lead over GERB–SDS and other rivals
- consensus reporting from reputable outlets treating PB as the clear front-runner, not just a major disruptor
- early official or near-official results placing PB first on seats

## Source-quality assessment

- **Primary source used:** Polymarket contract / market page.
- **Most important secondary/contextual source used:** Wikipedia's 2026 Bulgarian parliamentary election page.
- **Evidence independence:** **low to medium**. I have one direct governing source and one main contextual source; independent confirmation was partial and mostly about date/reporting context, not outcome probability.
- **Source-of-truth ambiguity:** **medium**. The governing fallback source is clear (CIK), but the pre-resolution public information environment is noisy and some direct official/media endpoints were inaccessible from this environment.

## Verification impact

- **Additional verification pass performed:** yes.
- I explicitly rechecked the contract wording, election date, and contextual field structure after the initial evidence pass.
- **Did it materially change the view?** No. It modestly increased confidence that the date and reporting chain are real, but it did **not** produce the kind of independent evidence needed to support the market's extreme confidence.

## Reusable lesson signals

- **Possible durable lesson:** in election markets on exact rank or winner outcomes, a new-party narrative should not automatically defeat structural priors without independently verified late polling.
- **Possible missing or underbuilt driver:** none confidently identified beyond the existing `elections` driver.
- **Possible source-quality lesson:** anti-bot barriers on official or major-media sites can create fake confidence if not stated plainly; preserving the access limitation is itself important provenance.
- **Confidence that any lesson here is reusable:** medium.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: Bulgarian political actors relevant to this market appear absent from canonical entity coverage, so the case can only use `proposed_entities` rather than clean linkage.

## Recommended follow-up

- Highest-value follow-up is one more independent late-cycle Bulgaria-focused poll or seat-model source, especially one directly indicating whether PB is actually polling first.
- If synthesis can access better Bulgarian-language reporting or CIK mirrors, that could move the estimate materially.
