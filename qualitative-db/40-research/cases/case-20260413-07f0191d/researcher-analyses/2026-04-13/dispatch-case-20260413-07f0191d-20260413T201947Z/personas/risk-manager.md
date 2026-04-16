---
type: agent_finding
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 7193f87b-1ac8-4e02-8e83-58e04bae3a49
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: bulgaria-election
entity:
topic: "second-place finisher in 2026 Bulgarian parliamentary election"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: orchestrator
stance: cautious-disagree
certainty: medium-low
importance: high
novelty: medium
time_horizon: event-date
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["GERB-SDS", "PP-DB", "Revival", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: ["2026-04-13-risk-manager-market-contract-and-date", "2026-04-13-risk-manager-election-context-and-current-order", "2026-04-13-risk-manager-competitor-structure"]
downstream_uses: ["orchestrator synthesis"]
tags: ["bulgaria", "election", "exact-rank", "risk-manager", "source-of-truth"]
---

# Claim

I do **not** think the available evidence justifies the market's near-certainty that GERB-SDS will finish **specifically second** in the 2026 Bulgarian parliamentary election. My working view is that GERB-SDS is a plausible top-two finisher, but exact second place is materially more fragile than the current price implies.

**Compliance / evidence-floor note:** this run used three meaningful source classes with preserved provenance: (1) the market contract text as the governing resolution source, (2) a contextual election-overview source for election date, field structure, and current parliamentary ordering, and (3) competitor-structure sources on GERB-SDS, PP-DB, and Revival. I also performed an explicit extra verification pass because the market price is extreme (>85%), but that pass did **not** recover strong independent polling or official Bulgarian reporting sufficient to validate a 96% exact-rank probability.

## Market-implied baseline

Current price is **0.96**, implying roughly **96%** probability that GERB-SDS finishes second.

As a confidence object, that price appears to embed a view that GERB-SDS is not just likely top-two, but very tightly concentrated into the exact second-place slot rather than first or lower.

## Own probability estimate

**Own estimate: 58%.**

That is still above a coin flip because GERB-SDS is clearly a major bloc with a realistic path to second, but far below the market because exact-rank outcomes in fragmented parliamentary systems are usually not this locked absent stronger polling or authoritative late-campaign evidence.

## Agreement or disagreement with market

**Disagree.**

The market may be directionally right that GERB-SDS is a strong contender for second, but I think it is materially overconfident.

Main reasons:

- The strongest disconfirming consideration is simple: the contextual election-overview source shows GERB-SDS as the **current largest parliamentary bloc**, not the current second-largest. If that remains roughly true in electoral strength, first place is a live alternative outcome.
- There are multiple meaningful competitors in the field, especially **PP-DB** and **Revival**, which makes exact placement more fragile than generic top-two status.
- I did not recover fresh independent national polling or authoritative Bulgarian reporting that would justify compressing the distribution into a 96% second-place probability.
- In this kind of market, traders can easily overprice “likely near the top” and underprice the difference between **first / second / third**.

## Implication for the question

The best risk-manager interpretation is: **GERB-SDS finishing second is plausible, but not close to settled.** If I were weighting this input for synthesis, I would treat the market price as overstating precision rather than necessarily pointing in the wrong direction.

## Key sources used

Primary / governing source:

- `researcher-source-notes/2026-04-13-risk-manager-market-contract-and-date.md` — Polymarket contract text and source-of-truth logic. Direct for resolution mechanics and date.

Key secondary / contextual sources:

- `researcher-source-notes/2026-04-13-risk-manager-election-context-and-current-order.md` — election date, field structure, and current parliamentary ordering from the 2026 election overview page. Contextual, not authoritative for final resolution.
- `researcher-source-notes/2026-04-13-risk-manager-competitor-structure.md` — party pages for GERB-SDS, PP-DB, and Revival used to map the competitive structure and stress-test rank fragility. Contextual.

Supporting audit artifacts:

- `.../assumptions/risk-manager.md`
- `.../evidence/risk-manager.md`

Primary source-of-truth for eventual market resolution:

- Consensus of credible reporting first; if ambiguous, official results from the **Central Election Commission of Bulgaria (CIK)** control per contract.

## Supporting evidence

- The contract clearly defines the resolution metric as **seats won**, with explicit tie-breakers. That reduces one class of ambiguity.
- GERB-SDS is a major established coalition and plainly belongs in the top-tier competitive set.
- The field appears fragmented enough that a GERB-SDS second-place finish is absolutely realistic.
- Because the contest is fragmented, a single challenger overtaking GERB-SDS without multiple challengers doing so is a coherent scenario.

## Counterpoints / strongest disconfirming evidence

**Strongest disconfirming evidence:** the contextual election-overview source shows GERB-SDS as the **current first-place parliamentary coalition**, not the current second-place bloc.

That matters because a second-place bet on GERB-SDS is not just a bet that it remains strong; it is a bet that it lands in one very specific rank slot. If GERB-SDS remains the strongest bloc, the market loses. If fragmentation or protest voting pushes it below two rivals, the market also loses.

Additional counterpoints:

- PP-DB remains a meaningful rival.
- Revival is a meaningful anti-establishment rival in a volatile system.
- No recovered source in this run independently validated a near-lock second-place consensus.
- Search/fetch limitations reduced access to broader confirmation, which is itself a reason to avoid mirroring an extreme market price.

## Resolution or source-of-truth interpretation

What counts:

- The party or coalition that wins the **second-greatest number of seats** in the next Bulgarian National Assembly election.
- If tied on seats, the higher **total valid vote** total wins the higher rank.
- If still tied, **alphabetical order of listed party abbreviations** breaks the tie.
- If consensus reporting is ambiguous, the contract falls back to the **official results from CIK**.

What does **not** count:

- Poll position.
- Media narratives about momentum.
- Coalition desirability for government formation.
- Broad top-two likelihood without exact second-place specificity.

Contract wording effect on my view:

- This is an **exact-rank** market, which is more fragile than a generic top-two market.
- The coalition-dissolution clause exists, but I found no concrete evidence in this run that a GERB-SDS label/constituent issue is the main risk.
- The key contract risk is therefore ranking precision, not naming ambiguity.

**Date / timing verification:** both the market contract and the contextual election overview point to **19 April 2026** as election day. The market closes/resolves on **2026-04-18 20:00 ET**, which is before election day local completion, so this is also a date-sensitive pre-event market whose final resolution depends on later reported results.

## Key assumptions

- Current parliamentary ordering is an imperfect but still relevant prior for exact-rank risk.
- No major coalition rupture or candidate shock materially changes GERB-SDS before the vote.
- The market is overpricing second-place specificity rather than responding to strong hidden polling evidence.
- The contextual sources used here are directionally informative even though they are not authoritative election-result sources.

## Why this is decision-relevant

The main risk is an **unforced error from overconfidence**. At 96%, the question is not “can GERB-SDS finish second?” but “is it almost impossible for GERB-SDS to finish first or below second?” I do not think the recovered evidence supports that level of concentration.

## What would falsify this interpretation / change your mind

What would move me **toward the market**:

- Two or more recent, independent national polls consistently showing GERB-SDS clustered around **second specifically**, not merely top-two.
- High-quality Bulgarian reporting converging that one challenger is clearly ahead of GERB-SDS while all others are clearly behind it.
- Late-campaign evidence that the first/second ordering is stabilizing rather than widening into a multi-way contest.

What would move me **further away from the market**:

- Credible polling showing GERB-SDS still leading nationally.
- Credible polling showing GERB-SDS in a volatile cluster with PP-DB and Revival where third becomes plausible.
- Any coalition or turnout shock that increases rank volatility.

## Source-quality assessment

- **Primary source used:** Polymarket contract text / market description.
- **Most important secondary/contextual source used:** the 2026 Bulgarian parliamentary election overview page for field structure and current parliamentary ordering.
- **Evidence independence:** **low-to-medium**. The contextual pages are separate references, but several are within the same general source ecosystem and I did not successfully recover a strong Reuters/official-poll confirmation set.
- **Source-of-truth ambiguity:** **low for final resolution mechanics**, because the contract explicitly points to consensus credible reporting with CIK as fallback; **medium for current pre-election probability estimation**, because the best recovered evidence was contextual rather than direct polling.

## Verification impact

- **Additional verification pass performed:** yes.
- **What was checked:** direct fetches of the market contract and multiple election/party context pages; attempted broader search and independent-source retrieval, which was partly blocked by tool/search limitations.
- **Did it materially change the view?** It reinforced the skepticism. The extra pass did not uncover strong evidence supporting a 96% exact-rank probability, so I stayed well below market.

## Reusable lesson signals

- Possible durable lesson: **exact-rank parliamentary markets can be materially overconfident when traders confuse top-two strength with a specific finishing slot.**
- Possible missing or underbuilt driver: none confidently identified beyond existing `elections`.
- Possible source-quality lesson: when web search access is degraded, extreme market prices should be discounted unless primary/independent confirmation is still recoverable.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**
- Review later for driver candidate: **no**
- Review later for canon or linkage issue: **yes**
- One-sentence reason: the case suggests a reusable caution about exact-rank overconfidence, and the vault currently lacks clean canonical entity slugs for several Bulgarian parties/CIK that would improve linkage quality.

## Verification impact (extra labeled case requirement)

Extra verification was performed because the market-implied probability is extreme. It did **not** materially increase confidence in the market's 96% view; instead, it mostly confirmed that the evidentiary basis recovered in-run was too thin to support near-certainty.

## Reusable lesson signals (extra labeled case requirement)

Same as above: likely reusable caution on exact-rank overconfidence; no new driver proposal with high confidence.

## Orchestrator review suggestions (extra labeled case requirement)

Same as above: consider durable-lesson review and canonical linkage cleanup for Bulgarian party/election entities.

## Recommended follow-up

Before any high-confidence synthesis, obtain at least one stronger independent confirmation set: recent Bulgarian polling, major Bulgarian election coverage, or authoritative analyst aggregation focused on **seat ranking**, not just vote share narratives.