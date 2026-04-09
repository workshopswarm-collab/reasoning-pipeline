---
type: agent_finding
domain: culture
subdomain: film
entity:
topic: Risk-manager view on Project Hail Mary second weekend > $54M
question: Will "Project Hail Mary" second weekend domestic box office be greater than $54M?
driver: seasonality
date_created: 2026-03-30
agent: risk-manager
stance: lean yes, but market overstates confidence
certainty: medium
importance: high
novelty: medium
time_horizon: immediate
related_entities: []
related_drivers: [seasonality, media-narratives, product-launches, performance]
upstream_inputs:
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-risk-manager-the-numbers-final-box-office.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-risk-manager-the-numbers-weekend-chart-context.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-risk-manager-rotten-tomatoes-reception.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/assumptions/risk-manager.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/evidence/risk-manager.md
downstream_uses: []
tags: [domain/culture, subdomain/film, market/project-hail-mary-second-weekend, agent/risk-manager]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/agent-findings/risk-manager/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
legacy_original_note_kind: persona
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-0a94627e
dispatch_id: dispatch-case-20260330-0a94627e-20260330T142051Z
analysis_date: 2026-03-30
persona: risk-manager
---

# Claim
The market question is whether *Project Hail Mary* earns **more than $54M** domestically in its second weekend. The market-implied probability at the supplied close price is **79.25%**. My own view is that **YES was more likely than not, around 68%**, but that the market was **too confident** given how close the eventual result sat to the strike.

## Implication for the question
This is a case where I **disagree modestly with the market on confidence rather than direction**. The movie had the profile of a likely YES: huge $80.5M opening, strong reception, broad theater footprint, and an excellent -32% hold. But the actual final second weekend came in at **$54.5376M** — only about **$0.54M above the threshold**. That is a reminder that the underpriced risk was not a collapse narrative; it was **margin-to-strike risk** and the chance of a small downward revision or softer-than-expected Sunday number.

Because the market closed after the weekend had effectively played out, the remaining edge question was mostly about **finalization risk and confidence calibration**. A 79% price embedded not just a bullish directional view but a claim that the final reported number would likely survive above the line with decent cushion. I do not think the available evidence justified that level of confidence.

## Supporting evidence
- The Numbers reports a finalized second weekend of **$54,537,595**, above the strike and confirming the directional YES thesis.
- The same source shows an **$80,506,007 opening weekend** and only a **-32% second-weekend drop**, indicating strong playability.
- The film stayed **#1 domestically** in weekend two with **4,077 theaters**, so there was no sign of broad demand collapse.
- Rotten Tomatoes presents clearly positive critical and audience framing, which is consistent with stronger holds for a big commercial release.

## Counterpoints
- The realized buffer over the contract line was only about **1.0%** of the threshold. That is much thinner than a 79% market price would normally make me comfortable with.
- Strong box-office narrative signals can be misleading in threshold contracts. “Still #1” and “great hold” are bullish in general, but they do not guarantee safety against a finely set strike.
- The film’s **156-minute runtime** slightly constrained throughput and left less room for upside surprise than a shorter crowd-pleaser might have had.

## Key assumptions
- Strong retention would survive final reporting without being revised below the strike.
- Positive reception and weak competition would translate into enough real weekend revenue, not just a good comparative headline.
- The market was not over-extrapolating from the general success story into excessive confidence about a narrow threshold.

## Why this is decision-relevant
The biggest lesson is about **confidence discipline**. The market’s 79.25% price appears to have been directionally right but somewhat careless about tail risk near the line. For threshold box-office markets, the risk-manager should care less about “is the movie doing well?” and more about “how much room is there between the expected finish and the contract cutoff?” Here, that room was very small.

## What would falsify this interpretation
- Evidence that contemporaneous near-final estimates before close already sat materially above $54M with enough buffer that revision risk was trivial.
- Box Office Mojo final data showing a much larger margin than implied by the secondary sources.
- Reliable evidence that comparable late-weekend estimates almost never revise downward enough to matter in this range.

## Recommended follow-up
- In future box-office bracket markets, track **distance from strike** and probable revision size explicitly rather than relying on generic holdover strength.
- Preserve Sunday estimate snapshots when possible; they matter most for calibration when contracts close after most of the weekend has already occurred.
- Treat prices in the high-70s as statements about both **probability** and **embedded confidence**. Here, the latter looks somewhat overstated.