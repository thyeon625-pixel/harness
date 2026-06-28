# Existing Hermes Worker Profile Integration

Existing Hermes worker profiles are not discarded. They become the trusted runtime workforce under the Designer_Univers Harness Layer.

## Current Principle

- Harness describes **team architecture and task protocol**.
- Hermes worker profiles provide **actual bounded execution identities**.
- Claude Code remains reviewer/helper unless explicitly promoted for a task.

## Worker Profile Mapping

| Existing Worker / Agent | Status Under Harness Model | Notes |
|---|---|---|
| `designer_reviewer` | keep as first-line safety/review expert | maps to `safety-reviewer`, `audit-reviewer`, `identity-boundary-reviewer` |
| `designer_docs` | keep/extend as documentation/report expert | maps to `technical-writer`, `report-generator`, `operations-manual` roles |
| `designer_works` | keep/extend for Work Files and portfolio artifacts | maps to `works-archivist`, `personal-works-analyst` |
| `research-analyst` | keep; merge with H100 market/research patterns | avoid duplicate market-research agents |
| `eagle-curator` | keep; add protected Eagle raw-library rules | maps to visual/reference curator roles |
| `thinking-processor` | keep; strict Personal Thinking read-only | maps to identity/philosophy candidate processor |
| `master-orchestrator` | keep; may become harness router/orchestrator | must enforce cost and protection gates |

## Do Not Do

- Do not replace existing workers with H100 agents wholesale.
- Do not create duplicate agents with different names for the same role until the old/new responsibilities are compared.
- Do not let imported harnesses bypass Kanban/ReviewLedger/Hermes verification.

## Integration Plan

1. Convert selected H100 roles into generic role specs.
2. Map each role to an existing worker if possible.
3. Only create a new worker/agent when no existing role fits.
4. Update skills before changing worker profiles.
5. Test with read-only or draft-write pilot runs.
6. Promote only after Hermes verification and user approval.
