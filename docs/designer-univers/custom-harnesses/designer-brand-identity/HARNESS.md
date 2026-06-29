# designer-brand-identity

## Source

Derived from Harness-100 `06-brand-identity` as a Designer_Univers-specific identity-safe brand strategy harness. This is not a direct import.

## Purpose

Draft brand positioning, naming directions, verbal identity, visual direction, and consistency review while treating Hyeon's identity/philosophy sources as protected read-only lenses.

## Default Routing

```yaml
harness: designer-brand-identity
source: H100/ko/06-brand-identity
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: free-only for public benchmark lookup; paid/private services require approval
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping | Default Use |
|---|---|---|---|
| `brand-strategist` | positioning, audience, archetype, competitive frame | research-analyst + Hermes | strategy/full mode |
| `naming-specialist` | naming directions and candidate evaluation | designer_docs helper or Claude CLI | naming mode |
| `copywriter` | slogans, tone, verbal identity, story | designer_docs | verbal/full mode |
| `visual-director` | visual principles, palette direction, typography direction | eagle-curator + visual-language-reviewer | visual/full mode |
| `identity-lens-reviewer` | read-only fit against protected identity/philosophy | thinking-processor + designer_reviewer | always when protected sources are referenced |
| `safety-reviewer` | protected-source and promotion boundary check | designer_reviewer | required for promotion or canonical use |

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “브랜드 방향 간단히 잡아줘” | L1 | brand-strategist, identity-lens-reviewer |
| “네이밍 후보만” | L1 | brand-strategist, naming-specialist, identity-lens-reviewer |
| “슬로건/톤앤매너” | L1 | copywriter, identity-lens-reviewer |
| “비주얼 방향까지” | L1-L2 | brand-strategist, visual-director, identity-lens-reviewer, safety-reviewer |
| “공식 프로필/브랜드 가이드 반영” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_brand_strategy.md
Designer Master/System/Runs/{run_id}/workspace/02_naming_candidates.md
Designer Master/System/Runs/{run_id}/workspace/03_verbal_identity.md
Designer Master/System/Runs/{run_id}/workspace/04_visual_identity.md
Designer Master/System/Runs/{run_id}/review/05_identity_lens_review.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_brand_identity_draft.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Input framing** — clarify project, audience, medium, and whether protected identity/philosophy sources are involved.
2. **Strategy** — draft positioning, audience, promise, boundaries, and non-goals.
3. **Naming** — generate candidates only as draft options; mark trademark/domain checks as user verification items.
4. **Verbal identity** — draft slogans, tone, story, taboo phrases, and sentence examples.
5. **Visual identity direction** — draft principles, color/typography mood, layout references; no paid generation by default.
6. **Identity lens review** — check fit against protected sources without changing them.
7. **Safety review** — verify no protected content was copied into public/promotion artifacts without approval.

## Protected Source Rules

- Never create root `_workspace`.
- Never modify or quote protected identity/philosophy sources into public-facing brand copy without user approval.
- Treat `_Identity`, `_Philosophy`, `About Me`, `Storytelling_First`, and `Background_Before_Design` as read-only lenses.
- Personal Thinking and Personal Inspiration originals may inform drafts only as private interpretation, not official claims.
- Canonical absorption requires ReviewLedger entry and explicit user approval.

## Dry-Run Prompt

```text
Run designer-brand-identity in draft-write mode for a hypothetical portfolio identity refresh. Use no protected source text unless Hermes explicitly provides excerpts. Produce strategy, verbal, visual, identity-review, and safety-review artifacts only under System/Runs.
```
