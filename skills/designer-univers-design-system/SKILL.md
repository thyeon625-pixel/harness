---
name: designer-univers-design-system
description: "Draft Designer_Univers visual-language tokens, pattern principles, accessibility review, and design-system documentation without activating runtime code by default."
version: 0.1.0
author: Hermes Agent
license: Internal
platforms: [macos]
metadata:
  hermes:
    tags: [Designer_Univers, harness, staging, visual-language]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Design System Harness

## When to Use

Use for visual language/token/pattern planning, accessibility checks, and design-system documentation drafts. Runtime code/storybook work requires separate approved software scope.

## Procedure

1. Route with `designer-univers-expert-router`; keep `default_cost_tier=L1` unless optional research/implementation/full review is explicitly requested.
2. Keep all outputs under System/Runs path contracts described in `docs/designer-univers/custom-harnesses/designer-design-system/HARNESS.md`.
3. Treat protected sources as read-only lenses and never upload raw images/materials to external tools without explicit user approval.
4. Require the shared `safety-reviewer` before promotion candidates, public use, or canonical absorption.
5. In GitHub fork staging, describe intended paths only; do not create canonical Designer_Univers files.

## Verification

- `python3 scripts/designer_univers_validate.py` passes in the fork.
- Outputs distinguish source evidence, interpretation, draft proposal, and approved knowledge.
- No runtime/code/purchase/public action occurs without separate approval.
