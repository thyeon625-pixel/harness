# designer-visual-storytelling

## Source

Derived from Harness-100 `15-visual-storytelling` as a Designer_Univers-specific visual narrative and portfolio story harness. This is not a direct import.

## Purpose

Turn reference analyses, project materials, and visual language observations into private draft visual essays, portfolio narratives, page structures, and image/text story plans without modifying raw sources or publishing protected identity material.

## Default Routing

```yaml
harness: designer-visual-storytelling
source: H100/ko/15-visual-storytelling
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; image generation and public web lookup require router escalation
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping | Default Use |
|---|---|---|---|
| `story-architect` | narrative arc, scene structure, message hierarchy | designer_docs + Hermes | planning/full mode |
| `essay-writer` | essay text, captions, portfolio copy | designer_docs | writing mode |
| `image-prompt-planner` | image prompt/spec planning only; no paid generation by default | visual-language-reviewer / Claude CLI | prompt mode |
| `layout-planner` | page/sequence/layout structure; no app build by default | designer_docs | layout mode |
| `editorial-reviewer` | coherence, tone, evidence/source separation | designer_reviewer | review mode |
| `safety-reviewer` | protected-source and public/canonical boundary check | shared spec | required for promotion/public use |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “스토리 구조만 잡아줘” | L1 | story-architect, editorial-reviewer |
| “에세이/캡션 초안” | L1 | story-architect, essay-writer, editorial-reviewer |
| “이미지 프롬프트 방향까지” | L1-L2 | story-architect, image-prompt-planner, editorial-reviewer, safety-reviewer if protected sources |
| “포트폴리오 페이지 구조” | L1-L2 | story-architect, essay-writer, layout-planner, editorial-reviewer |
| “공개용 비주얼 스토리 후보” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_story_blueprint.md
Designer Master/System/Runs/{run_id}/workspace/02_essay_text.md
Designer Master/System/Runs/{run_id}/workspace/03_image_prompt_plan.md
Designer Master/System/Runs/{run_id}/workspace/04_layout_plan.md
Designer Master/System/Runs/{run_id}/review/05_editorial_review.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_visual_story_draft.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Input framing** — identify source type: reference analysis, project case, personal thinking summary, or portfolio draft.
2. **Story blueprint** — define thesis, sequence, emotional rhythm, visual motifs, and source boundaries.
3. **Text draft** — write captions/essay/portfolio story using only approved or provided material.
4. **Image prompt plan** — create prompt directions; do not generate images unless separately approved.
5. **Layout plan** — plan page hierarchy, scene order, and image/text relationship without building a production app.
6. **Editorial review** — check coherence and distinguish evidence from interpretation.
7. **Safety review** — required before public-facing or promotion candidates.

## Protected Source Rules

- Never create root `_workspace`.
- Never modify, quote, upload, or publish protected sources without approval.
- Personal Inspiration originals and Eagle raw library are read-only; use existing analyses or explicitly provided excerpts.
- Personal Thinking and identity/philosophy sources may inform private drafts only as interpretation unless user approves exact wording.
- Canonical absorption requires ReviewLedger entry and explicit user approval.

## Dry-Run Prompt

```text
Run designer-visual-storytelling in draft-write mode for a hypothetical private portfolio story. Use only provided summaries, do not generate images, and write artifacts only under System/Runs paths.
```
