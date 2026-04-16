---
type: source_note
source_type: web
title: Inter vs Cagliari base-rate context and contract check
date: 2026-04-14
case_key: case-20260414-26cfc91d
persona: base-rate
url: https://polymarket.com/event/sea-int-cag-2026-04-17
related_entities: []
related_drivers: []
proposed_entities:
  - fc-internazionale-milano
  - cagliari-calcio
  - serie-a
proposed_drivers:
  - home-field-advantage
  - team-strength-gap
  - draw-rate-in-soccer-match-winner-markets
---

# Source summary
This note captures the minimum provenance for a low-difficulty base-rate read on Inter vs Cagliari.

# Source 1: Polymarket contract page
- URL: https://polymarket.com/event/sea-int-cag-2026-04-17
- Key extract: resolves Yes only if FC Internazionale Milano win; otherwise No.
- Critical contract detail: only the first 90 minutes plus stoppage time count.
- Governing source of truth: official statistics recognized by the governing body or event organizers; if unavailable within 2 hours, consensus of credible reporting may be used.
- Research use: this is the primary direct source for contract interpretation and settlement logic.

# Source 2: Wikipedia 2025–26 Serie A page
- URL: https://en.wikipedia.org/wiki/2025%E2%80%9326_Serie_A
- Fetch date: 2026-04-14
- Key extracts visible in fetched text:
  - statistics correct as of 13 April 2026
  - Inter listed with longest winning run (8 matches)
  - biggest away win listed as Sassuolo 0–5 Inter Milan
  - highest scoring match listed as Inter Milan 6–2 Pisa
  - Lautaro Martínez listed as top goalscorer with 16 goals
  - Cagliari listed among teams with longest losing run (4 matches)
- Research use: contextual evidence that Inter are currently one of the strongest sides in the league and Cagliari are materially weaker.

# Additional context checks
- Inter Milan Wikipedia page: supports long-run elite-club baseline.
- Cagliari Calcio Wikipedia page: supports lower-table / weaker-club baseline.
- These were supportive but did not materially move the estimate beyond the season page.

# Reliability / caveats
- Polymarket contract text is strong for settlement logic.
- Wikipedia is acceptable for low-stakes contextual standings/performance cues but not ideal as a sole statistical authority.
- I attempted broader result/stat-source retrieval, but some common football-stat sites were blocked or degraded in this environment. For this low-difficulty case, the next likely source was unlikely to move the estimate by ~5 percentage points.

# Takeaway for main finding
Base-rate view: Inter should be heavy favorites, but because this is a 90-minute win contract rather than a broader superiority claim, draw risk keeps the estimate around 80% rather than something much closer to certainty.
