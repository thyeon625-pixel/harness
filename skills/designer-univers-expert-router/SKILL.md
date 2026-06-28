---
name: designer-univers-expert-router
description: "Use when routing Designer_Univers harness work through a cost-aware Expert Pool. Selects the smallest safe expert set, assigns L0-L3 cost tier, enforces protected-source and external-service gates, and writes all execution artifacts to System/Runs rather than root _workspace."
version: 0.1.0
author: Hermes Agent
license: Apache-2.0
platforms: [macos]
metadata:
  hermes:
    tags: [designer-univers, expert-pool, routing, cost-control, governance]
    related_skills: [designer-univers-harness]
---

# Designer_Univers Expert Router

## Overview

This skill is the router layer for Designer_Univers custom harnesses. It prevents the default Harness failure mode of launching a full team for every task. It selects only the experts needed for the current task, records the cost tier, and enforces protected-source and external-service gates before any worker or Claude Code task is dispatched.

## When to Use

Use this skill before:

- converting any Harness-100 candidate into a project-specific run;
- dispatching multiple agents/workers;
- touching protected-source context;
- using public web, private GitHub, image generation, or any API/service;
- deciding whether to run a mini harness or full team.

## Routing Steps

1. **Classify task risk.** Identify source paths, protected-source involvement, requested output, and whether external services are needed. Completion: risk is `low`, `medium`, or `high`.
2. **Assign cost tier.** Start at L0 and raise only when synthesis, protected context, or official promotion requires it. Completion: tier is L0-L3 with a one-line reason.
3. **Select experts.** Choose the smallest useful set from the Expert Pool. Completion: every selected and excluded expert has a reason.
4. **Set workspace.** Create or reference `Designer Master/System/Runs/{run_id}`. Completion: no root `_workspace` path is used.
5. **Gate external services.** If service use is not `none` or `free-only`, stop and call the user. Completion: `external_services.policy` is recorded.
6. **Dispatch or block.** Dispatch only if mode/path/cost/protection gates are satisfied. Completion: next action is `dispatch`, `needs_user_call`, or `blocked`.

## Cost Tiers

| Tier | Pattern | Gate |
|---|---|---|
| L0 | Hermes direct / single expert | no protected interpretation, no broad synthesis |
| L1 | 2-3 experts | bounded analysis or draft proposal |
| L2 | 4-5 experts | important synthesis or design/knowledge architecture |
| L3 | full + review/rework | official governance, protected promotions, large structural change |

## Expert Pool

| Expert | Default Runtime |
|---|---|
| harness-router | Hermes / master-orchestrator |
| safety-reviewer | designer_reviewer |
| knowledge-collector | source-specific existing worker |
| taxonomy-designer | designer_docs or new draft role |
| wiki-builder | designer_docs |
| search-optimizer | designer_docs + scripts |
| maintenance-planner | designer_docs + designer_reviewer |
| visual-language-reviewer | eagle-curator / future visual worker |
| identity-lens-reviewer | thinking-processor + designer_reviewer |
| research-analyst | existing research-analyst |
| cost-controller | Hermes direct |

## Output Template

```yaml
routing_decision:
  task_summary:
  risk:
  cost_tier:
  mode:
  run_id:
  selected_experts: []
  excluded_experts: {}
  external_services:
    policy: none
    user_call_required: false
  protected_sources:
    involved: false
    safety_reviewer_required: false
  next_action: dispatch | needs_user_call | blocked
```

## Verification Checklist

- [ ] The selected team is smaller than full team unless full team is justified.
- [ ] Protected-source tasks include safety review.
- [ ] External services are recorded as `none`, `free-only`, or `approval-required`.
- [ ] Root `_workspace` is not used.
- [ ] The router decision can be copied into `run_manifest.yaml`.
