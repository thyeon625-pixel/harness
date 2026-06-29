---
name: designer-univers-knowledge-base
description: "Use when building, auditing, or improving the Designer_Univers knowledge base. Converts Harness-100 knowledge-base-builder into a safe Designer_Univers workflow: Expert Pool routing, protected-source read-only handling, System/Runs workspace, taxonomy/index drafts, and ReviewLedger-ready promotion candidates."
version: 0.1.0
author: Hermes Agent
license: Apache-2.0
platforms: [macos]
metadata:
  hermes:
    tags: [designer-univers, knowledge-base, obsidian, taxonomy, harness]
    related_skills: [designer-univers-harness, designer-univers-expert-router]
---

# Designer_Univers Knowledge Base Harness

## Overview

This is the first detailed Designer_Univers custom harness, adapted from Harness-100 `64-knowledge-base-builder`. It builds inventories, taxonomy proposals, draft wiki/index artifacts, search metadata, and maintenance plans while preserving the Designer_Univers DNA and protected-source boundaries.

It is a **staged harness**, not a direct writer into Designer Earth. All work starts in `Designer Master/System/Runs/{run_id}`. Official absorption into Designer Earth or System/Rules requires Hermes verification and user approval.

## When to Use

Use this skill when the user asks to:

- organize the Designer_Univers knowledge base;
- create or audit Obsidian indexes, MOCs, tags, taxonomy, or search maps;
- convert analysis outputs into durable Markdown knowledge proposals;
- review whether existing notes/rules/skills are discoverable and maintainable;
- plan maintenance cadence, ownership, or quality checks for Designer Earth / Designer Master documentation.

Do not use it to directly edit protected Identity/Philosophy files, move raw Personal Thinking notes, restructure Eagle raw library, or bulk rewrite Designer Earth.

## Required References

When this skill is installed before docs-only absorption, these references may still live only in the GitHub fork. Use them as source references from the fork until the user separately approves docs-only copying into Designer_Univers.

- `docs/designer-univers/custom-harnesses/designer-knowledge-base/HARNESS.md`
- `docs/designer-univers/expert-pool-router-design.md`
- `docs/designer-univers/workspace-policy.md`
- `docs/designer-univers/protected-source-injection.md`
- `docs/designer-univers/worker-profile-integration.md`

## Workflow

1. **Route.** Use `designer-univers-expert-router` to assign cost tier and experts. Completion: a routing decision exists.
2. **Create run manifest.** Use `Designer Master/System/Runs/{run_id}/run_manifest.yaml`. Completion: mode, cost tier, selected experts, protected-source involvement, and external-service policy are recorded.
3. **Inventory.** Run `knowledge-collector` on approved source paths. Completion: `workspace/01_source_inventory.md` exists.
4. **Taxonomy.** Run `taxonomy-designer` only after inventory. Completion: `workspace/02_taxonomy_draft.md` distinguishes existing structure from proposals.
5. **Knowledge map and search plan.** Run `wiki-builder` and `search-optimizer` in L1/L2 modes. Completion: `workspace/03_knowledge_map.md` and `workspace/04_search_index_plan.md` exist.
6. **Maintain.** Run `maintenance-planner` for lifecycle and quality controls. Completion: `workspace/05_maintenance_plan.md` exists.
7. **Review.** Run `safety-reviewer` whenever protected sources or promotion candidates are involved. Completion: review output lists pass/fail and required fixes.
8. **Report.** Hermes summarizes outputs and next steps. Completion: no canonical file changes are claimed unless separately applied and verified.

## Expert Pool Modes

| Mode | Cost | Experts |
|---|---|---|
| Inventory | L0-L1 | router, knowledge-collector |
| Taxonomy Proposal | L1 | router, knowledge-collector, taxonomy-designer |
| Index/Wiki Draft | L1-L2 | router, taxonomy-designer, wiki-builder, search-optimizer |
| Maintenance Plan | L1 | router, maintenance-planner, safety-reviewer if policy impact |
| Official Absorption Proposal | L3 | router, relevant experts, safety-reviewer, Claude review, Hermes verification |

## Path Contract

```text
Designer Master/System/Runs/{run_id}/
├── run_manifest.yaml                    # optional for non-synthetic runs
├── workspace/
│   ├── 00_input.md
│   ├── 01_source_inventory.md
│   ├── 02_taxonomy_draft.md
│   ├── 03_knowledge_map.md
│   ├── 04_search_index_plan.md
│   └── 05_maintenance_plan.md
├── review/
│   ├── 06_safety_review.md
│   └── 08_hermes_verification.md         # created by Hermes when verifying a pilot
├── outputs/
│   └── 07_knowledge_base_draft.md
└── promotion_candidates/
    └── README.md                         # gate notes; may contain zero candidates
```

## Common Pitfalls

1. **Treating taxonomy proposal as official structure.** Keep proposals in Runs/Drafts until approved.
2. **Using root `_workspace`.** This is prohibited; use System/Runs.
3. **Overwriting existing Obsidian notes.** Draft new candidates instead.
4. **Letting H100 names duplicate existing workers.** Map to current worker profiles first.
5. **Running full team by default.** Use Expert Pool routing and start small.

## Verification Checklist

- [ ] Run manifest exists and records cost/expert/protection decisions.
- [ ] No protected source was modified, moved, renamed, deleted, or uploaded.
- [ ] No root `_workspace` was used.
- [ ] Outputs separate inventory, interpretation, proposal, and promotion candidate.
- [ ] Existing workers were reused or explicitly marked as needing a new role.
- [ ] Canonical absorption is not performed without later user approval.
