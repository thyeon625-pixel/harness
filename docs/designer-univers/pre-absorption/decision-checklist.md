# Absorption Decision Checklist

Use this checklist in the conversation before any canonical Designer_Univers write.

## Current Fork State

- [ ] Remote branch is `thyeon625-pixel/harness:feat/designer-univers-harness`.
- [ ] Remote SHA is recorded immediately before action.
- [ ] Local HEAD matches intended remote SHA.
- [ ] `python3 scripts/designer_univers_validate.py` passes.
- [ ] Claude CLI review result is saved under Agent_Orchestration review logs.

## User Decision

- [ ] User explicitly chose Scenario A, B, C, or D from `absorption-scenarios.md`.
- [ ] If Scenario B/C/D, exact source files are listed.
- [ ] If Scenario B/C/D, exact target paths are listed.
- [ ] User understands docs-only still means copying into Designer_Univers.
- [ ] User understands runtime activation is separate.

## Safety Gates

- [ ] No protected source will be modified.
- [ ] No raw image/source upload will occur.
- [ ] No external paid/private/API action will occur.
- [ ] No System/Rules change will occur unless specifically approved.
- [ ] No Designer Earth knowledge write will occur unless specifically approved.

## Operational Gates

- [ ] ReviewLedger entry plan exists.
- [ ] Rollback path exists.
- [ ] Baseline/manual verification command is selected if canonical files will change.
- [ ] Existing target files have been checked to avoid overwrite.

## Recommended Initial Approval Shape

If the user wants to proceed, the safest first approval should be:

```text
Approve Scenario B only: copy selected docs into Designer Master/System/_drafts/harness-adaptation/ for review. Do not install skills, agents, rules, or runtime automation.
```
