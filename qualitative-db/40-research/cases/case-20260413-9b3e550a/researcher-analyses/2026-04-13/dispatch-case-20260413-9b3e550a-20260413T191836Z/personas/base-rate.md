---
artifact_type: agent_finding
schema_version: v1
case_key: case-20260413-9b3e550a
case_id: 486e70ea-39f6-406b-8cd6-58f061814155
market_id: 40ee3bf8-5598-4e09-ac01-028e008406d1
persona: base-rate
title: "Base-rate view on whether PP–DB finishes third in the 2026 Bulgarian parliamentary election"
status: final
entity:
driver: elections
related_entities: ["associated-press", "reuters"]
related_drivers: ["elections"]
proposed_entities: ["we-continue-the-change-democratic-bulgaria", "movement-for-rights-and-freedoms", "revival-bulgaria", "progressive-bulgaria", "central-election-commission-of-bulgaria"]
proposed_drivers: []
market_implied_probability: 0.78
own_probability: 0.71
confidence: medium
agreement_with_market: slight_disagreement
sources_used: ["2026-04-13-base-rate-election-date-and-rules.md", "2026-04-13-base-rate-poll-history.md"]
assumption_note: qualitative-db/40-research/cases/case-20260413-9b3e550a/researcher-analyses/2026-04-13/dispatch-case-20260413-9b3e550a-20260413T191836Z/assumptions/base-rate.md
evidence_map: qualitative-db/40-research/cases/case-20260413-9b3e550a/researcher-analyses/2026-04-13/dispatch-case-20260413-9b3e550a-20260413T191836Z/evidence/base-rate.md
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
analysis_date: 2026-04-13
type: agent_finding
---

# Executive summary
PP–DB looks like the most likely third-place finisher, but not by a huge margin. The market implies 78%; my estimate is **71%**. I therefore **slightly disagree** with the market on price, mainly because the most recent cross-firm polling usually has PP–DB in third, but often only narrowly ahead of DPS. A base-rate view says the modal outcome is still PP–DB third, yet the edge is too thin for near-80 confidence.

# Research question
Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election, where resolution is by seats won, then valid votes, then abbreviation order if still tied?

# Directional call
**Yes, PP–DB is the favorite to finish third.**

# Probability estimate
- **Market-implied probability:** 0.78
- **My probability:** 0.71
- **Agreement vs market:** slight disagreement; same direction, but I think the contract is priced a bit rich.

# Main reasoning
## Outside-view / base-rate frame
In fragmented Bulgarian parliamentary politics, parties already established in the low-to-mid teens are usually the natural candidates for third place once a new entrant or larger bloc occupies the top two. PP–DB entered this cycle from a stronger baseline than DPS or Revival: in the October 2024 election table, recalculated vote shares were GERB 26.4, PP–DB 14.2, Revival 13.4, DPS 11.5. That baseline matters because it says PP–DB was already the strongest non-GERB bloc short of the very top.

The main structural change is the emergence of Progressive Bulgaria, which appears to have displaced PP–DB from second to third rather than from third to fourth in most recent polling. Under that structure, third place is mostly a contest between **PP–DB and DPS**, with Revival now more often running fifth than third.

## Current evidence
The March-April 2026 polling compilation shows a repeated pattern across multiple firms:
- Alpha Research (19-26 Mar): PB 30.8, GERB 21.2, **PP–DB 11.1**, DPS 9.8, Revival 6.9.
- Gallup (20-30 Mar): PB 28.4, GERB 23.4, **PP–DB 10.9**, DPS 10.7, Revival 6.5.
- Sova Harris (2-6 Apr): PB 33.6, GERB 19.0, **PP–DB 11.2**, DPS 9.7, Revival 7.8.
- MarketLinks (17-21 Mar): PB 29.1, GERB 22.2, **PP–DB 13.3**, DPS 10.5, Revival 5.5.

This is exactly the kind of evidence a base-rate persona should respect: several different firms, same broad ordering, no need for an elaborate story. PP–DB is not dominating, but it is usually ahead in the relevant race.

## Why I am below the market
The polling edge is often small. Gallup has PP–DB ahead of DPS by only 0.2 points. In a proportional system with regional seat conversion, a sub-1-point national lead is absolutely not the same thing as a locked-in third place. The contract resolves on seats, not just national vote share, and while national order is a strong guide, it is not perfect.

So the right outside-view move is not to overreact to vivid campaign narratives, but also not to confuse "most likely" with "nearly certain." A fairer estimate is low 70s rather than high 70s.

# Strongest disconfirming evidence or consideration
The strongest disconfirming consideration is **how thin PP–DB's lead over DPS is in some of the latest polling**, especially Gallup's 10.9 vs 10.7. If turnout composition, house effects, or seat conversion break slightly against PP–DB, DPS can plausibly take third.

A secondary disconfirming point is that Progressive Bulgaria may be drawing disproportionately from PP–DB's electorate, which means older baselines where PP–DB sat clearly above the pack may now overstate its cushion.

