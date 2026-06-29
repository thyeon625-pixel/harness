# Designer_Univers Harness Decision Package

This file is the fork-side decision package for deciding whether any Designer_Univers harness artifacts should be absorbed into the canonical Dropbox workspace.

## Current Decision State

```text
source_repo: thyeon625-pixel/harness
source_branch: feat/designer-univers-harness
source_status: GitHub fork staging only
canonical_absorption_status: not approved / not performed
validator_target: detailed_harnesses=10
recommended_next_decision: review package first; do not absorb runtime artifacts yet
```

## What Is Complete in the Fork

All ten first-priority H100-derived harnesses are now detailed Designer_Univers staging pilots.

| Harness | Source | Purpose | Absorption posture |
|---|---|---|---|
| `designer-knowledge-base` | H100 64 knowledge-base-builder | knowledge base / Obsidian-compatible draft knowledge structure | docs only first; runtime skill later only after pilot |
| `designer-audit-report` | H100 94 audit-report | governance/protection audit package | docs only first; runtime skill optional later |
| `designer-brand-identity` | H100 06 brand-identity | identity-safe brand strategy drafts | docs only first; public/canonical use requires strict approval |
| `designer-visual-storytelling` | H100 15 visual-storytelling | visual narrative and portfolio story drafts | docs only first; no image generation by default |
| `designer-design-system` | H100 36 design-system | visual tokens and pattern principles | docs only first; no runtime code by default |
| `designer-space-concept-board` | H100 77 space-concept-board | spatial atmosphere / moodboard directions | docs only first; no raw image upload or purchasing |
| `designer-market-research` | H100 44 market-research | public/provided-source market research drafts | docs only first; paid/private research gated |
| `designer-report-generator` | H100 82 report-generator | internal report generation drafts | docs only first; no BI/ERP/DB integration |
| `designer-technical-writer` | H100 81 technical-writer | technical docs and diagram drafts | docs only first; no code/CI/hosting writes |
| `designer-operations-manual` | H100 92 operations-manual | SOP/process/training drafts | docs only first; no workflow/System Rules changes |

## Decision Options

### Option A — Continue GitHub-only staging

Meaning: keep all artifacts in the fork and do not copy anything into Designer_Univers.

Recommended when:

- user wants more review or refinement before Dropbox changes;
- target folder policy in Designer_Univers is not yet chosen;
- runtime/skill/agent activation questions are still open.

Effects:

- Canonical Designer_Univers remains untouched.
- Fork continues as design/staging source.
- Future work can refine docs, examples, or dry-runs.

### Option B — Docs-only absorption into a draft folder

Meaning: copy selected documentation into a clearly temporary Designer_Univers draft/review area, with no runtime activation.

Candidate target:

```text
Designer Master/System/_drafts/harness-adaptation/
```

Allowed contents for docs-only:

```text
docs/designer-univers/README.md
docs/designer-univers/custom-harnesses/README.md
docs/designer-univers/custom-harnesses/*/HARNESS.md
docs/designer-univers/common-agent-spec.md
docs/designer-univers/workspace-policy.md
docs/designer-univers/protected-source-injection.md
docs/designer-univers/external-service-policy.md
docs/designer-univers/cost-expert-pool-policy.md
docs/designer-univers/expert-pool-router-design.md
docs/designer-univers/pre-absorption/*.md
```

Explicitly excluded from docs-only:

```text
skills/**/SKILL.md as installed runtime skills
custom-harnesses/*/agents/*.md as active .claude/agents
System/Rules changes
Designer Earth knowledge writes
launchd/cron/gateway changes
external service credentials or account setup
```

### Option C — Runtime pilot candidate after docs-only review

Meaning: after docs-only review, copy one selected harness skill/agent set as a bounded runtime candidate and run it only under `System/Runs`.

Recommended first runtime candidate if approved later:

```text
designer-knowledge-base
```

Why:

- it has the oldest detailed pilot;
- it includes shared `safety-reviewer`;
- it is naturally draft-write and can avoid canonical writes.

Hard gates:

- explicit user approval;
- ReviewLedger entry;
- source remote SHA recorded immediately before copy;
- Hermes baseline/check verification;
- rollback path prepared;
- no protected-source mutation.

## Recommended Current Decision

Do **not** absorb yet unless the user explicitly wants a Dropbox draft copy now.

Recommended immediate next state:

```text
Option A: continue GitHub-only staging, or pause for user review.
```

If the user wants to move forward, choose Option B first. Do not jump directly to Option C.

## User Decision Questions

Before any absorption, answer these in plain terms:

1. Should anything be copied into Designer_Univers now, or should the fork remain the only staging area?
2. If copying, should it be docs-only into `_drafts/harness-adaptation/`?
3. Which files are allowed to copy?
4. Should runtime skills/agents remain excluded for now?
5. Should the first later runtime pilot, if any, be `designer-knowledge-base` only?

## Verification Required Before Acting

Run from the fork:

```bash
git fetch origin feat/designer-univers-harness
REMOTE_SHA=$(git ls-remote --heads origin feat/designer-univers-harness | awk '{print $1}')
git rev-parse HEAD
python3 scripts/designer_univers_validate.py
```

Stop if local HEAD does not match the intended remote SHA.
