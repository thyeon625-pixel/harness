# Absorption Plan: Designer_Univers Harness Layer

This plan covers the future movement from the GitHub fork branch into the canonical Designer_Univers workspace. It is not executed yet.

## Source

```text
repo: thyeon625-pixel/harness
branch: feat/designer-univers-harness
latest_known_commit: record-remote-sha-immediately-before-absorption
```

Before absorption, Hermes must update `latest_known_commit` to the actual remote SHA from:

```bash
git ls-remote --heads origin feat/designer-univers-harness
```

This is the same remote-source verification required by `hermes-review-protocol.md` Step 1. If the SHA in this plan does not match the branch head being absorbed, stop and re-run review.

## Absorption Principle

Absorb the **minimum validated subset**, not the whole fork. The fork remains the design/staging repository.

## Target Paths

| Source Artifact | Future Target | Absorption Mode |
|---|---|---|
| `docs/designer-univers/target-structure-current-aware.md` | `Designer Master/System/_drafts/harness-adaptation/` | draft only |
| `docs/designer-univers/expert-pool-router-design.md` | `Designer Master/System/_drafts/harness-adaptation/` then maybe `System/Rules` | draft then approval |
| `docs/designer-univers/custom-harnesses/designer-knowledge-base/` | `Designer Master/System/Harnesses/designer-knowledge-base/` | staged harness |
| `skills/designer-univers-expert-router/SKILL.md` | `Designer Master/.claude/skills/designer-univers-expert-router/SKILL.md` | runtime skill candidate |
| `skills/designer-univers-knowledge-base/SKILL.md` | `Designer Master/.claude/skills/designer-univers-knowledge-base/SKILL.md` | runtime skill candidate |
| converted agents under `designer-knowledge-base/agents/` | only selected `.claude/agents/` or worker docs | after mapping |

## Stages

### Stage 1 — Draft Import

Copy only docs into `Designer Master/System/_drafts/harness-adaptation/`. No runtime agent/skill activation yet.

### Stage 2 — Review

- Hermes validates files and paths.
- Claude Code reviews from `_ReviewLedger.md` or a dedicated review instruction.
- `designer_reviewer` checks safety boundaries.

### Stage 3 — Runtime Candidate

Copy selected skills into `.claude/skills/` with `SKILL.md` names. Do not overwrite existing skills without a diff.

### Stage 4 — Pilot Run

Run `designer-univers-knowledge-base` in draft-write mode only under `Designer Master/System/Runs/{run_id}/`. No Designer Earth or System/Rules writes.

### Stage 5 — Promotion Decision

Only after pilot review, decide whether to promote any draft to Designer Earth, System/Rules, System/Templates, or runtime specs.

## Rollback

- Remove imported draft folder if no canonical files were changed.
- If runtime skills were copied, remove only those exact copied paths.
- If canonical files were changed, use ReviewLedger affected file list and baseline audit to revert.

## ReviewLedger Entry Requirements

Every actual absorption operation must append source repo/branch/commit, copied files, target files, verification commands/results, protected-source status, external review status, and rollback path.
