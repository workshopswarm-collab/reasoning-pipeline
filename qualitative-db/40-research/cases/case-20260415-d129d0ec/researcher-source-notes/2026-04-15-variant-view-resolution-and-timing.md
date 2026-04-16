---
type: source_note
case_key: case-20260415-d129d0ec
dispatch_id: dispatch-case-20260415-d129d0ec-20260415T014044Z
analysis_date: 2026-04-15
persona: variant-view
domain: geopolitics
subdomain: russia-ukraine-war
entity: ukraine
topic: Russia military action against Kyiv municipality by April 17?
question: Will Russian Armed Forces initiate a qualifying drone, missile, or air strike on Kyiv municipality by April 17 under the market rules?
driver: conflicts
date_created: 2026-04-15
source_name: Market contract text plus fallback Ukrainian official sources
source_type: market-rule / official-source-framework
source_url: https://polymarket.com/event/russia-military-action-against-kyiv-municipality-by-april-17
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [russia, ukraine]
related_drivers: [conflicts]
upstream_inputs: []
downstream_uses: [variant-view.md, variant-view.sidecar.json]
tags: [source-note, resolution-criteria, timing, source-of-truth]
---

# Summary

The most important underweighted issue is not whether Russia often attacks Kyiv in general, but whether a qualifying strike on Kyiv municipality can be clearly evidenced within the remaining window and satisfy the contract’s narrow source-of-truth and timing logic.

## Key facts extracted

- The market resolves Yes only if Russian Armed Forces initiate a drone, missile, or air strike on Kyiv municipality between market creation and the specified date, using EET as the relevant time basis.
- Qualifying actions include aerial bombs, drones, or missiles launched by Russian Armed Forces on Kyiv municipality’s ground territory.
- Intercepted drones or missiles can still count if there is clear evidence they were directed against Kyiv municipality within the timeframe.
- Surface-to-air missiles and several other attack types do not count.
- Primary resolution source is consensus of credible reporting from major media; fallback in ambiguity is official Ukrainian military/government statements including the Air Force of the Armed Forces of Ukraine, Kyiv City State Administration, and Kyiv mayor.
- If date/time cannot be confirmed by end of the third calendar date after the timeframe, the market resolves No.

## Evidence directly stated by source

- The contract makes source-of-truth and date attribution central, not merely whether explosions or alerts occurred somewhere near Kyiv.
- The contract is municipality-specific, so Kyiv Oblast incidents outside Kyiv municipality would not count.
- The wording allows intercepted attacks to count, but only if they can still be clearly tied to Kyiv municipality during the window.

## What is uncertain

- The exact market creation timestamp is not visible in the assignment block, so the practical window is inferred from the event title and closing time rather than a fully explicit creation-to-close audit.
- The prompt says "by April 17" while the listed closes_at/resolves_at is 2026-04-16 20:00 ET; likely this corresponds to April 17 in Eastern European local time, but the mismatch is itself a timing-verification issue.

## Why this source may matter

This source governs what counts and creates the strongest variant-view argument against a simple base-rate Yes: even frequent Russian air attacks do not automatically satisfy a narrow municipality-and-timestamp contract without clear attributable reporting.

## Possible impact on the question

It pushes the analysis toward under on any naive "Kyiv gets attacked often" framing and toward a more moderate probability that discounts both short time remaining and possible municipality/timing ambiguity.

## Reliability notes

The market contract is the highest-priority interpretive source for what counts. However, it does not itself settle whether a qualifying strike occurs; that depends on later consensus reporting and, if needed, official Ukrainian sources named in the contract.