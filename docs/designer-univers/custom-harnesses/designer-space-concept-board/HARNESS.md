# designer-space-concept-board

## Source

Derived from Harness-100 `77-space-concept-board` as a Designer_Univers-specific spatial atmosphere, material palette, and moodboard planning harness. This is not a direct import.

## Purpose

Translate spatial/interior/reference inspiration into concept boards, palette/material directions, object/atmosphere suggestions, and review notes while keeping source images and protected libraries read-only.

## Default Routing

```yaml
harness: designer-space-concept-board
source: H100/ko/77-space-concept-board
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: free-only for public product/style lookup; purchasing/paid/private accounts require approval
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping | Default Use |
|---|---|---|---|
| `style-analyst` | style diagnosis, atmosphere vocabulary, constraints | visual-language-reviewer + eagle-curator | every board |
| `moodboard-designer` | palette/material/texture composition | visual-language-reviewer | moodboard mode |
| `item-curator` | object/furniture/reference suggestions as non-purchasing candidates | research-analyst | item mode |
| `budget-scope-planner` | cost bands and priority plan, no purchase execution | Hermes + research-analyst | budget mode |
| `concept-reviewer` | coherence, feasibility, source/proposal separation | designer_reviewer | review mode |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec | required for promotion/canonical use |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “무드/스타일 방향만” | L1 | style-analyst, moodboard-designer, concept-reviewer |
| “컬러/소재 보드” | L1 | style-analyst, moodboard-designer, concept-reviewer |
| “아이템 후보까지” | L1-L2 | style-analyst, moodboard-designer, item-curator, concept-reviewer |
| “예산/우선순위까지” | L2 | item-curator, budget-scope-planner, concept-reviewer |
| “공식 공간/브랜드 컨셉 후보” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_style_analysis.md
Designer Master/System/Runs/{run_id}/workspace/02_moodboard_direction.md
Designer Master/System/Runs/{run_id}/workspace/03_item_candidates.md
Designer Master/System/Runs/{run_id}/workspace/04_budget_priority.md
Designer Master/System/Runs/{run_id}/review/05_concept_review.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_space_concept_board_draft.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Input framing** — capture space type, mood, constraints, and whether source images are protected originals or existing analyses.
2. **Style analysis** — define atmosphere, spatial qualities, color/material keywords, and non-goals.
3. **Moodboard direction** — draft palette, texture, light, object families, and spatial composition.
4. **Item candidates** — provide candidates as inspiration/proposal only; no purchasing or account access.
5. **Budget priority** — optional rough bands and sequencing; mark uncertain prices.
6. **Concept review** — check coherence and source/proposal separation.
7. **Safety review** — required before promotion or public sharing.

## Protected Source Rules

- Never create root `_workspace`.
- Personal Inspiration originals and Eagle raw library are read-only; use thumbnails/analysis notes only if already approved.
- Do not upload raw source images to external services without explicit user approval.
- Product links/prices are suggestions, not purchases; private accounts are never accessed by default.
- Canonical absorption requires ReviewLedger entry and explicit user approval.

## Dry-Run Prompt

```text
Run designer-space-concept-board in draft-write mode for a private spatial atmosphere board using only provided non-sensitive summaries. Do not upload images or purchase anything.
```
