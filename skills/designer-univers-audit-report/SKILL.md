---
name: designer-univers-audit-report
description: "Run Designer_Univers governance/protection/pre-absorption audits in fork-first or draft-only mode using System/Runs paths, strict protected-source boundaries, and Hermes verification."
version: 0.1.0
author: Hermes Agent
license: Internal
platforms: [macos]
metadata:
  hermes:
    tags: [Designer_Univers, audit, governance, protection, harness]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Designer_Univers Audit Report Harness

## When to Use

Use for folder, branch, governance, protection, worker, baseline, and absorption-readiness audits related to Designer_Univers.

## Procedure

1. Route with `designer-univers-expert-router` and keep default `cost_tier=L1`.
2. Create run manifest under `Designer Master/System/Runs/{run_id}/` only when later absorbed; in GitHub fork staging, describe the intended path without creating canonical files.
3. Use `audit-scope-designer`, `checklist-builder`, and `safety-reviewer` for simple audits.
4. Add `findings-analyst`, `recommendation-writer`, and `tracking-manager` only when findings/actions are requested.
5. Never write to Designer Earth, System/Rules, or runtime specs without explicit user approval.

## Path Contract

- workspace: `Designer Master/System/Runs/{run_id}/workspace/`
- review: `Designer Master/System/Runs/{run_id}/review/`
- outputs: `Designer Master/System/Runs/{run_id}/outputs/`
- promotion candidates: `Designer Master/System/Runs/{run_id}/promotion_candidates/`

## Verification

- In GitHub fork staging, `python3 scripts/designer_univers_validate.py` passes.
- In canonical Designer_Univers runtime, use the manual baseline audit script instead: `/Users/taehyeon/.hermes/scripts/designer_baseline_audit.sh --verbose`.
- Safety review exists for protected or absorption-related audits.
- Findings distinguish evidence, interpretation, and proposed action.
