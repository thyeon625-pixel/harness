# designer-operations-manual

## Source

Derived from Harness-100 `H100/ko/92-operations-manual` as a Designer_Univers-specific staging harness. This is not a direct import.

## Purpose

Draft operational manuals, SOPs, process maps, FAQ/troubleshooting, and training materials for Designer_Univers workflows without changing the workflows themselves by default.

## Default Routing

```yaml
harness: designer-operations-manual
source: H100/ko/92-operations-manual
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; system changes, automations, credentials, or account actions require explicit approval
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping |
|---|---|---|
| `document-analyst` | analyze provided docs/processes and extract process inventory | designer_docs |
| `flowchart-designer` | Mermaid process maps, RACI, decision flow specs | visual-language-reviewer |
| `manual-writer` | step-by-step SOPs, checklists, role instructions | designer_docs |
| `faq-builder` | FAQ, troubleshooting, escalation trees | designer_docs |
| `training-producer` | training outline, quizzes, practice tasks, onboarding summary | designer_docs |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “프로세스 분석만” | L1 | document-analyst, flowchart-designer |
| “절차서/SOP 작성” | L1 | document-analyst, manual-writer, faq-builder |
| “FAQ/교육자료 추가” | L1-L2 | faq-builder, training-producer |
| “운영 매뉴얼 전체” | L2 | selected team + concept/technical review |
| “공식 운영 규칙 후보” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_document_analysis.md
Designer Master/System/Runs/{run_id}/workspace/02_process_flowcharts.md
Designer Master/System/Runs/{run_id}/workspace/03_step_by_step_manual.md
Designer Master/System/Runs/{run_id}/workspace/04_faq_troubleshooting.md
Designer Master/System/Runs/{run_id}/review/05_training_materials.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_operations_manual_candidate.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Frame** — Frame process scope, source materials, audience, and whether this is documentation-only.
2. **Analyze** — Analyze existing docs/processes and extract inventory, terms, risks, and unknowns.
3. **Draft** — Draft flowcharts, SOPs, FAQ, and training materials as proposals.
4. **Review** — Review for consistency with actual governance and mark gaps or [field verification needed].
5. **Safety** — Safety review and approval before official rules or workflow changes.

## Protected Source Rules

- Never create root `_workspace`.
- Protected sources are read-only: `_Identity`, `_Philosophy`, `Personal Thinking`, `Personal Inspiration Sources`, Eagle raw library, Work Files originals, and identity/philosophy files.
- Do not upload protected/private files, raw images, credentials, or account data to external services without explicit user approval.
- Distinguish evidence, interpretation, proposal, and approved knowledge.
- Canonical absorption requires ReviewLedger entry, Hermes verification, and explicit user approval.
- Documentation does not change operations; official workflow changes require separate approval.
- Do not edit System/Rules, credentials, automations, or launchd/cron configs by default.
- If source truth is unclear, record interview questions and verification gaps rather than inventing process facts.

## Dry-Run Prompt

```text
Run designer-operations-manual in draft-write mode using only provided/public approved inputs. Write artifacts only under System/Runs paths. Do not modify canonical Designer_Univers files.
```
