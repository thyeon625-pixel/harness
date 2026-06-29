# Absorption Scenarios

This file gives user-facing choices for what can happen next. It is not an approval.

## Scenario A — Pause at GitHub Fork

```text
Action: none in Designer_Univers
Risk: lowest
Recommended now: yes
```

Use when the user wants to review or refine more before Dropbox changes.

Verification:

```bash
python3 scripts/designer_univers_validate.py
```

## Scenario B — Docs-Only Draft Copy

```text
Action: copy selected docs to Designer Master/System/_drafts/harness-adaptation/
Risk: low
Runtime activation: no
Recommended if user wants local review in Designer_Univers: yes
```

Allowed:

- overview/policy docs;
- custom harness `HARNESS.md` files;
- pre-absorption decision package;
- optional agent specs as documentation-only under a draft folder.

Not allowed:

- `.claude/skills` install;
- `.claude/agents` install;
- System/Rules edits;
- Designer Earth writes;
- external service setup.

## Scenario C — Single Runtime Pilot Candidate

```text
Action: after Scenario B review, install one bounded candidate for a draft-only pilot
Risk: medium
Runtime activation: limited
Recommended now: no
```

Candidate later:

```text
designer-knowledge-base
```

Required approvals:

- exact files to copy;
- exact target paths;
- exact run mode;
- rollback plan;
- ReviewLedger entry;
- protected-source verification.

## Scenario D — Full Runtime Absorption

```text
Action: install multiple skills/agents and rules
Risk: high
Recommended now: no
```

Do not do this from the current package. Full runtime absorption should be a separate project after at least one successful bounded pilot.
