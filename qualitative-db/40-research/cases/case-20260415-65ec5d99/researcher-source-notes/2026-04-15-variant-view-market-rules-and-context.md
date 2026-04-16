---
type: source_note
case_key: case-20260415-65ec5d99
dispatch_id: dispatch-case-20260415-65ec5d99-20260415T210454Z
analysis_date: 2026-04-15
persona: variant-view
domain: sports
subdomain: soccer
entity: real-madrid
topic: real-madrid-vs-alaves-market-rules-and-context
question: Will Real Madrid CF win on 2026-04-21?
date_created: 2026-04-15
source_name: Polymarket market page + Understat team context
source_type: market rules + statistical context
source_url: https://polymarket.com/event/lal-rea-ala-2026-04-21
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: [real-madrid]
related_drivers: [injuries-health, seasonality]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, understat, la-liga, real-madrid, alaves]
---

# Summary

This note captures the governing market resolution logic from Polymarket plus broad contextual team-strength information from Understat's 2025/26 Real Madrid team page.

## Key facts extracted

- The market resolves **Yes only if Real Madrid wins in 90 minutes plus stoppage time**; any draw or Alavés win resolves No.
- If the match is postponed, the market stays open until played; if canceled with no make-up game, it resolves No.
- The stated primary resolution source is the **official statistics of the event as recognized by the governing body or event organizers**; if those are unavailable within 2 hours, consensus credible reporting may be used.
- Understat hosts a dedicated 2025/26 team page for Real Madrid, indicating up-to-date statistical tracking for the current season and supporting the contextual claim that Real Madrid remains an elite-side baseline rather than a legacy-name-only team.

## Evidence directly stated by source

- Polymarket directly states the market rules and primary resolution source.
- Understat directly states that it provides detailed Real Madrid xG stats for the 2025/2026 season.

## What is uncertain

- The fetched Polymarket page did not expose lineup/injury specifics.
- The accessible Understat page confirmed active statistical coverage but did not yield a clean machine-readable stat extract during this run.
- This note does not by itself prove Real Madrid's exact current form level, only that strong contextual-statistical coverage exists for the current season.

## Why this source may matter

- Polymarket is the governing contract surface for what counts.
- Understat is a strong contextual source for team-strength framing and a useful check against lazy prestige-only narratives.

## Possible impact on the question

- The contract wording slightly lowers the probability relative to a casual “better team should win” framing because draws are full No outcomes.
- The contextual-statistics source supports treating Real Madrid as a deserved favorite, but not automatically an overwhelming one absent lineup or situational confirmation.

## Reliability notes

- Polymarket is authoritative for market wording and resolution mechanics, but not for match strength.
- Understat is a respected contextual football analytics source for team-strength direction, though it is not the source of truth for match settlement.
- Evidence independence is medium because the note combines one primary contract source with one independent contextual-statistics source.