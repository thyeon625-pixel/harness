# Docs-Only Absorption Candidates

This file defines the maximum safe docs-only candidate set. It does not approve copying. It exists so the user can decide scope before any canonical Designer_Univers write.

## Docs-Only Means

Docs-only absorption means copying documentation to a draft/review location in Designer_Univers. It does **not** install runtime skills, activate agents, modify System/Rules, or write Designer Earth knowledge.

## Candidate Target

```text
Designer Master/System/_drafts/harness-adaptation/
```

## Candidate Files

### Core overview and policy docs

```text
DESIGNER_UNIVERS.md
docs/designer-univers/README.md
docs/designer-univers/common-agent-spec.md
docs/designer-univers/target-structure-current-aware.md
docs/designer-univers/workspace-policy.md
docs/designer-univers/protected-source-injection.md
docs/designer-univers/external-service-policy.md
docs/designer-univers/cost-expert-pool-policy.md
docs/designer-univers/expert-pool-router-design.md
docs/designer-univers/worker-profile-integration.md
docs/designer-univers/harness-100-first-priority-candidates.md
```

### Custom harness documentation

```text
docs/designer-univers/custom-harnesses/README.md
docs/designer-univers/custom-harnesses/*/HARNESS.md
```

### Pre-absorption package

```text
docs/designer-univers/pre-absorption/README.md
docs/designer-univers/pre-absorption/decision-package.md
docs/designer-univers/pre-absorption/docs-only-candidates.md
docs/designer-univers/pre-absorption/non-absorption-boundaries.md
docs/designer-univers/pre-absorption/absorption-scenarios.md
docs/designer-univers/pre-absorption/decision-checklist.md
docs/designer-univers/pre-absorption/absorption-plan.md
docs/designer-univers/pre-absorption/absorption-readiness-checklist.md
docs/designer-univers/pre-absorption/dry-run-scenarios.md
docs/designer-univers/pre-absorption/claude-review-request.md
docs/designer-univers/pre-absorption/hermes-review-protocol.md
docs/designer-univers/pre-absorption/validation-report.md
```

## Excluded from Docs-Only

```text
skills/**/SKILL.md
custom-harnesses/*/agents/*.md as active agents
.claude/**
.agents/**
.codex/**
System/Rules/**
System/Templates/**
System/Scripts/**
Designer Earth/**
Personal Inspiration Sources/**
Eagle library files
Work Files originals
```

Agent spec markdown may be copied as documentation only if it stays under `_drafts/harness-adaptation/agent-specs/` and is not placed in `.claude/agents`.

## Safety Conditions

- Copy only after explicit user approval.
- Record source repo/branch/SHA.
- Append ReviewLedger entry in the actual absorption operation.
- Do not overwrite existing canonical files.
- Do not promote anything from `_drafts` without a second approval.
