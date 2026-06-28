# Designer_Univers Expert Pool Router Design

This document turns the cost policy into an executable harness design. The router is the first step of every Designer_Univers custom harness: it selects the smallest useful expert set, assigns a cost tier, and blocks unsafe external-service/protected-source use.

## Router Inputs

```yaml
task_summary: string
source_paths: []
requested_output: inventory | taxonomy | draft | report | review | promotion
protected_sources_involved: true | false | unknown
external_services_requested: []
urgency: normal | high
user_cost_preference: conserve | balanced | quality
```

## Router Outputs

```yaml
cost_tier: L0 | L1 | L2 | L3
mode: read-only | draft-write | approved-write
selected_experts: []
blocked_reasons: []
run_workspace: Designer Master/System/Runs/{run_id}/workspace
requires_user_call: true | false
review_required: true | false
```

## Expert Pool

| Expert | Maps To Existing Worker/Agent | Use When |
|---|---|---|
| harness-router | `master-orchestrator` | every run; selects tier/mode/experts |
| safety-reviewer | `designer_reviewer` | any protected source, official promotion, deletion/move risk |
| knowledge-collector | existing workers by source type | inventory across notes, rules, logs, work files |
| taxonomy-designer | new role or `designer_docs` extension | category/tag/navigation/schema work |
| wiki-builder | `designer_docs` | draft markdown pages or index proposals |
| search-optimizer | `designer_docs` + deterministic scripts | indexes, aliases, link maps, search metadata |
| maintenance-planner | `designer_docs` + `designer_reviewer` | lifecycle, update rhythm, RACI, audit cadence |
| visual-language-reviewer | `eagle-curator` + future visual expert | image/reference/design-language synthesis |
| identity-lens-reviewer | `thinking-processor` + `designer_reviewer` | identity/philosophy fit without editing protected files |
| research-analyst | existing `research-analyst` | external research, market/trend evidence |
| cost-controller | Hermes direct | token/API use is ambiguous or potentially paid |

## Routing Matrix

| Task Pattern | Default Tier | Experts |
|---|---|---|
| file/folder inventory only | L0 | harness-router or Hermes direct |
| classify existing analysis notes | L1 | knowledge-collector, taxonomy-designer |
| build/update wiki draft | L1-L2 | knowledge-collector, taxonomy-designer, wiki-builder, search-optimizer |
| protected-source interpretation | L2 | identity-lens-reviewer, safety-reviewer, relevant source expert |
| official rules/governance change | L3 | harness-router, safety-reviewer, maintenance-planner, independent reviewer |
| bulk inspiration analysis | L1 first | inventory/sampling; add visual-language-reviewer only for selected clusters |
| market/trend report | L1-L2 | research-analyst, report-generator, safety-reviewer if DNA impact |

## Dispatch Rules

1. Start L0 unless the task requires synthesis or protected-source reasoning.
2. Add `safety-reviewer` whenever protected sources are read or promotion is proposed.
3. Add `cost-controller` before paid APIs, private repo access, or image generation.
4. Full five-expert execution requires a `full_team_reason` in `run_manifest.yaml`.
5. If a previous run exists for the same topic, read it before dispatching new experts.
6. The router never writes to Designer Earth or System/Rules directly; it writes only to `System/Runs` or proposes `System/_drafts` candidates.

## Run Manifest Additions

```yaml
routing:
  router: harness-router
  cost_tier: L1
  selected_experts:
    - knowledge-collector
    - taxonomy-designer
    - safety-reviewer
  excluded_experts:
    wiki-builder: "not needed; no page generation requested"
  full_team_reason: null
  user_call_required: false
```
