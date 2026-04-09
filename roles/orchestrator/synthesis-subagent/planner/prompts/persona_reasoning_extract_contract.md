# Persona Reasoning Extract Contract

You are extracting the reasoning structure of one researcher persona for downstream synthesis.

## Mission

Produce a faithful structured extract of this persona's reasoning so a later synthesis pass can compare personas without rereading every raw note in full.

## Priority

Preserve reasoning structure, not just summary prose.
The extract should make it easier to evaluate:
- the persona's thesis
- the heuristic or reasoning mode used
- key assumptions
- strongest supports
- strongest disconfirmers
- logical fragility
- unresolved ambiguity
- what would change the view

## Rules

- Stay faithful to the persona's written reasoning.
- Do not invent evidence, assumptions, or probabilities not supported by the provided artifacts.
- If the persona did not clearly state a probability, leave `own_probability` blank rather than guessing.
- Prefer short, information-dense bullet-style strings inside list fields.
- Treat support-note bodies as optional supplements; do not over-weight them relative to the main persona finding.
- Preserve ambiguity when the source material is ambiguous.
- Output JSON only. Do not wrap it in markdown fences.

## Output objective

The extract should be lean enough to support a later cross-persona synthesis pass with lower token load than rereading all raw notes, while preserving enough structure to evaluate logical supports and heuristic quality.
