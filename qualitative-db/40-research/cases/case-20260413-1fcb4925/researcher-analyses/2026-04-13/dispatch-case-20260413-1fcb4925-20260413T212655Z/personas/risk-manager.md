---
type: agent_finding
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
research_run_id: ad2462a8-2e50-428b-a45d-1c7f2d4df798
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: "Bulgaria 2026 parliamentary election"
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: yes-but-overpriced
certainty: medium
importance: high
novelty: medium
time_horizon: "through election day and CEC seat allocation window"
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["progressive-bulgaria", "gerb-sds", "we-continue-the-change-democratic-bulgaria", "central-election-commission-of-bulgaria", "rumen-radev"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["bulgaria", "election", "polymarket", "risk-manager", "pb"]
---

# Claim

Progressive Bulgaria (PB) is still the most likely winner of the most seats, but the market is too close to certainty. My working view is **78%** for PB to win the most seats, versus the market-implied **95.95%**. The core risk is not that PB is unfavored; it is that the market is underpricing ordinary election uncertainty around a brand-new alliance, poll dispersion, threshold-driven seat conversion, and the gap between pre-election narrative dominance and official CEC seat allocation.

## Market-implied baseline

Current price is **0.9595**, implying **95.95%**.

That price embeds not just “PB is leading” but something close to “very little can realistically go wrong from here.” I do not think the evidence quality justifies that confidence level.

## Own probability estimate

**78%** that PB wins the most seats.

## Agreement or disagreement with market

**Disagree.** I agree on direction (PB is the favorite) but disagree materially on confidence. PB appears to be leading in multiple March source clusters, but the accessible evidence does not support treating the race as almost settled.

Why I am below market:

- PB is a **new coalition** built around Rumen Radev and may not convert leader popularity into seats as cleanly as a mature party machine.
- Polling support is **directionally consistent but quantitatively noisy**: accessible coverage ranges from roughly **21%** to around **31%** for PB.
- Bulgaria’s fragmented field and **4% threshold** make seat allocation more nonlinear than topline vote share alone.
- The contract resolves on **seats**, with fallback to official **CEC** reporting if reporting consensus is ambiguous, so late interpretive confidence should be discounted.

## Implication for the question

The right interpretation is not “PB probably loses”; it is “PB probably wins, but the residual loss probability is much larger than ~4%.” On a risk-manager lens, the market looks **overconfident** rather than directionally wrong.

## Key sources used

Evidence-floor compliance: **met high-difficulty floor with 4 meaningful source classes plus an extra verification pass**.

1. **Primary resolution / source-of-truth source**: Polymarket market description and rules page
   - URL: https://www.polymarket.com/event/bulgaria-parliamentary-election-winner
   - Role: authoritative for contract wording, what counts, tie-breaks, and fallback source-of-truth logic.
   - Direct vs contextual: **direct** for resolution mechanics.

2. **Contextual election-mechanics source**: The Sofia Globe factfile on Bulgaria’s April 2026 parliamentary elections
   - URL: https://sofiaglobe.com/2026/03/19/bulgarias-april-2026-parliamentary-elections-the-sofia-globes-factfile/
   - Role: campaign calendar, voting hours, threshold, and CEC reporting timetable.
   - Direct vs contextual: **contextual**, but directly useful for date/timing verification.

3. **Contextual polling / fragility source**: The Sofia Globe summary of Market Links polling
   - URL: https://sofiaglobe.com/2026/03/18/market-links-poll-support-for-radevs-progressive-bulgaria-has-dropped-4-5-points-in-a-month/
   - Role: specific disconfirming evidence that PB’s lead may be narrower and weakening.
   - Direct vs contextual: **contextual**, but important disconfirming evidence.

4. **Independent contextual confirmation source**: Balkan Insight on election reshaping and Sova Harris polling
   - URL: https://balkaninsight.com/2026/03/19/bulgarias-next-election-already-reshaping-the-political-landscape/
   - Role: independent confirmation that PB emerged as frontrunner.
   - Direct vs contextual: **contextual**.

5. **Additional verification pass / corroboration bundle**: Politico Poll of Polls Bulgaria page, Google News results snippets surfacing Reuters / TVP World / Alpha Research / Gallup / BTA references, and Wikipedia pages for the election and PB as a cross-check on basic field description.
   - Role: independent confirmation that PB-leading is not a one-source artifact, while also highlighting source-quality limits.
   - Direct vs contextual: **contextual / verification only**.

Supporting artifact references:
- `qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-source-notes/2026-04-13-risk-manager-polls-and-field.md`
- `qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413-1fcb4925-20260413T212655Z/assumptions/risk-manager.md`
- `qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413-1fcb4925-20260413T212655Z/evidence/risk-manager.md`

## Supporting evidence

- Multiple accessible March sources show **PB in first place**.
- Balkan Insight cited a **Sova Harris** reading with PB at **30.9%** versus GERB at **19.3%**, which would ordinarily be a comfortable first-place margin.
- Google News snippets surfaced apparently independent reports from **Reuters**, **TVP World**, **Alpha Research coverage**, **Gallup coverage**, and **BTA**, all broadly consistent with PB as the current frontrunner.
- The opposition field remains **fragmented**, reducing the odds that one challenger cleanly overtakes PB before election day.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming evidence is the **Market Links** poll relayed by The Sofia Globe showing PB at only **21.1%** versus **18.6%** for GERB-UDF, alongside **19.1% undecided voters**. That is still a PB lead, but it is not remotely a lock.

Additional downside considerations:

- PB is a **new electoral vehicle**, so organization and district-level conversion may lag national attention.
- Several parties hover around the **4% threshold**, meaning modest vote shifts can change seat allocation materially.
- “Most votes” and “most seats” are close but not identical when fragmentation and threshold effects are present.

## Resolution or source-of-truth interpretation

**Governing source of truth:** The market rules say resolution is based first on a **consensus of credible reporting**, and if there is ambiguity, then **solely on official Bulgarian government results from the Central Election Commission of Bulgaria (CEC / CIK)**.

**What counts:**
- The relevant outcome is **which listed party or coalition wins the greatest number of seats** in the Bulgarian National Assembly from the **19 April 2026 parliamentary election**.
- If there is a tie in seats, the market falls back to **greater number of valid votes**, then alphabetical tie-break if needed.
- If a named coalition dissolves, the market resolves by the **constituent party within that coalition that held the largest number of seats before the election**.

**What does not count:**
- Popular-vote lead by itself does **not** settle the market unless it is needed as the explicit seat-tie-break.
- Government-formation ability after the election does **not** determine resolution.
- Narrative that PB “won the campaign” or “won the anti-establishment vote” does **not** matter unless it converts into the most seats under reported results.

**Date / timing check:**
- Election day is **19 April 2026**.
- The Sofia Globe factfile says voting runs **7am–8pm local time** on 19 April, extendable by up to an hour for queued voters.
- The same factfile says the **CEC has until 23 April** to announce seat distribution and until **26 April** to announce names of elected MPs.
- The market itself closes/resolves operationally on **18 April 2026 20:00 ET**, so this is a clearly **date-sensitive pre-event pricing question** rather than a settled-results question.

## Key assumptions

- PB’s apparent polling lead is real enough to survive normal late-campaign movement.
- No rival, especially **GERB-SDS**, closes the gap materially in the final days.
- PB’s support is not disproportionately soft, protest-driven, or poorly distributed for seat conversion.
- Available media summaries are directionally reliable even if some raw underlying polling documents are not directly accessible.

## Why this is decision-relevant

At a **95.95% implied probability**, the market is demanding near-certainty. In election markets, especially with a newly created coalition and fragmented seat mechanics, the main error is often **overconfidence** rather than wrong direction. A decision-maker should distinguish “favorite” from “near lock.”

## What would falsify this interpretation / change your mind

I would revise **up toward the market** if:
- multiple final-week independent polls converge with PB holding a **clear, stable double-digit lead** over GERB, and
- credible election-night reporting shows PB clearly ahead in both votes and projected seats.

I would revise **down further** if:
- a late reputable poll shows **GERB tied with or ahead of PB**,
- credible reporting shows PB organizational weakness or district-level underperformance,
- final-week evidence suggests undecideds are breaking sharply away from PB, or
- early seat projections show threshold effects narrowing or erasing PB’s seat edge.

The single fastest invalidator of my current view would be **independent final-week polling convergence showing PB’s lead was overstated and the seat race is effectively even**.

## Source-quality assessment

- **Primary source used:** Polymarket market rules page for contract wording and settlement mechanics.
- **Most important secondary/contextual source used:** The Sofia Globe factfile and The Sofia Globe Market Links polling summary, with Balkan Insight as an important independent contextual check.
- **Evidence independence:** **Medium.** There is some meaningful cross-source corroboration, but several accessible reports likely depend on overlapping domestic pollsters and media summaries.
- **Source-of-truth ambiguity:** **Low for resolution mechanics, medium for pre-election confidence assessment.** The contract’s fallback to CEC is clear; what is less clear is how much trust to place in currently accessible poll summaries before the vote.

## Verification impact

**Yes, additional verification was performed** because this is a high-difficulty, high-resolution-risk case with an extreme market probability.

The extra pass **did not change the directional view** that PB is favored, but it **did reinforce** my decision to stay materially below market because the added corroboration showed two things at once: PB-leading appears real, and confidence around the exact margin is still too soft for ~96% pricing.

## Reusable lesson signals

- Possible durable lesson: in fragmented parliamentary races, a newly formed alliance can be the clear favorite while still being mispriced at near-certainty because seat conversion and threshold effects are nonlinear.
- Possible missing or underbuilt driver: none clearly identified beyond existing `elections` + `polling` coverage.
- Possible source-quality lesson: when authoritative election commission pages are hard to fetch directly, preserve an explicit distinction between **contract authority**, **timing mechanics**, and **contextual polling evidence** instead of blurring them.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: this case suggests a reusable lesson about overconfidence in fragmented parliamentary markets and also exposed missing canonical entity slugs for core Bulgaria-election objects.

## Recommended follow-up

No urgent follow-up suggested before synthesis beyond checking whether any final-week independent poll or credible seat-projection update materially narrows or widens the PB/GERB gap.