---
type: source_note
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: hockey
entity: nhl
topic: case-20260413-e8e9e57e | risk-manager
question: Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket contract text plus NHL official-site source-of-truth rule
source_type: market rules / primary resolution logic
source_url: https://polymarket.com/event/nhl-2025-26-art-ross-trophy
source_date: 2026-04-13
credibility: high
recency: high
stance: supports-yes-with-resolution-caveat
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [nhl, connor-mcdavid]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e8e9e57e/researcher-analyses/2026-04-13/dispatch-case-20260413-e8e9e57e-20260413T224434Z/personas/risk-manager.md]
tags: [source-note, market-rules, source-of-truth, resolution]
---

# Summary

The market description says the contract resolves according to the player awarded the 2025-26 NHL Art Ross Trophy, resolves No if the listed player is not announced as a finalist, and uses official NHL information as the primary resolution source while allowing consensus credible reporting as fallback. For risk analysis, this means the biggest remaining uncertainty is not who led the scoring race, but whether official NHL award/finalist communication cleanly matches the statistical outcome on time.

## Key facts extracted

- Market resolves according to the player awarded the 2025-26 NHL Art Ross Trophy.
- If the listed player is not announced as a finalist for the 2025-26 Art Ross Trophy, the market resolves to No.
- Primary resolution source is official information from the NHL.
- Consensus of credible reporting may also be used.

## Evidence directly stated by source

- Official NHL information governs first.
- There is fallback to consensus reporting if needed.
- Finalist wording exists in the contract even though the Art Ross is typically associated with points leadership.

## What is uncertain

- The contract text creates some source-of-truth/timing sensitivity around “announced as a finalist,” which is not obviously the standard way the Art Ross is discussed publicly.
- It is not fully clear from the market text alone whether an official finalist list is always separately published in a clean and timely way for this trophy.
- If official NHL communication lagged, consensus reporting might matter.

## Why this source may matter

This note defines the main residual failure mode after the sporting evidence: operational or interpretive settlement risk, not a meaningful remaining race risk.

## Possible impact on the question

Supports a high Yes probability, but not an absolute 99%+ confidence, because the contract still depends on NHL official or consensus reporting mechanics rather than the raw standings table alone.

## Reliability notes

Primary for contract interpretation. Not sufficient on its own for the sporting facts, but essential for identifying remaining tail risk and source-of-truth ambiguity.