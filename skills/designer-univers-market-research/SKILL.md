---
name: designer-univers-market-research
description: "Designer_Univers staging skill for market-research: Designer_Univers-aware market, competitor, consumer, and trend research using public/free sources or provided material while keeping private sources and paid research accounts gated."
version: 0.1.0
author: Hermes Agent
license: Internal
platforms: [macos]
metadata:
  hermes:
    tags: [Designer_Univers, harness, staging, operations]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Market-Research Harness

## When to Use

Use this staging skill when routing GitHub-only Designer_Univers harness work for `designer-market-research`. It may be installed as a bounded canonical runtime pilot only after explicit user approval; otherwise it remains staging-only.

## Procedure

1. Route with `designer-univers-expert-router`; keep `default_cost_tier=L1` unless optional full-team/L3 review is explicitly requested.
2. Keep artifacts under the System/Runs path contract in `docs/designer-univers/custom-harnesses/designer-market-research/HARNESS.md`.
3. Keep protected sources read-only and never upload private/protected data to external services without explicit user approval.
4. Require the shared `safety-reviewer` before promotion candidates, public sharing, or canonical absorption.
5. In GitHub fork staging, describe intended paths only; do not create canonical Designer_Univers files.

## Verification

External web/API lookup and paid/private research accounts are disabled for synthetic pilots. Real research lookups require explicit routing, safety review, and user approval.

- In GitHub fork staging, `python3 scripts/designer_univers_validate.py` passes.
- In canonical Designer_Univers runtime, use `/Users/taehyeon/.hermes/scripts/designer_baseline_audit.sh --verbose`.
- Outputs distinguish evidence, interpretation, proposal, and approved knowledge.
- No runtime/canonical/public/external paid action occurs without separate approval.

## Dry-Run Scenario

Use the `## Dry-Run Prompt` in `docs/designer-univers/custom-harnesses/designer-market-research/HARNESS.md` for staging verification. Dry-runs must remain GitHub-only or System/Runs-only drafts and must not create canonical Designer_Univers files.

