# Evaluator review-from-learning-packet contract

Produce the full canonical contents of `review.md` for one case.

## Output requirements

- Return **only** the final markdown for the file.
- Do **not** wrap the answer in code fences.
- Do **not** include commentary before or after the markdown.
- Preserve YAML frontmatter at the top.
- Use the canonical learning-note structure.
- Keep the exact top heading: `# Learning Note`.

## Required section headings

Use these headings in this order:

1. `## What was being evaluated`
2. `## What the pipeline believed or did`
3. `## What happened in reality`
4. `## Outcome and scoring evidence`
5. `## Which inputs were high signal`
6. `## Which inputs were misleading`
7. `## What was missing`
8. `## Error-pattern classification`
9. `## Driver and mechanism takeaways`
10. `## Source / input / workflow takeaways`
11. `## Proposed intervention or hold decision`
12. `## Promotion candidates for stable layers`
13. `## How this should be reused later`

## Review doctrine

- Distinguish **observed facts** from **inferred explanations**.
- Do not invent resolution, execution, or score facts that are not in the packet.
- If the packet is still incomplete, say so plainly.
- Prefer specific, evidence-linked bullets over generic retrospective prose.
- Preserve uncertainty when the causal story is unclear.
- Use the current draft as a scaffold, but improve it where the packet supports improvement.
- Keep the note useful for later signal extraction and intervention design.

## Frontmatter expectations

Keep or improve the existing frontmatter. When you are unsure, preserve a cautious/draft status rather than overclaiming.

## Canonical source of structure

Use this as the shape reference:
- `qualitative-db/00-system/templates/learning-note-template.md`
