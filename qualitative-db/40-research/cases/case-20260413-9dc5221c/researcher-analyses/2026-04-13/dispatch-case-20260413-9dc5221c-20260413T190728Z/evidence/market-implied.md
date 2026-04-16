---
type: evidence_map
case_key: case-20260413-9dc5221c
dispatch_id: dispatch-case-20260413-9dc5221c-20260413T190728Z
research_run_id: 18ced415-8cd0-4433-9ebd-4ee964919e31
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: chess
entity:
topic: "whether a 95.05% market price is justified for Sindarov with two rounds left"
question: "Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?"
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["javokhir-sindarov", "2026-fide-candidates-tournament"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "market-implied", "chess"]
---

# Summary

The market is pricing near-certainty because Sindarov appears to hold a dominant late-stage lead in a short event. The residual risk is real but concentrated.

## Question being evaluated

Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?

## Current lean

Yes, with very high probability, but not quite as high as the market’s 95.05%.

## Prior / starting view

Start from the market as serious prior: if the market is above 95%, the most likely explanation is that Sindarov already has a nearly decisive live edge rather than a broad long-run superiority claim.

## Evidence supporting the claim

- Wikipedia live tournament page: Sindarov listed at 9/12, Giri 7/12, others lower.  
  - Why it matters: a two-point lead with two rounds left is an overwhelming structural edge.  
  - Direct or indirect: contextual-direct on standings.  
  - Weight: high.

- Event format: only 14 rounds, with tie-breaks only if first is tied.  
  - Why it matters: very limited remaining sample; most paths preserve the leader.  
  - Direct or indirect: direct on mechanism.  
  - Weight: high.

- Sindarov profile/rating context: 2745, world no. 11, 2025 World Cup winner.  
  - Why it matters: reduces concern that the lead is a pure fluke from an overmatched entrant.  
  - Direct or indirect: contextual.  
  - Weight: medium.

## Evidence against the claim

- FIDE is the actual settlement source, and the fetched official pages did not provide a clean live standings extract.  
  - Why it matters: there is some source-of-truth friction; contextual pages could lag.  
  - Direct or indirect: direct on resolution reliability.  
  - Weight: medium.

- Two rounds plus possible tie-breaks still leave a nonzero path to failure.  
  - Why it matters: 95% can still be too high if late collapse and tiebreak variance are understated.  
  - Direct or indirect: direct on residual risk.  
  - Weight: medium.

- Extreme market prices can overcompress tail risk.  
  - Why it matters: traders often round "huge favorite" up toward certainty.  
  - Direct or indirect: indirect.  
  - Weight: low to medium.

## Ambiguous or mixed evidence

- Media coverage praising Sindarov’s dominance could be both signal and hype.
- Rating/rank context supports class, but tournament conversion is more important than generic strength now.

## Conflict between inputs

No major factual conflict. The main issue is weighting and source hierarchy: contextual standings strongly support the price, but official-source fetch quality was weaker than ideal.

## Key assumptions

- Contextual standings are materially accurate.
- No procedural/fair-play disruption changes results.
- Conversion from a two-point lead with two rounds left is extremely likely.

## Key uncertainties

- Exact official live standings and tie scenarios from FIDE surfaces.
- Whether any non-performance controversy could alter outcomes.

## Disconfirming signals to watch

- Official round-13 result narrowing the lead sharply.
- FIDE notice of dispute, forfeit, or changed standings.
- Entering round 14 with a tie or near-tie.

## What would increase confidence

- Clean official FIDE standings page showing the same 9/12 lead.
- Official round-13/14 recap preserving at least a one-point cushion.

## Net update logic

The market starts from a sensible place: a late-stage tournament lead of this size deserves a very high price. I trim slightly below market because the current evidence for live standings is cleaner from contextual sources than from official fetches, and because 95% leaves little room for the residual tail of two remaining rounds plus tiebreak variance.

## Suggested downstream use

Use as an orchestrator synthesis input: market largely efficient, with only modest caution about extreme-price tail risk and official-source verification quality.