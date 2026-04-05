---
type: agent_finding
domain: culture
subdomain: film
entity: Project Hail Mary
topic: market-implied assessment of Project Hail Mary second-weekend box office
question: Will "Project Hail Mary" 2nd weekend domestic box office be greater than $54M?
driver: seasonality
date_created: 2026-03-30
agent: market-implied
stance: mildly bullish vs market
certainty: medium-high
importance: high
novelty: medium
time_horizon: immediate-resolution
related_entities: [amazon]
related_drivers: [seasonality, product-launches, media-narratives]
upstream_inputs:
  - qualitative-db/10-domains/culture/film/00-overview.md
  - qualitative-db/30-drivers/seasonality.md
  - qualitative-db/30-drivers/product-launches.md
  - qualitative-db/30-drivers/media-narratives.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/source-notes/case-20260330-0a94627e-market-implied-the-numbers-movie-page.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/source-notes/case-20260330-0a94627e-market-implied-weekend-chart-confirmation.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/source-notes/case-20260330-0a94627e-market-implied-box-office-mojo-link-anomaly.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/assumptions/market-implied.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/evidence/market-implied.md
downstream_uses: []
tags: [domain/culture, subdomain/film, market/project-hail-mary, agent/market-implied]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/agent-findings/market-implied/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
legacy_original_note_kind: persona
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-0a94627e
dispatch_id: dispatch-case-20260330-0a94627e-20260330T142051Z
analysis_date: 2026-03-30
persona: market-implied
---

# Claim

The market's **79.25% YES** price is directionally right, but after taking the market seriously as a prior I still land a bit higher, at roughly **91% YES** that `Project Hail Mary`'s second weekend will resolve above **$54M**.

## Implication for the question

My view is **rough agreement with a bullish tilt**. The strongest case for the market is that it correctly priced a very strong second-weekend hold after an $80.5M opening. The strongest case against the current price is that a major box-office source is already publishing a weekend number of **$54.5376M**, which is above the line. The main remaining risks are not demand-related; they are **revision risk** and **resolution-source mechanics**.

Explicit answers required by the case:

- **What is the market question?** Whether the domestic Mar. 27-29, 2026 second-weekend gross for `Project Hail Mary` is greater than **$54M**.
- **What probability is the market implying?** **79.25% YES**.
- **What is my probability estimate?** **91% YES**.
- **Do I agree or disagree with the market?** I **roughly agree** on direction but think the market is somewhat too low given the currently published box-office figure.

## Supporting evidence

1. **The Numbers movie page shows $54,537,595 for the second weekend**. That is direct evidence above the threshold.
2. **The Numbers weekend chart independently repeats the same $54,537,595 figure**, along with a **#1** rank, **-32%** drop, and **4,077** theaters.
3. **The trajectory makes sense**: an **$80.506M** opening followed by a **32%** second-weekend drop is exactly the sort of strong-hold pattern a bullish market should respect.
4. **Daily grosses for Mar. 27-29 support the reported weekend total**, so this does not look like a stray or internally inconsistent number.

## Counterpoints

1. **The margin over the threshold is small**: only about **$537,595**. That is enough for YES right now, but not enough to eliminate revision risk.
2. **The Box Office Mojo title URL cited in the market description currently resolves to a different movie page** (`The Super Mario Galaxy Movie`), which creates genuine operational uncertainty around the primary resolution source.
3. **The Numbers page markup still looks estimate-like in places**, so it is prudent not to overstate certainty before full finalization.

## Key assumptions

- The currently reported **$54.5376M** weekend figure will not revise down below **$54.0M**.
- The Box Office Mojo anomaly is a source-link/plumbing problem, not evidence that the underlying `Project Hail Mary` weekend number is wrong.
- If Box Office Mojo remains ambiguous, the market's fallback confirmation logic will still end up anchoring to materially the same second-weekend result.

## Why this is decision-relevant

The market-implied perspective should start by asking what the market is pricing correctly. Here, the answer is: **the market was right to be strongly bullish on the film's hold quality**. The opening-to-second-weekend conversion was excellent, and the published second-weekend number is indeed above the bar. But if the market is still only at 79.25% after that number is visible, it is probably embedding extra discount for **close-call revision risk** and **source-resolution ambiguity**. That discount is reasonable, but in my view it is a bit too large.

Stated differently: the market seems to have efficiently aggregated the box-office-demand case, but not fully collapsed the residual operational uncertainty.

## What would falsify this interpretation

- Final Box Office Mojo Domestic Daily values or fallback-resolved figures come in **below $54.0M**.
- A material downward revision from The Numbers pushes the weekend under the bar.
- Resolver treatment of the Box Office Mojo anomaly creates an unexpected resolution path inconsistent with the currently published The Numbers number.

## Recommended follow-up

- Check final Box Office Mojo Domestic Daily values for Mar. 27-29 as soon as the correct film page is available.
- Check for any Monday actuals revision from major trades or The Numbers.
- Treat any price still materially below ~90% after clean source confirmation as likely stale or overly cautious.

## Strongest case that the market is efficiently aggregating evidence

The market likely understood before many isolated researchers would that `Project Hail Mary` had the profile of a strong week-two hold: big opening, strong weekdays, continued #1 status, and broad theater support. A non-market view would need stronger evidence than vague skepticism, because the market's high starting prior already matched the film's realized momentum quite well.

## Where I still agree and disagree after inhabiting the market's logic

- **Agree:** the movie looked very likely to clear $54M because its week-two hold profile was clearly strong enough.
- **Disagree:** once The Numbers is already printing **$54.5376M**, I think **79.25%** is a little too low unless one is very worried about source plumbing or a downward revision of more than half a million dollars.

## What evidence would make me trust the market more or less

- **Trust market more / move lower:** if finalization uncertainty proves larger than it looks, especially if the current number revises sharply or the resolver treats the Box Office Mojo mismatch as materially blocking.
- **Trust market less / move higher:** if correct Box Office Mojo daily totals appear and still sum above **$54M**, because then the remaining discount should compress hard.