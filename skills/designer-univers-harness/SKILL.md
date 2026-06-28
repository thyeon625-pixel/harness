---
name: designer-univers-harness
description: "Use when adapting Harness or Harness-100 patterns for Designer_Univers. Converts Claude Code agent-team templates into a common Hermes/Claude/Codex-compatible harness while preserving Designer_Univers protected-source DNA, workspace separation, cost-aware Expert Pool routing, and ReviewLedger verification."
version: 0.1.0
author: Hermes Agent
license: Apache-2.0
platforms: [macos]
metadata:
  hermes:
    tags: [designer-univers, harness, agent-teams, governance, knowledge-management]
    related_skills: [harness]
---

# Designer_Univers Harness

## Overview

This skill adapts external Harness / Harness-100 team patterns into a Designer_Univers-safe, runtime-portable harness. It does not bulk import external `.claude/agents`, `.claude/skills`, `CLAUDE.md`, or `_workspace` conventions. It converts selected components into a common agent spec, injects protected-source rules, rewrites workspaces to the adopted Run/Draft/Knowledge/Rules separation, and routes tasks through a cost-aware Expert Pool.

## When to Use

Use this skill when:

- building a custom Designer_Univers harness;
- converting a Harness-100 candidate such as `knowledge-base-builder`, `brand-identity`, `visual-storytelling`, `design-system`, or `audit-report`;
- deciding whether an imported H100 agent duplicates an existing Hermes worker profile;
- rewriting root `_workspace` assumptions into `Designer Master/System/Runs/{run_id}`;
- adding protection, external-service, or cost rules to imported agent/skill drafts.

Do not use this skill to directly modify protected Identity/Philosophy files or to bulk-copy H100 into Designer_Univers.

## Required References

Load the following as needed:

- `references/common-agent-spec.md` for portable agent definitions.
- `references/hybrid-architecture.md` for the final integration spine.
- `references/workspace-policy.md` for adopted solution C.
- `references/protected-source-injection.md` for common and role-specific protection blocks.
- `references/external-service-policy.md` before any API/tool use.
- `references/cost-expert-pool-policy.md` before dispatching multiple agents.
- `references/harness-100-first-priority-candidates.md` when selecting candidates.
- `references/worker-profile-integration.md` before creating or renaming agents/workers.

## Workflow

1. **Classify the task.** Decide whether this is a new custom harness, an H100 conversion, or a review of existing Designer_Univers workers. Completion: task type and candidate source are named.
2. **Load Designer_Univers DNA.** Treat System/Rules and protected-source policy as higher priority than imported harness instructions. Completion: protected scope is identified.
3. **Choose the minimal expert set.** Apply the Expert Pool policy instead of defaulting to a full team. Completion: cost tier and selected experts are recorded.
4. **Convert agent specs.** Rewrite imported `.claude/agents/*.md` into the common agent spec. Completion: every agent has mission, inputs, outputs, protected rules, workspace rules, collaboration protocol, cost/tool policy, completion criteria, and failure handling.
5. **Rewrite workspace paths.** Replace `_workspace/` with `Designer Master/System/Runs/{run_id}/workspace`, and move promotion candidates into `promotion_candidates/` or `System/_drafts`. Completion: no root `_workspace` references remain.
6. **Inject protection and service rules.** Add common protected-source block plus role-specific restrictions; record external service mode. Completion: every agent/skill declares `external_services` and protected-source behavior.
7. **Map to existing workers.** Reuse `designer_reviewer`, `designer_docs`, `designer_works`, `research-analyst`, `eagle-curator`, `thinking-processor`, and `master-orchestrator` where appropriate. Completion: every role is mapped to keep/extend/new/defer.
8. **Verify before absorption.** Run Markdown/frontmatter checks, review changed files, and require Claude Code review + Hermes verification before project absorption. Completion: absorption checklist is complete.

## Verification Checklist

- [ ] No bulk H100 import occurred.
- [ ] Every skill uses `SKILL.md` if moved into Designer_Univers conventions.
- [ ] No imported instruction can write to protected sources by default.
- [ ] Root `_workspace/` is not used.
- [ ] Cost tier and Expert Pool selection are documented.
- [ ] Existing worker profiles were mapped before creating new agents.
- [ ] External services are `none`, `free-only`, or `approval-required`.
- [ ] Final project absorption remains gated by user approval.
