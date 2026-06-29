---
name: designer-univers-technical-writer
description: "Designer_Univers staging skill for technical-writer: Draft technical documentation, API/architecture guides, diagrams, tutorials, and version notes for Designer_Univers-related systems without modifying runtime code or publishing docs by default."
version: 0.1.0
author: Hermes Agent
license: Internal
platforms: [macos]
metadata:
  hermes:
    tags: [Designer_Univers, harness, staging, operations]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Technical-Writer Harness

## When to Use

Use this staging skill when routing GitHub-only Designer_Univers harness work for `designer-technical-writer`. It is not installed into the canonical Designer_Univers runtime.

## Procedure

1. Route with `designer-univers-expert-router`; keep `default_cost_tier=L1` unless optional full-team/L3 review is explicitly requested.
2. Keep artifacts under the System/Runs path contract in `docs/designer-univers/custom-harnesses/designer-technical-writer/HARNESS.md`.
3. Keep protected sources read-only and never upload private/protected data to external services without explicit user approval.
4. Require the shared `safety-reviewer` before promotion candidates, public sharing, or canonical absorption.
5. In GitHub fork staging, describe intended paths only; do not create canonical Designer_Univers files.

## Verification

- `python3 scripts/designer_univers_validate.py` passes in the fork.
- Outputs distinguish evidence, interpretation, proposal, and approved knowledge.
- No runtime/canonical/public/external paid action occurs without separate approval.
