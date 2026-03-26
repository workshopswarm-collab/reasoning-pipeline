---
type: domain_overview
domain: tech-ai
subdomain: models
topic: AI models research overview
date_created: 2026-03-25
last_updated: 2026-03-26
agent: orchestrator
status: active
certainty: medium
importance: high
upstream_inputs:
  - vault/40-research/source-notes/by-domain/tech-ai/2026-03-25-llm-basics.md
downstream_uses: []
related_entities: []
related_drivers: [product-launches, operational-risk, regulation]
tags: [domain/tech-ai, subdomain/models, overview]
---

# Overview summary

Models are the capability-and-evaluation subdomain of tech & AI: architectures, training regimes, benchmarks, inference behavior, safety properties, and deployment-quality tradeoffs. They deserve a standalone overview because model quality is a distinct object of analysis even when commercial outcomes ultimately depend on product and distribution layers.

## Why this subdomain matters

This subdomain matters because many high-salience AI questions begin with model capability, but researchers can misread the space if they treat capabilities as identical to product success or enterprise adoption. A dedicated models overview keeps the technical-evaluation layer separate from infrastructure, regulation, and product packaging.

## Core conclusions

- Capability is only one layer of the AI stack, but it is still an essential one.
- Benchmarks, real-world usefulness, safety behavior, and deployment economics can diverge materially.
- Model evaluation should separate architecture and capability claims from product distribution and workflow integration.
- Release-specific model narratives belong in research notes, while this note should stay focused on durable evaluation structure.

## Main evidence clusters

- model families and architecture choices
- benchmarks and evaluation design
- reasoning, multimodality, and tool-use behavior
- safety, alignment, and failure modes
- inference cost, latency, and serving constraints
- model-to-product integration

## Important recurring objects

- frontier and open-source model families
- labs and model providers
- eval suites and benchmark ecosystems
- safety and alignment frameworks
- inference platforms and deployment layers
- API and product wrappers

## Important recurring drivers

- product-launches
- operational-risk
- regulation
- partnerships

## Common conflicts or failure modes

- treating benchmark gains as equivalent to durable user value
- flattening very different model classes into one leaderboard mentality
- ignoring inference cost, latency, and operational quality while focusing only on capability
- treating release hype as evidence of stable competitive position

## Missing coverage

- stronger evaluation-source hierarchy
- better handling of model-family versus version-specific notes
- clearer links between model capability and real product adoption

## Most fragile assumptions

- that the best benchmark model automatically wins the market
- that one evaluation suite captures broad model usefulness
- that release-day capability rankings are stable over meaningful time horizons

## Recommended next research steps

- keep version-specific model notes and launch reactions in `40-research/`
- use this note for stable model-evaluation orientation rather than rolling leaderboard commentary
- deepen substructure only where repeated retrieval demand justifies model-class or eval-specific breakdowns
