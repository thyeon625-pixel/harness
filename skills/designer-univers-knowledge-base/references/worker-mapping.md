# Worker Mapping for designer-univers-knowledge-base

| Harness Expert | Existing Worker/Profile | Decision |
|---|---|---|
| harness-router | Hermes / master-orchestrator | reuse |
| safety-reviewer | designer_reviewer | reuse; required for protected or promotion scope |
| knowledge-collector | works-archivist, thinking-processor, eagle-curator, research-analyst by source | reuse source-specific collectors |
| taxonomy-designer | designer_docs or new lightweight role | extend designer_docs first |
| wiki-builder | designer_docs | reuse |
| search-optimizer | designer_docs + deterministic scripts | reuse/extend |
| maintenance-planner | designer_docs + designer_reviewer | reuse combined review |

No new worker is required for the first pilot. Create a new `knowledge-taxonomist` only if designer_docs becomes overloaded or taxonomy tasks repeat often.
