# Workspace Policy: Adopted Solution C

This policy replaces upstream Harness root `_workspace/` assumptions for Designer_Univers.

## Adopted Separation

```text
Designer Master/System/Runs/      # execution artifacts and intermediate outputs
Designer Master/System/_drafts/   # canonical-change proposals and promotion candidates
Designer Earth/                   # approved durable knowledge
Designer Master/System/Rules/     # official governance rules
```

## Prohibited

- Do not create or use `Designer_Univers/_workspace/`.
- Do not write harness outputs directly to `Designer Earth` unless the user has approved a specific promotion.
- Do not write canonical rule changes directly from an imported harness.
- Do not store protected-source extracts in an unscoped shared folder.

## Run Directory Contract

Every run must use:

```text
Designer Master/System/Runs/{YYYYMMDD_HHMMSS}_{short-task}/
├── run_manifest.yaml
├── input/
├── workspace/
├── outputs/
├── review/
└── promotion_candidates/
```

## `run_manifest.yaml`

Minimum fields:

```yaml
run_id: YYYYMMDD_HHMMSS_short-task
harness: designer-knowledge-base
actor: hermes | claude-code | worker | codex
mode: read-only | draft-write | approved-write
cost_tier: L0 | L1 | L2 | L3
external_services: none | free-only | approval-required
protected_sources_read: []
protected_sources_modified: []   # must remain empty unless separately approved
output_policy: run-only | draft-candidate | knowledge-promotion-candidate
review_required: true
ledger_entry_required: true
```

## Promotion Flow

```text
Runs/workspace
→ Runs/outputs
→ Runs/review
→ Runs/promotion_candidates
→ System/_drafts, if proposal is needed
→ Designer Earth or System/Rules only after user approval
```

## Cleanup Policy

Runs are not automatically deleted. They may be archived or pruned only after:

1. outputs are either promoted or marked obsolete,
2. protected-source excerpts are checked,
3. ReviewLedger records the cleanup decision,
4. user approves deletion if canonical project files are affected.
