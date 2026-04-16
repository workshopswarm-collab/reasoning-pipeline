---
type: source_note
case_key: case-20260416-f08c3dae
dispatch_id: dispatch-case-20260416-f08c3dae-20260416T041907Z
analysis_date: 2026-04-16
persona: risk-manager
domain: sports
subdomain: colombia-primera-a
entity:
topic: CD Tolima vs Deportivo Pereira market context and governing source
question: Will CD Tolima win on 2026-04-18?
driver:
date_created: 2026-04-16
source_name: ESPN COL.1 scoreboard and team schedule APIs plus Polymarket market page
source_type: api_and_market_page
source_url: https://site.api.espn.com/apis/site/v2/sports/soccer/col.1/scoreboard?dates=20260418
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [colombia]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/personas/risk-manager.md
tags: [espn, polymarket, market-context, source-of-truth, team-form]
---

# Summary

This note captures the main auditable inputs used for the risk-manager view: the Polymarket contract wording / governing-source language, and ESPN's current fixture, team-record, recent-form, venue, and bookmaker context for Deportes Tolima vs Deportivo Pereira.

## Key facts extracted

- Polymarket wording: if CD Tolima wins, market resolves Yes; otherwise No.
- Polymarket wording: only first 90 minutes plus stoppage time count.
- Polymarket wording: primary resolution source is official statistics recognized by governing body or event organizers; if not published within 2 hours, consensus of credible reporting may be used instead.
- ESPN scoreboard for 2026-04-18 lists event `401850871`: Deportivo Pereira at Deportes Tolima, scheduled 2026-04-18 23:10Z / 7:10 PM EDT, venue Estadio Manuel Murillo Toro, Ibague.
- ESPN lists Tolima as home with record `7-6-3` and recent form `LLDDW`.
- ESPN lists Deportivo Pereira as away with record `0-7-9` and recent form `DLLLD`.
- ESPN betting context for the same fixture shows DraftKings moneyline roughly Tolima `-370`, draw `+400`, Pereira `+800`; Tolima -1.5 spread priced `-125`.
- ESPN team schedules show Tolima's recent results include home wins over Águilas Doradas (4-1), Jaguares de Córdoba (3-1), Fortaleza CEIF (2-0), and Atlético Nacional (1-0), plus a recent away loss at Pasto (0-1) and draw vs Santa Fe (2-2).
- ESPN team schedules show Pereira's recent results include losses to Alianza FC (2-3), Boyacá Chicó (0-1), Deportivo Cali (0-1), and Águilas Doradas (0-1), with draws against Once Caldas (0-0), Cúcuta Deportivo (2-2), and Internacional de Bogotá (2-2).

## Evidence directly stated by source

- Fixture identity, date, venue, and home/away designation.
- Team records and recent form strings.
- Bookmaker prices embedded in ESPN scoreboard.
- Polymarket contract wording and resolution-source language.

## What is uncertain

- ESPN did not provide a clean standings table in the accessed endpoint.
- No accessible official Dimayor match preview or official lineup/injury bulletin was recovered during this run.
- Recent team form is direct but still a small sample and may hide roster-specific changes.
- Bookmaker pricing is contextual rather than governing.

## Why this source may matter

- It provides the market mechanism and source-of-truth rules needed for settlement interpretation.
- It also gives independent contextual evidence that the matchup is materially lopsided in Tolima's favor, which helps judge whether Polymarket's 0.76 is too high, too low, or roughly fair.

## Possible impact on the question

- The source set supports a bullish Tolima directional view because the home side has a strong overall record and Pereira has no wins through 16 matches.
- The main risk-manager pushback is that the market may be pricing near-certainty off blunt record asymmetry even though soccer draw risk remains material and this contract requires a regulation home win, not merely "avoid loss."

## Reliability notes

- Polymarket is authoritative for contract wording but not for final official match statistics.
- Official governing source for settlement appears to be the match statistics recognized by the governing body / event organizer; for practical review that likely means official league or organizer results first, with credible consensus only as fallback per contract language.
- ESPN is a strong contextual source and useful independent check on fixture identity, records, form, and sportsbook pricing, but it is secondary for settlement.