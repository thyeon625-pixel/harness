# Cost Policy + Expert Pool

Designer_Univers adopts a cost-aware Expert Pool model. The system does not launch a full five-agent team for every task. A router/orchestrator selects the smallest useful expert set.

## Cost Tiers

| Tier | Execution Pattern | Use For |
|---|---|---|
| L0 | Hermes/direct/single lightweight agent | trivial classification, file inventory, simple summary |
| L1 | mini harness, 2-3 experts | bounded analysis, small batch review, draft taxonomy |
| L2 | standard harness, 4-5 experts | important synthesis, brand/knowledge architecture, design language extraction |
| L3 | standard harness + rework + independent review | governance changes, protected-scope decisions, official promotions |

## Expert Pool Integration

Instead of fixed teams, every custom Designer_Univers harness should define:

```yaml
expert_pool:
  required_core:
    - orchestrator
    - safety-reviewer
  optional_experts:
    - visual-reference-analyst
    - identity-lens-reviewer
    - knowledge-taxonomist
    - works-archivist
    - research-analyst
    - cost-controller
  selection_rule: choose the minimal set needed for the input and risk tier
```

## Router Rules

1. Start at L0 unless task risk or complexity requires more.
2. If protected sources are involved, include `safety-reviewer` even for small runs.
3. If the task is broad but low risk, use sampling before full analysis.
4. If external API use may cost money, stop and request user approval.
5. If a previous run already produced useful artifacts, read them before re-running experts.
6. Full team execution requires a reason in `run_manifest.yaml`.

## Practical Token Guardrails

Use these planning estimates as rough token budgets, not prices:

| Scenario | Approx. Tokens |
|---|---:|
| L0 direct | 3k-15k |
| L1 2-3 experts | 25k-60k |
| L2 4-5 experts | 80k-150k |
| L3 with rework/review | 180k-400k+ |

## Batch Strategy

For large reference/material sets:

```text
inventory → sample → cluster → expert review on representative clusters → promote patterns → only then deep-dive selected items
```

Do not run a full expert team separately for every image, note, or work file.
