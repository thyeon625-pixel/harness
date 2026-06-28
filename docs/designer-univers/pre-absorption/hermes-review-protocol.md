# Hermes Review Protocol Before Absorption

Hermes performs this protocol after fork validation and before any canonical Designer_Univers absorption.

## Step 1 — Verify Remote Source

Confirm branch exists remotely, confirm latest commit SHA, and fetch raw files for representative artifacts.

## Step 2 — Run Fork Validator

```bash
python3 scripts/designer_univers_validate.py
```

The validator must pass before absorption.

## Step 3 — Review Safety Invariants

- No root `_workspace` positive instruction.
- No direct Designer Earth write in fork instructions.
- No direct System/Rules write without approval gate.
- Every custom harness has protected-source rules or points to them.
- Every runtime skill has valid frontmatter.

## Step 4 — Review Worker Mapping

Existing workers are reused where possible. `designer_reviewer` remains safety reviewer. Hermes remains primary operator/ledger keeper.

## Step 5 — Prepare ReviewLedger Draft

Before actual absorption, prepare but do not append until copying occurs.

## Step 6 — User Approval Gate

Even if the fork is ready, canonical absorption requires explicit user approval because it writes into Designer_Univers project files.
