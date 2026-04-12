---
type: agent_finding
domain: culture
subdomain: film
entity: Project Hail Mary
topic: second-weekend domestic box office threshold
question: Will "Project Hail Mary" 2nd weekend box office be greater than $54M?
driver: product-launches
date_created: 2026-03-30
agent: base-rate
stance: yes
certainty: medium-high
importance: high
novelty: medium
time_horizon: immediate
related_entities: [Project Hail Mary, Amazon MGM Studios, Oppenheimer, Dune: Part Two, The Martian]
related_drivers: [seasonality, media-narratives, product-launches]
upstream_inputs:
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-base-rate-the-numbers-weekend-data.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-base-rate-box-office-mojo-source-ambiguity.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-base-rate-trade-coverage-and-comps.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/evidence/base-rate.md
downstream_uses: []
tags: [domain/culture, subdomain/film, agent/base-rate, market/case-20260330-0a94627e]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/agent-findings/base-rate/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
legacy_original_note_kind: persona
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-0a94627e
dispatch_id: dispatch-case-20260330-0a94627e-20260330T142051Z
analysis_date: 2026-03-30
persona: base-rate
---

# Claim

`Project Hail Mary` is **very likely to resolve YES** on the `> $54M` second-weekend question. The market-implied probability was **79.25%**, but my current estimate is **98%**.

## Implication for the question

The market question is whether the film’s domestic **March 27–29, 2026** weekend gross exceeds **$54M**. The best available current evidence says it already did: The Numbers lists **$54,537,595**, and both AP and Deadline converged around **$54.5M** on Sunday reporting. At this point, the residual risk is not demand-side uncertainty; it is mostly whether Box Office Mojo’s final daily table for the correct title page matches the same number closely enough.

## Supporting evidence

- **Current market-implied probability:** 79.25% from `current_price = 0.7925`.
- **My probability:** 98%.
- **Reason for disagreement:** the market price looks too low relative to the currently available post-weekend evidence.

Most important evidence:

1. **Exact reported weekend total already above the threshold.**  
   The Numbers shows **$54,537,595**, which is **$537,595** above the line.

2. **Multiple sources converge on the same answer.**  
   AP and Deadline both reported about **$54.5M** and a roughly **-32%** hold.

3. **The hold required to clear $54M was exceptional but not unexplained.**  
   The film had the kinds of conditions that can overpower a skeptical base-rate prior: very strong reception (**A CinemaScore**, **95% RT**), no major new competition, premium-format retention, and a favorable spring-break / Easter calendar setup.

4. **The comparison set suggests this was a standout hold, not a routine one.**  
   Trade coverage explicitly compared the second weekend favorably with `Oppenheimer` (**$46.7M, -43%**) and `Dune: Part Two` (**$46.2M, -44%**). That matters because the threshold required a much better hold than a normal big opener would usually post.

## Counterpoints

- **Base-rate caution mattered before weekend data arrived.**  
  Off an **$80.5M** opening, clearing **$54M** required retaining about **67.7%** of opening weekend, or avoiding a drop worse than about **-32.3%**. That is a hard ask for a big live-action opener and not something I would have assumed by default.

- **The contractual source is Box Office Mojo, not The Numbers or Sunday trades.**  
  So there is still some mechanical resolution risk until the exact Box Office Mojo daily-table final is confirmed.

- **The market description appears to contain a wrong Box Office Mojo URL.**  
  The embedded link points to a different title ID than the apparent real `Project Hail Mary` Mojo page. I view this as a small operational ambiguity, not a meaningful argument that the commercial outcome is below $54M.

## Key assumptions

- Box Office Mojo final daily data for the correct `Project Hail Mary` page will not revise downward by more than **$537k**.
- Resolution will use the intended movie page, despite the likely bad URL in the market description.
- No late source discrepancy emerges between Box Office Mojo and The Numbers large enough to flip the bracket.

## Why this is decision-relevant

The outside view here is useful because it shows **where the market was right to be cautious** and **why that caution is now mostly stale**. Before the weekend results, a strong prior against a >$54M second weekend was reasonable: the threshold implied an unusually small drop for a large-opening non-franchise film. But once the actual Friday/Saturday/Sunday data and cross-source weekend reporting came in, that prior should have been overwhelmed.

Active drivers:
- **product-launches:** post-opening conversion and hold profile of a major release
- **media-narratives:** unusually positive critic/audience reception supporting word of mouth
- **seasonality:** favorable late-March / spring-break / Easter runway and weak competition

## What would falsify this interpretation

- Box Office Mojo’s final Domestic Daily tab for March 27–29 prints a 3-day weekend **below $54.0M**.
- The market resolves against an incorrect or inconsistent source because of the embedded bad URL.

## Recommended follow-up

- Verify the correct Box Office Mojo `Project Hail Mary` page and final Domestic Daily 3-day total once fully visible.
- If this is being converted into a structured prediction now, I would log **98% YES** with a note that the main residual risk is **resolution-source mechanics**, not box-office demand.
