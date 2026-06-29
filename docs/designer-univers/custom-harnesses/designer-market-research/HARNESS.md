# designer-market-research

## Source

Derived from Harness-100 `H100/ko/44-market-research` as a Designer_Univers-specific staging harness. This is not a direct import.

## Purpose

Designer_Univers-aware market, competitor, consumer, and trend research using public/free sources or provided material while keeping private sources and paid research accounts gated.

## Default Routing

```yaml
harness: designer-market-research
source: H100/ko/44-market-research
mode_default: draft-write
default_cost_tier: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
review: Designer Master/System/Runs/{run_id}/review
promotion_candidates: Designer Master/System/Runs/{run_id}/promotion_candidates
external_services: free-only public web lookup; paid reports, surveys, interviews, scraping, or private accounts require explicit approval
protected_scope: strict
canonical_write: approval-required
```

## Agent Team

| Expert | Role | Existing Worker Mapping |
|---|---|---|
| `industry-analyst` | market size, industry structure, value chain, regulation mapping | research-analyst |
| `competitor-analyst` | competitor map, positioning, SWOT, offer comparison | research-analyst |
| `consumer-analyst` | audience segments, journey, needs, signals from approved/public sources | research-analyst |
| `trend-analyst` | PESTLE, technology/culture/consumer trend synthesis | research-analyst |
| `research-reviewer` | source quality, uncertainty, insight integration, contradiction checks | designer_reviewer |
| `safety-reviewer` | protected-source and promotion boundary check | shared spec |

## Shared Safety Reviewer

This harness references the shared `safety-reviewer` spec at `designer-knowledge-base/agents/safety-reviewer.md` rather than duplicating the file locally. If this pilot is ever absorbed, include that shared safety reviewer spec or an approved equivalent.

## Routing Matrix

| Request | Cost Tier | Experts |
|---|---:|---|
| “시장/산업 방향만” | L1 | industry-analyst, research-reviewer |
| “경쟁사 분석” | L1 | industry-analyst, competitor-analyst, research-reviewer |
| “소비자/타깃 분석” | L1-L2 | consumer-analyst, trend-analyst, research-reviewer |
| “트렌드/시장 종합 리서치” | L2 | selected team + source log |
| “전략 후보/공개 보고서” | L3 | selected team + safety-reviewer + Claude CLI review + Hermes/user approval |

## Run Artifact Contract

```text
Designer Master/System/Runs/{run_id}/workspace/00_input.md
Designer Master/System/Runs/{run_id}/workspace/01_industry_analysis.md
Designer Master/System/Runs/{run_id}/workspace/02_competitor_analysis.md
Designer Master/System/Runs/{run_id}/workspace/03_consumer_analysis.md
Designer Master/System/Runs/{run_id}/workspace/04_trend_analysis.md
Designer Master/System/Runs/{run_id}/review/05_research_review.md
Designer Master/System/Runs/{run_id}/review/06_safety_review.md
Designer Master/System/Runs/{run_id}/outputs/07_market_research_draft.md
Designer Master/System/Runs/{run_id}/promotion_candidates/*
```

## Workflow

1. **Frame** — Frame market scope, geography, time horizon, decision need, and allowed source types.
2. **Collect/source** — Collect/source public or provided evidence with date and uncertainty labels.
3. **Draft** — Draft industry, competitor, consumer, and trend sections with clear evidence/proposal separation.
4. **Review** — Review source quality, contradictions, and overclaim risk.
5. **Run** — Run safety review before any public or canonical candidate.

## Protected Source Rules

- Never create root `_workspace`.
- Protected sources are read-only: `_Identity`, `_Philosophy`, `Personal Thinking`, `Personal Inspiration Sources`, Eagle raw library, Work Files originals, and identity/philosophy files.
- Do not upload protected/private files, raw images, credentials, or account data to external services without explicit user approval.
- Distinguish evidence, interpretation, proposal, and approved knowledge.
- Canonical absorption requires ReviewLedger entry, Hermes verification, and explicit user approval.
- Do not buy market reports, run surveys/interviews, scrape sites, or access private accounts without explicit approval.
- Research World is for recent trends/current information from user-interest URLs; Eagle non-URL assets remain image/design analysis, not market research by default.
- Private identity/philosophy material may shape internal fit criteria only; do not expose it publicly.

## Dry-Run Prompt

```text
Run designer-market-research in draft-write mode using only provided/public approved inputs. Write artifacts only under System/Runs paths. Do not modify canonical Designer_Univers files.
```
