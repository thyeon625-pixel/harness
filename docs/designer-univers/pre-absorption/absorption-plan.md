# Absorption Plan: Designer_Univers Harness Layer

This plan covers a future movement from the GitHub fork branch into the canonical Designer_Univers workspace. It is not executed yet.

## Source

```text
repo: thyeon625-pixel/harness
branch: feat/designer-univers-harness
latest_known_commit: record-remote-sha-immediately-before-absorption
validated_scope: 10 first-priority detailed pilots
```

Before absorption, Hermes must update `latest_known_commit` to the actual remote SHA from:

```bash
git ls-remote --heads origin feat/designer-univers-harness
```

If the SHA in this plan does not match the branch head being absorbed, stop and re-run review.

## Absorption Principle

Absorb the **minimum validated subset**, not the whole fork. The fork remains the design/staging repository.

## Available Detailed Pilots

```text
designer-knowledge-base
designer-audit-report
designer-brand-identity
designer-visual-storytelling
designer-design-system
designer-space-concept-board
designer-market-research
designer-report-generator
designer-technical-writer
designer-operations-manual
```

## Recommended Stage Order

### Stage 0 — User Decision

Use `decision-package.md`, `absorption-scenarios.md`, and `decision-checklist.md`. No file copy happens in this stage.

### Stage 1 — Docs-Only Draft Copy, if approved

Copy only selected docs into:

```text
Designer Master/System/_drafts/harness-adaptation/
```

No runtime agent/skill activation.

### Stage 2 — Review Draft Copy

- Hermes validates copied files and paths.
- Claude Code reviews from the ReviewLedger or a dedicated review instruction.
- `safety-reviewer` / `designer_reviewer` checks safety boundaries.

### Stage 3 — Single Runtime Candidate, if later approved

Copy one selected skill/agent set into runtime candidate paths. Recommended first candidate, if any:

```text
designer-knowledge-base
```

Do not overwrite existing skills/agents without a diff and explicit approval.

### Stage 4 — Draft-Write Pilot Run

Run only under:

```text
Designer Master/System/Runs/{run_id}/
```

No Designer Earth, System/Rules, external service, or public output writes.

### Stage 5 — Promotion Decision

Only after pilot review, decide whether to promote any draft to Designer Earth, System/Rules, System/Templates, or runtime specs.

## Rollback

- Remove imported draft folder if no canonical files were changed.
- If runtime skills were copied, remove only those exact copied paths.
- If canonical files were changed, use ReviewLedger affected file list and baseline audit to revert.

## ReviewLedger Entry Requirements

Every actual absorption operation must append source repo/branch/commit, copied files, target files, verification commands/results, protected-source status, external review status, and rollback path.
