---
type: source_note
case_key: case-20260413-f6bfc755
dispatch_id: dispatch-case-20260413-f6bfc755-20260413T152336Z
analysis_date: 2026-04-13
persona: variant-view
domain: entertainment
subdomain: streaming-rankings
entity:
topic: netflix-us-top-10-movies-weekly-chart
question: Will "Thrash" be the top US Netflix movie this week?
driver:
date_created: 2026-04-13
source_name: Netflix Tudum Top 10 - United States Movies
source_type: primary_chart
source_url: https://www.netflix.com/tudum/top10/united-states/movies
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: ["variant-view finding"]
tags: [netflix, top10, source-of-truth, timing]
---

# Summary

This is the governing source-of-truth surface named by the market description: Netflix's own Tudum Top 10 page for United States movies.

## Key facts extracted

- The United States movies page was reachable on 2026-04-13.
- The visible published weekly window on the page was `3/30/26 - 4/5/26`.
- The page methodology language says Netflix Top 10 lists are weekly and region-specific.
- A separate direct HTML inspection of `https://www.netflix.com/tudum/top10` confirmed the same week string in page source and showed title rows for the currently published chart.
- In direct source inspection, the currently published global movie chart included `Anaconda` as #1 with `9,900,000` views for `3/30/26 - 4/5/26`; the US movie page was also still keyed to the same week, indicating the next update had not yet posted during this run.

## Evidence directly stated by source

- Netflix publishes regional weekly Top 10 movie charts.
- The currently visible US movie week on the authoritative page was `3/30/26 - 4/5/26`.
- The page contains methodology text indicating the lists are country-specific and weekly.

## What is uncertain

- The readable fetch did not cleanly expose the US title names for the current week, only the week label and ranking structure.
- Because the relevant resolution week is the one ending 2026-04-12 and Netflix is expected to update on 2026-04-14 at 3 PM ET, the authoritative page had not yet published the deciding chart at the time of research.
- Therefore no direct authoritative evidence yet proves `Thrash` specifically is #1 for the resolving week.

## Why this source may matter

This is the explicit source named in the market rules, so it governs settlement. The key variant implication is that the deciding evidence is not yet published, which makes a very high pre-update market probability somewhat more fragile than it first appears.

## Possible impact on the question

The source supports confidence about how the market will eventually resolve, but not yet about which title wins for the unresolved week. That pushes the analysis toward a timing-and-verification variant view rather than a hard title-level contradiction.

## Reliability notes

High reliability for settlement because it is the named official chart. Lower immediate usefulness for this run than usual because the decisive weekly update is not yet live.