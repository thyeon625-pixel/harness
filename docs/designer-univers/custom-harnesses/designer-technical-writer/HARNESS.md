# designer-technical-writer

## Source

Derived from Harness-100 `H100/ko/81-technical-writer` as a Designer_Univers-specific staging harness. This is not a direct import.

## Purpose

Draft technical documentation, API/architecture guides, diagrams, tutorials, and version notes for Designer_Univers-related systems without modifying runtime code or publishing docs by default.

## Default Routing

```yaml
harness: designer-technical-writer
source: H100/ko/81-technical-writer
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; code execution, hosting, or repo writes require explicit software scope approval
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping |
|---|---|---|
| `info-architect` | audience analysis, information architecture, outline | designer_docs |
| `doc-writer` | technical prose, examples, tutorials, user/developer guide text | designer_docs |
| `diagram-maker` | Mermaid/diagram specifications and captions | visual-language-reviewer |
| `tech-reviewer` | technical accuracy, completeness, consistency, unverifiable claim checks | designer_reviewer |
| `version-controller` | metadata, changelog/version notes, update plan | Hermes |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “문서 구조만” | L1 | info-architect, tech-reviewer |
| “본문 작성” | L1 | info-architect, doc-writer, tech-reviewer |
| “다이어그램 포함” | L1-L2 | doc-writer, diagram-maker, tech-reviewer |
| “기존 문서 업데이트” | L1-L2 | doc-writer, tech-reviewer, version-controller |
| “공식 기술문서 후보” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_doc_structure.md
Designer Master/System/Runs/{run_id}/workspace/02_doc_draft.md
Designer Master/System/Runs/{run_id}/workspace/03_diagrams.md
Designer Master/System/Runs/{run_id}/workspace/04_technical_review.md
Designer Master/System/Runs/{run_id}/review/05_version_meta.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_technical_doc_candidate.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Frame** — Frame audience, doc type, scope, source material, and verification level.
2. **Draft** — Draft structure, prose, examples, and diagrams with [verification needed] markers where necessary.
3. **Review** — Review technical accuracy and version implications.
4. **Prepare** — Prepare metadata and update plan; do not publish or edit canonical docs without approval.
5. **Safety** — Safety review before official/canonical promotion.

## Protected Source Rules

- Never create root `_workspace`.
- Protected sources are read-only: `_Identity`, `_Philosophy`, `Personal Thinking`, `Personal Inspiration Sources`, Eagle raw library, Work Files originals, and identity/philosophy files.
- Do not upload protected/private files, raw images, credentials, or account data to external services without explicit user approval.
- Distinguish evidence, interpretation, proposal, and approved knowledge.
- Canonical absorption requires ReviewLedger entry, Hermes verification, and explicit user approval.
- Do not write or execute source code, tests, CI, or hosting deployments by default.
- Unverified examples must be labeled; do not imply tested behavior unless actually verified.
- Official documentation changes require ReviewLedger and user approval.

## Dry-Run Prompt

```text
Run designer-technical-writer in draft-write mode using only provided/public approved inputs. Write artifacts only under System/Runs paths. Do not modify canonical Designer_Univers files.
```
