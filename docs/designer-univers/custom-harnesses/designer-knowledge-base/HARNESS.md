# designer-knowledge-base

Detailed pilot conversion from Harness-100 `64-knowledge-base-builder` into a Designer_Univers-safe custom harness.

## Purpose

Build and maintain the Designer_Univers knowledge architecture without modifying protected sources or writing directly into canonical Designer Earth. It produces inventories, taxonomy proposals, wiki/index drafts, search metadata, and maintenance plans.

## Runtime Contract

```yaml
harness: designer-knowledge-base
source: H100/ko/64-knowledge-base-builder
mode_default: draft-write
cost_default: L1
workspace: Designer Master/System/Runs/{run_id}/workspace
protected_scope: strict
canonical_write: approval-required
external_services: none by default; free-only for public web references if needed
```

## Expert Pool

| Expert | Existing Runtime Mapping | Required? | Purpose |
|---|---|---:|---|
| harness-router | master-orchestrator / Hermes | yes | choose tier/mode/experts |
| safety-reviewer | designer_reviewer | conditional | enforce protected-source and promotion gates |
| knowledge-collector | source-specific existing workers | yes | inventory current notes/rules/logs/analyses |
| taxonomy-designer | designer_docs extension or new role | yes for taxonomy | propose categories, tags, MOCs, naming |
| wiki-builder | designer_docs | conditional | draft markdown pages/indexes only |
| search-optimizer | designer_docs + scripts | conditional | aliases, link maps, search index proposals |
| maintenance-planner | designer_docs + designer_reviewer | yes for lifecycle | update cadence, ownership, audit loop |

## Converted Workflow

### Step 1 — Routing and Manifest

Hermes/router creates:

```text
Designer Master/System/Runs/{run_id}/run_manifest.yaml
```

Completion: cost tier, selected experts, protected-source involvement, and external service policy are recorded.

### Step 2 — Knowledge Inventory

`knowledge-collector` inventories current knowledge zones without modifying them:

- Designer Earth zone structure
- current analysis note types
- System/Rules and System/Templates
- ReviewLedger/SystemState/Lessons patterns
- existing `.claude/agents` and `.claude/skills`

Output:

```text
System/Runs/{run_id}/workspace/01_knowledge_inventory.md
```

### Step 3 — Taxonomy Proposal

`taxonomy-designer` proposes structure, tags, MOCs, and naming rules. It does not move files.

Output:

```text
System/Runs/{run_id}/workspace/02_taxonomy_proposal.md
```

### Step 4 — Draft Wiki/Index Artifacts

`wiki-builder` drafts markdown pages or indexes only under the run workspace or promotion candidates.

Output:

```text
System/Runs/{run_id}/workspace/03_wiki_drafts/
System/Runs/{run_id}/promotion_candidates/
```

### Step 5 — Search and Link Optimization

`search-optimizer` proposes aliases, backlinks, index names, and lightweight search metadata. It does not rewrite vault notes.

Output:

```text
System/Runs/{run_id}/workspace/04_search_index_proposal.md
```

### Step 6 — Maintenance Plan and Review

`maintenance-planner` creates lifecycle rules. `safety-reviewer` verifies protected boundaries before any promotion.

Output:

```text
System/Runs/{run_id}/outputs/05_maintenance_plan.md
System/Runs/{run_id}/review/06_safety_review.md
```

## Modes

| Request | Cost | Experts |
|---|---|---|
| “현재 지식 구조 인벤토리만” | L0-L1 | router, knowledge-collector |
| “분류 체계만 제안” | L1 | router, knowledge-collector, taxonomy-designer |
| “Obsidian 인덱스 초안 생성” | L1-L2 | router, taxonomy-designer, wiki-builder, search-optimizer, safety-reviewer |
| “공식 구조 변경” | L3 | full selected team + safety-reviewer + Claude review + Hermes verification |

## Protected Source Rules

- Never create root `_workspace`.
- Never modify `_Identity`, `_Philosophy`, Personal Thinking raw notes, Personal Inspiration originals, Eagle raw library, or Work Files originals.
- Never promote taxonomy/pattern/decision notes directly into Designer Earth.
- Always distinguish inventory, interpretation, proposal, and approved knowledge.
- Always record official absorption proposals in ReviewLedger when later applied to Designer_Univers.
