---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: variant-view
domain: tech-ai
subdomain: frontier-model-releases
entity:
topic: DeepSeek V-series public release status
question: Has DeepSeek publicly launched the next DeepSeek V model, such as V4, by the relevant deadline?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official website plus DeepSeek official GitHub/Hugging Face surfaces
source_type: primary
source_url: https://www.deepseek.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [product-launches, development]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-49227e85/researcher-analyses/2026-04-13/dispatch-case-20260413-49227e85-20260413T180153Z/personas/variant-view.md]
tags: [deepseek, official-source, launch-audit]
---

# Summary

Official DeepSeek surfaces checked during this run did not show a clearly announced, generally accessible DeepSeek V4 or other next-major V-series flagship release as of 2026-04-13.

## Key facts extracted

- The main DeepSeek website fetch did not surface any visible V4 release announcement or public access details during this check.
- DeepSeek's GitHub organization showed repositories for DeepSeek-V2 and DeepSeek-V3, plus nonqualifying side-series and specialized products, but no visible DeepSeek-V4 repository in the org listing checked on 2026-04-13.
- DeepSeek-V3 had a public GitHub repository and a later archival release record, reinforcing that prior major V-series launches leave visible official traces.
- DeepSeek's Hugging Face org page showed later products and V3.2-related listings, but no clearly visible DeepSeek-V4 public model card in the checked surface.

## Evidence directly stated by source

- DeepSeek website fetch returned only sparse site content and footer/legal text; no V4 launch text appeared in the fetched readable content.
- GitHub org listing on 2026-04-13 included DeepSeek-V2 and DeepSeek-V3 among visible repos, but not DeepSeek-V4.
- GitHub releases API for DeepSeek-V3 showed a public release object for V3 (published 2025-06-27) described as archival/DOI generation.
- Hugging Face org surface displayed products including DeepSeek-OCR, DeepSeek-OCR-2, and DeepSeek-V3.2 variants, but not a visible DeepSeek-V4 card in the checked result.

## What is uncertain

- The main website fetch was sparse; absence in readable extraction is not perfect proof of absence on the full site.
- DeepSeek could theoretically launch through another official channel or an application UI surface before mirror sites or scraped surfaces show it.
- A private, gated, or partially exposed model could exist without qualifying under the contract.

## Why this source may matter

These are the closest available primary surfaces to the market's stated source of truth. The contract explicitly prioritizes official information from DeepSeek, so failure to find a clear public V4 launch on official surfaces is materially bearish for a near-term Yes resolution.

## Possible impact on the question

If no official DeepSeek surface clearly announces and exposes a next-major V-series model to the general public by the deadline, the market should resolve No even if rumors, leaks, or limited-access sightings exist.

## Reliability notes

Primary-source quality is high, but this is partly negative evidence (absence of qualifying launch evidence rather than a direct official denial). That makes it strong for source-of-truth logic but imperfect for timing claims about what could still appear before deadline.