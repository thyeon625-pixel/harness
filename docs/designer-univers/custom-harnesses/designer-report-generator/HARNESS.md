# designer-report-generator

## Source

Derived from Harness-100 `H100/ko/82-report-generator` as a Designer_Univers-specific staging harness. This is not a direct import.

## Purpose

Generate internal Designer_Univers reports from approved data, run artifacts, research summaries, and analysis notes without connecting live BI/ERP or publishing by default.

## Default Routing

```yaml
harness: designer-report-generator
source: H100/ko/82-report-generator
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; public lookup or data tools require explicit route approval; live BI/ERP/database integration out of scope
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping |
|---|---|---|
| `data-collector` | collect and normalize provided/public evidence into a source log | research-analyst |
| `analysis-synthesizer` | turn collected data into trends, findings, and implications | designer_docs |
| `visualization-planner` | chart/table/diagram specifications, not dashboard implementation by default | visual-language-reviewer |
| `report-writer` | full report structure and prose | designer_docs |
| `executive-summarizer` | executive summary, consistency checks, decision points | designer_reviewer |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “요약 보고서” | L1 | report-writer, executive-summarizer |
| “제공 데이터 분석 보고서” | L1-L2 | data-collector, analysis-synthesizer, report-writer |
| “시각화 명세 포함” | L2 | analysis-synthesizer, visualization-planner, report-writer, executive-summarizer |
| “경영/공개 후보 보고서” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_data_collection.md
Designer Master/System/Runs/{run_id}/workspace/02_analysis_synthesis.md
Designer Master/System/Runs/{run_id}/workspace/03_visualization_spec.md
Designer Master/System/Runs/{run_id}/workspace/04_report_draft.md
Designer Master/System/Runs/{run_id}/review/05_executive_summary.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_final_report_candidate.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Frame** — Frame audience, decision, period, source set, and data limitations.
2. **Collect** — Collect provided/public evidence into a traceable source log.
3. **Synthesize** — Synthesize analysis and chart/table specifications without building live dashboards.
4. **Draft** — Draft report and executive summary with uncertainty labels.
5. **Safety** — Safety review before promotion, sharing, or canonical absorption.

## Protected Source Rules

- Never create root `_workspace`.
- Protected sources are read-only: `_Identity`, `_Philosophy`, `Personal Thinking`, `Personal Inspiration Sources`, Eagle raw library, Work Files originals, and identity/philosophy files.
- Do not upload protected/private files, raw images, credentials, or account data to external services without explicit user approval.
- Distinguish evidence, interpretation, proposal, and approved knowledge.
- Canonical absorption requires ReviewLedger entry, Hermes verification, and explicit user approval.
- Do not connect live BI, ERP, databases, or private accounts by default.
- Do not present estimates as facts; label missing data and assumptions.
- Report candidates remain draft artifacts until Hermes verification and user approval.

## Dry-Run Prompt

```text
Run designer-report-generator in draft-write mode using only provided/public approved inputs. Write artifacts only under System/Runs paths. Do not modify canonical Designer_Univers files.
```