# What could change my mind
I would move materially lower on PP–DB if any of the following appeared:
- several late independent polls showing DPS clearly ahead of PP–DB, not just tied;
- evidence that district-level seat conversion favors DPS enough to overcome a tiny PP–DB national edge;
- strong late evidence that Revival is being understated and has re-entered the realistic third-place race;
- official or near-official reporting on election night showing PP–DB underperforming its late polling band.

I would move modestly higher if late polling consistently showed PP–DB ahead of DPS by ~2+ points across multiple firms.

# Source of truth and resolution logic
## Governing source of truth
The governing source of truth is the market's stated resolution logic:
1. rank by **seats won** in the Bulgarian National Assembly election;
2. if tied on seats, break ties by **valid votes**;
3. if still tied, break by **alphabetical order of listed party abbreviations**;
4. market uses a **consensus of credible reporting** if results are clear;
5. if ambiguous, fallback is the **official results of the Central Election Commission of Bulgaria (CIK)**.

## Date / timing check
- Election date in the market description: **19 April 2026**.
- Independent contextual confirmation from the 2026 election page: the election is scheduled for **19 April 2026**, following appointment of a caretaker government on 18 February 2026.
- Market close/resolution timestamp in assignment: **2026-04-18 20:00 ET**, i.e. just before election day in Bulgaria. So the key question is pre-election probability, not post-vote interpretation.

# Canonical-mapping check
## Canonical linkages used
- Driver used: `elections`
- Canonical entities used only where known from vault: `associated-press`, `reuters`

## Proposed entities instead of forced weak fits
I did **not** force uncertain canonical slugs for the causally central actors. Important but unresolved entities are recorded as proposed:
- `we-continue-the-change-democratic-bulgaria`
- `movement-for-rights-and-freedoms`
- `revival-bulgaria`
- `progressive-bulgaria`
- `central-election-commission-of-bulgaria`

## Proposed drivers
- none

# Evidence floor and compliance
## Evidence floor assessment
This was an ordinary interpretive election market with date sensitivity and consensus-reporting dependency, so the right threshold was at least **two meaningful sources** plus an explicit resolution/source-of-truth check.

## How I met it
1. **Election-date / rules source note** capturing the election date, threshold, electoral system, and market resolution hierarchy.
2. **Polling-history source note** capturing the recent cross-firm ordering of PP–DB, DPS, and Revival.
3. Additional assumption note and evidence map to make the tradeoff legible.

## Compliance statement
I met the evidence floor using one rules/date source set plus one substantive polling/context source set, and I explicitly checked date relevance, source-of-truth logic, and strongest disconfirmation.

# Source-quality assessment
## Primary source
The best primary resolution source is the **Central Election Commission of Bulgaria (CIK)** because the market explicitly names it as the official fallback if consensus reporting is ambiguous. I could not directly inspect CIK in this environment because the site was Cloudflare-blocked here.

## Key secondary/contextual source
The most useful contextual source was the **Wikipedia raw 2026 Bulgarian parliamentary election page**, specifically its polling table and cited election-date references. This is not authoritative by itself, but it is useful as a recent cross-firm aggregation and provides visible provenance to AP/Politico/other reporting.

## Evidence independence
Evidence independence is only moderate. The polling compilation is one secondary aggregation and may embed correlated polling-industry assumptions. However, the underlying entries come from multiple firms, which is still better than relying on a single poll or a single news story.

## Source-of-truth ambiguity
Resolution ambiguity is manageable rather than severe. The main ambiguity is operational access to CIK from this environment, not the contract wording. The contract itself is relatively clear: seats first, votes second, CIK fallback if reporting conflicts.

# Verification impact
- **Extra verification performed:** yes
- **What I verified:** election date, market timing relevance, official-source fallback logic, and whether recent polling still broadly places PP–DB in third.
- **Did it materially change the view?** modestly. The extra pass mainly reduced the chance of overconfidence. It reinforced that PP–DB is favorite, but the thin PP–DB-over-DPS margin kept me below the market.

# Reusable lesson signals
- In fragmented parliamentary systems, third-place contracts can look easy but still be materially noisier than winner markets when several parties cluster around 9-13%.
- For seat-ranking markets, a small national polling lead should not be treated as equivalent to a large seat-probability edge.
- When a new entrant reorganizes the top of the field, older second-place status can still matter as a base rate, but only after checking whether the entrant is pulling more from that party than from the rest of the field.

# Orchestrator review suggestions
- Consider adding canonical entity pages for PP–DB, DPS/MRF, Revival, Progressive Bulgaria, and CIK if Bulgarian election markets will recur.
- No urgent follow-up suggested for this specific run beyond normal controller synthesis.

# Bottom line
PP–DB is the **most likely** third-place finisher, so my directional answer is **Yes**. But the best outside-view read is **71%**, not the market's **78%**, because recent evidence usually has PP–DB third while leaving enough room for a DPS overtake that I cannot justify treating this as close to settled.
