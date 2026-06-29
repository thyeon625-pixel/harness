# designer-design-system

## Source

Derived from Harness-100 `36-design-system` as a Designer_Univers-specific visual language and token/design-principle harness. This is not a direct import.

## Purpose

Draft visual tokens, principles, component/pattern directions, accessibility checks, and documentation structure for Designer_Univers design language. This is a design-system planning harness by default, not an automatic code-generation/runtime activation harness.

## Default Routing

```yaml
harness: designer-design-system
source: H100/ko/36-design-system
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: none by default; package/code execution requires explicit project scope
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping | Default Use |
|---|---|---|---|
| `token-designer` | color/type/spacing/motion token proposals | visual-language-reviewer + designer_docs | token mode |
| `pattern-designer` | component/pattern principles, usage rules | designer_docs | pattern mode |
| `a11y-reviewer` | contrast/accessibility heuristics | designer_reviewer / Claude CLI | review mode |
| `documentation-writer` | design-system docs and examples | designer_docs | docs mode |
| `implementation-planner` | optional code/storybook plan, not execution by default | Claude CLI helper | only when software scope exists |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec | required for promotion/canonical use |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “디자인 토큰 방향만” | L1 | token-designer, a11y-reviewer |
| “패턴/컴포넌트 원칙” | L1 | token-designer, pattern-designer, documentation-writer |
| “접근성 리뷰” | L1 | a11y-reviewer |
| “문서화까지” | L1-L2 | token-designer, pattern-designer, documentation-writer, a11y-reviewer |
| “실제 코드/스토리북 후보” | L3 | selected team + implementation-planner + safety-reviewer + explicit software scope approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_token_direction.md
Designer Master/System/Runs/{run_id}/workspace/02_pattern_principles.md
Designer Master/System/Runs/{run_id}/workspace/03_accessibility_review.md
Designer Master/System/Runs/{run_id}/workspace/04_documentation_outline.md
Designer Master/System/Runs/{run_id}/review/05_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/06_design_system_draft.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Input framing** — determine whether the work is visual-language planning, UI system planning, or implementation planning.
2. **Token direction** — propose color/type/spacing/motion tokens as drafts.
3. **Pattern principles** — map tokens to components, layouts, and visual usage rules.
4. **Accessibility review** — check contrast, legibility, motion, and keyboard/screen-reader implications where applicable.
5. **Documentation outline** — write adoption notes, examples, and do/don't guidance.
6. **Safety review** — required before any pattern is promoted to official Designer_Univers rules.

## Protected Source Rules

- Never create root `_workspace`.
- Do not convert private identity/philosophy language into public design principles without approval.
- Do not write code into project runtime or canonical repos unless a separate software scope is approved.
- Treat tokens/patterns as proposal candidates until Hermes/user promotion.
- Canonical absorption requires ReviewLedger entry and explicit user approval.

## Dry-Run Prompt

```text
Run designer-design-system in draft-write mode to propose private visual-language tokens from existing approved reference analyses. Do not edit runtime code or canonical System/Rules.
```
