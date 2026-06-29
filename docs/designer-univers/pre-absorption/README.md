# Pre-Absorption Package

This package defines what must be understood before any Designer_Univers harness artifact is absorbed into the canonical Dropbox workspace.

## Contents

- `decision-package.md` — current decision summary and recommended next decision.
- `docs-only-candidates.md` — maximum safe docs-only candidate set.
- `non-absorption-boundaries.md` — what remains explicitly excluded until later approval.
- `absorption-scenarios.md` — Scenario A/B/C/D choices for the user.
- `decision-checklist.md` — final user decision checklist before any canonical write.
- `absorption-readiness-checklist.md` — detailed readiness checklist before absorption.
- `absorption-plan.md` — staged plan for moving from fork to Designer_Univers body.
- `dry-run-scenarios.md` — scenarios to test custom harness behavior without touching canonical files.
- `claude-review-request.md` — copy-ready prompt for Claude Code review.
- `hermes-review-protocol.md` — Hermes verification procedure.
- `sample-run-manifest.yaml` — manifest template for System/Runs execution.
- `validation-report.md` — generated/updated validation summary.

## Current Rule

Fork artifacts are staging outputs. They are not canonical Designer_Univers rules until absorbed through an explicit user decision, recorded source SHA, Hermes verification, and ReviewLedger entry.

## Current Recommendation

Do not absorb runtime artifacts yet. If the user wants to move forward, start with Scenario B: docs-only draft copy into `Designer Master/System/_drafts/harness-adaptation/`.
