# Designer_Univers Custom Harnesses

This directory contains Designer_Univers-specific harness designs derived from Harness/Harness-100. These are staging artifacts in the GitHub fork. They are not yet absorbed into the canonical Designer_Univers workspace.

## Adoption Rules

- Use common agent spec.
- Use cost-aware Expert Pool routing.
- Use `System/Runs` for execution artifacts and `System/_drafts` for promotion candidates.
- Inject protected-source rules by role.
- Map to existing worker profiles before creating new workers.
- Absorb into Designer_Univers only after review and user approval.

## First-Priority Harnesses Created

| Harness | Status | Source Inspiration |
|---|---|---|
| designer-knowledge-base | detailed pilot conversion | H100 64 knowledge-base-builder |
| designer-audit-report | detailed pilot conversion | H100 94 audit-report |
| designer-brand-identity | detailed pilot conversion | H100 06 brand-identity |
| designer-visual-storytelling | detailed pilot conversion | H100 15 visual-storytelling |
| designer-design-system | detailed pilot conversion | H100 36 design-system |
| designer-space-concept-board | detailed pilot conversion | H100 77 space-concept-board |
| designer-market-research | detailed pilot conversion | H100 44 market-research |
| designer-report-generator | detailed pilot conversion | H100 82 report-generator |
| designer-technical-writer | detailed pilot conversion | H100 81 technical-writer |
| designer-operations-manual | detailed pilot conversion | H100 92 operations-manual |

## Shared Agents

`designer-knowledge-base/agents/safety-reviewer.md` is the shared safety reviewer specification for all detailed pilots unless a harness explicitly defines a narrower safety reviewer. Detailed harnesses may reference `safety-reviewer` without duplicating the file in every harness directory; absorption planning must include this shared spec whenever any detailed pilot is moved forward.


## Root Placeholder

Use `${DESIGNER_UNIVERS_ROOT}` in fork-staged agent specs and manifests. Hermes resolves it to the actual canonical Designer_Univers root only during an approved local run or absorption step.
