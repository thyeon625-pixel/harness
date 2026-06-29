# designer-audit-report

## Source

Derived from Harness-100 `94-audit-report` as a Designer_Univers-specific governance and protection audit harness. This is not a direct import.

## Purpose

Create structured audits for Designer_Univers governance, folders, safety boundaries, baseline drift, worker behavior, and absorption readiness. This harness is for **internal project governance audits**, not legal/accounting/tax audits.

## Default Routing

```yaml
harness: designer-audit-report
source: H100/ko/94-audit-report
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; free-only only for public documentation lookup
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping | Default Use |
|---|---|---|---|
| `audit-scope-designer` | scope, criteria, audit plan | Hermes + designer_reviewer | every audit |
| `checklist-builder` | checklist, tests, evidence requests | designer_reviewer | every audit |
| `findings-analyst` | severity, root cause, impact | designer_reviewer + relevant domain worker | when findings exist |
| `recommendation-writer` | corrective action, priority, owner proposal | Hermes + designer_reviewer | when actions needed |
| `tracking-manager` | follow-up ledger and verification status | Hermes ledger keeper | when audit creates follow-ups |
| `safety-reviewer` | protected-source and promotion boundary check | designer_reviewer | required for protected or absorption audits |

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “이 폴더/브랜치 구조가 안전한지 체크” | L1 | audit-scope-designer, checklist-builder, safety-reviewer |
| “흡수 전 준비상태 감사” | L1-L2 | audit-scope-designer, checklist-builder, findings-analyst, safety-reviewer |
| “발견사항과 개선권고까지 작성” | L2 | full audit team except tracking optional |
| “후속조치 추적대장 생성” | L1 | tracking-manager, recommendation-writer, safety-reviewer |
| “공식 규칙 변경 감사” | L3 | full selected team + Claude CLI review + Hermes verification |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_audit_scope.md
Designer Master/System/Runs/{run_id}/workspace/02_audit_checklist.md
Designer Master/System/Runs/{run_id}/workspace/03_findings.md
Designer Master/System/Runs/{run_id}/workspace/04_recommendations.md
Designer Master/System/Runs/{run_id}/workspace/05_tracking_ledger.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_final_audit_report.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Scope** — define audit objective, subject, criteria, protected areas, and allowed evidence.
2. **Checklist** — convert criteria into concrete checks and evidence paths.
3. **Findings** — classify findings by severity and source confidence; no invented evidence.
4. **Recommendations** — propose reversible actions, owners, and verification steps.
5. **Tracking** — create follow-up ledger rows for unresolved items.
6. **Safety review** — confirm no protected source/canonical boundary was crossed.
7. **Final report** — summarize for Hermes/user decision; do not apply changes.

## Protected Source Rules

- Never create root `_workspace`.
- Never modify or upload `_Identity`, `_Philosophy`, Personal Thinking raw notes, Personal Inspiration originals, Eagle raw library, Work Files originals, `About Me`, `Storytelling_First`, or `Background_Before_Design`.
- Treat audit outputs as draft findings until Hermes verifies and the user approves any canonical action.
- Canonical absorption requires ReviewLedger entry and explicit user approval.

## Dry-Run Prompt

```text
Run designer-audit-report in read-only mode against the GitHub fork branch. Check whether the branch is ready for docs-only absorption. Use L1 unless findings require recommendations. Write only run artifacts; do not modify Designer_Univers canonical files.
```
