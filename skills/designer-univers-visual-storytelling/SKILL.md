---
name: designer-univers-visual-storytelling
description: "Draft private visual essays, portfolio narratives, scene/story structures, image prompt plans, and layout plans for Designer_Univers without generating images or publishing protected material by default."
version: 0.1.0
author: Hermes Agent
license: Internal
platforms: [macos]
metadata:
  hermes:
    tags: [Designer_Univers, harness, staging, visual-language]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Visual Storytelling Harness

## When to Use

Use for private visual narrative planning, portfolio story drafts, reference-analysis-to-story transformation, caption/essay planning, and layout sequencing. Require safety review before public/promotion use.

## Procedure

1. Route with `designer-univers-expert-router`; keep `default_cost_tier=L1` unless optional research/implementation/full review is explicitly requested.
2. Keep all outputs under System/Runs path contracts described in `docs/designer-univers/custom-harnesses/designer-visual-storytelling/HARNESS.md`.
3. Treat protected sources as read-only lenses and never upload raw images/materials to external tools without explicit user approval.
4. Require the shared `safety-reviewer` before promotion candidates, public use, or canonical absorption.
5. In GitHub fork staging, describe intended paths only; do not create canonical Designer_Univers files.

## Verification

- `python3 scripts/designer_univers_validate.py` passes in the fork.
- Outputs distinguish source evidence, interpretation, draft proposal, and approved knowledge.
- No runtime/code/purchase/public action occurs without separate approval.
