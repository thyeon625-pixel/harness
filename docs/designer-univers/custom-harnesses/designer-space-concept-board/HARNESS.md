# designer-space-concept-board

## Source

Derived from Harness-100 `77-space-concept-board` as a Designer_Univers-specific scaffold. This is not a direct import.

## Purpose

spatial mood, material, color, and atmosphere synthesis.

## Default Routing

```yaml
harness: designer-space-concept-board
default_cost_tier: L1
mode: draft-write
workspace: Designer Master/System/Runs/{run_id}/workspace
external_services: free-only
protected_scope: strict
```

## Expert Pool

- `style-analyst`
- `moodboard-designer`
- `material-curator`
- `budget-free-curator`
- `concept-reviewer`

Always add `safety-reviewer` when protected sources are read or any official promotion is proposed.

## Output Policy

- Intermediate outputs: `System/Runs/{run_id}/workspace`
- Reviewed outputs: `System/Runs/{run_id}/outputs`
- Promotion candidates: `System/Runs/{run_id}/promotion_candidates`
- Canonical absorption: only after Hermes verification and user approval

## Conversion Tasks Before Use

- [ ] Convert all selected agents to common-agent-spec.
- [ ] Replace root `_workspace` with `System/Runs`.
- [ ] Inject protected-source rules.
- [ ] Map experts to existing worker profiles.
- [ ] Add tests or dry-run prompts.
- [ ] Run Claude Code review and Hermes verification.
