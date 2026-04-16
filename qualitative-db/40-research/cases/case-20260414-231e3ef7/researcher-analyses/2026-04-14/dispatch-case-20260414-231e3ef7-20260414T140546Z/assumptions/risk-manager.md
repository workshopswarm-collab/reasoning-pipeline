---
artifact_type: assumption_note
schema_version: v1
persona: risk-manager
created_at: 2026-04-14T10:07:00-04:00
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["javokhir-sindarov", "2026-fide-candidates-tournament"]
proposed_drivers: []
case_key: case-20260414-231e3ef7
dispatch_id: dispatch-case-20260414-231e3ef7-20260414T140546Z
analysis_date: 2026-04-14
type: assumption_note
entity:
driver:
related_entities: []
---

# Assumption
The market should be valued off tournament state and official FIDE reporting rather than treated as already resolved, because the contract resolves only when FIDE declares the winner (or fallback consensus reporting applies).

# Why this assumption is needed
Polymarket is pricing Sindarov around 99% based on a dominant round-12 position, but the contract text says the market resolves to the player that wins the tournament, not to the player who is merely the overwhelming favorite after round 12.

# Supporting considerations
- FIDE is the explicit primary resolution source in the market description.
- FIDE round-12 coverage says Sindarov is "one step closer" and that Giri still has a must-win game against him, which implies the event remains live.
- Extreme market probabilities can overcompress residual upset, rules, or reporting risk.

# Main failure mode if wrong
If the official tiebreak structure or pairing situation made Sindarov effectively unbeatable after round 12, then my probability would be understated. Conversely, if there were an unobserved operational issue (appeal, withdrawal, postponement, result correction), then market certainty would be overstated.

# What would reduce this assumption risk
A direct official standings/tiebreak page or final FIDE declaration confirming whether a draw in round 13 clinches outright victory, plus the eventual official winner announcement.

# Net effect on estimate
This assumption pushes me modestly below the market rather than far below it. It does not flip the directional view that Sindarov is the overwhelming favorite.