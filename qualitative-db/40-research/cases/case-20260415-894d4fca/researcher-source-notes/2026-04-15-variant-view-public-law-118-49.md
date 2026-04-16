---
type: source_note
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
analysis_date: 2026-04-15
persona: variant-view
domain: politics
subdomain: legislative-power
entity: u-s-congress
topic: fisa-section-702-reauthorization-timing
question: Did Public Law 118-49 already extend the operative Section 702 deadline beyond the market deadline?
driver: operational-risk
date_created: 2026-04-15
source_name: Public Law 118-49 (Reforming Intelligence and Securing America Act)
source_type: official-law-text
source_url: https://www.govinfo.gov/link/plaw/118/public/49?link-type=html
source_date: 2024-04-20
credibility: high
recency: medium
stance: neutral
certainty: high
importance: high
novelty: high
agent: Orchestrator
related_entities: [u-s-congress, united-states]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/personas/variant-view.md]
tags: [fisa, section-702, public-law, deadline, source-note]
---

# Summary

Official enacted text confirms that Public Law 118-49 was signed on April 20, 2024 and amended the prior FISA Title VII sunset reference from April 19, 2024 to "two years after the date of enactment of the Reforming Intelligence and Securing America Act." That implies the operative statutory expiration is around April 20, 2026, not April 19, 2026.

## Key facts extracted

- The document is the enacted federal law: Public Law 118-49, dated Apr. 20, 2024, for H.R. 7888.
- Section 19(a) states that the relevant paragraph is amended by striking "April 19, 2024" and inserting "two years after the date of enactment of the Reforming Intelligence and Securing America Act."
- Because enactment occurred on Apr. 20, 2024, the replacement date maps to Apr. 20, 2026.
- This matters because the market resolves based on whether reauthorizing legislation is enacted by Apr. 19, 2026 11:59 PM ET.

## Evidence directly stated by source

- Public Law 118-49 is an enacted law, dated Apr. 20, 2024.
- The law explicitly changes the prior expiration language to a rolling formulation tied to enactment date plus two years.

## What is uncertain

- The market description explicitly says qualifying legislation includes Public Law 118-49, but its primary source link points to a Congress.gov bill page that was inaccessible from this runtime due to Cloudflare challenge.
- I did not directly verify via Congress.gov whether its current tracker mirrors the same date expression, though that would be expected.
- Exact interpretation of whether any implementation or certification provisions create a different practical urgency from the legal sunset is not resolved by this source alone.

## Why this source may matter

This is the strongest primary evidence on the core timing mechanism. If the legal sunset is Apr. 20, 2026, a market asking whether Section 702 is reauthorized before it expires by Apr. 19, 2026 may already be asking about a date one day before the actual sunset. That weakens any thesis that Congress must act before Apr. 19, 2026 to avoid expiration.

## Possible impact on the question

This source materially supports a lower-than-market probability for new reauthorizing legislation by the market deadline, because the legal urgency may be weaker than market participants assume.

## Reliability notes

- Source is official enacted statutory text from GovInfo, so credibility is high.
- This is direct evidence on the timing mechanism, not just commentary.
- The main caveat is source-of-truth alignment with the market wording, because the market names Congress.gov as primary resolution source and separately states that Public Law 118-49 qualifies.
