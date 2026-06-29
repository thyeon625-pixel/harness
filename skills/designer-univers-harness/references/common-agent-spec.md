# Common Agent Specification for Designer_Univers Harness

이 규격은 Claude Code 전용 `.claude/agents/*.md`를 Hermes, Claude Code, Codex, Kanban worker, 파일 기반 오케스트레이션에서 모두 해석할 수 있는 공용 에이전트 정의로 바꾸기 위한 기준이다.

## Required Fields

```yaml
---
name: agent-name
runtime_targets: [hermes, claude-code, codex, kanban-worker]
role_class: collector | analyst | creator | reviewer | orchestrator | router | maintainer
owner_system: Designer_Univers
canonical_root: ${DESIGNER_UNIVERS_ROOT}
allowed_modes: [read-only, draft-write, approved-write]
default_mode: read-only
cost_tier: L0 | L1 | L2 | L3
external_services: none | free-only | approval-required
protected_scope: strict
handoff_protocol: file-ledger
---
```

## Required Body Sections

Every agent file must contain these sections:

1. `## Mission` — what the agent exists to do.
2. `## Inputs` — allowed input types and paths.
3. `## Outputs` — exact output paths and whether they are draft, run artifact, or canonical knowledge.
4. `## Protected Source Rules` — role-specific read-only and no-upload rules.
5. `## Workspace Rules` — no root `_workspace`; use `System/Runs/{run_id}/workspace`.
6. `## Collaboration Protocol` — how it communicates with Hermes, Claude Code, and other agents.
7. `## Cost and Tool Policy` — cost tier and external-service policy.
8. `## Completion Criteria` — checkable conditions for done.
9. `## Failure Handling` — retry/fallback/report rules.

## Runtime Mapping

| Generic Concept | Claude Code | Hermes | Kanban / Worker | File-based Orchestration |
|---|---|---|---|---|
| Dispatch task | Agent / TaskCreate | delegate_task / todo | kanban task | instruction markdown |
| Team message | SendMessage | summary + follow-up prompt | task comments | result JSON |
| Work state | TaskCreate/TaskUpdate | todo | kanban status | `orchestrator_state.json` |
| Artifact | `_workspace` in upstream | `System/Runs` | task result path | result JSON + markdown |
| Review | reviewer agent | Hermes verification | designer_reviewer | `_ReviewLedger.md` entry |

## Write Modes

- `read-only`: may inspect and report only.
- `draft-write`: may write only under `Designer Master/System/Runs/{run_id}` or `Designer Master/System/_drafts`.
- `approved-write`: may modify canonical project files only after explicit user approval and Hermes verification.

## Naming

- Use lowercase hyphen names for portable agent identifiers.
- Avoid generic names already used by Designer_Univers unless intentionally extending them.
- Prefix Designer_Univers-specific agents with domain meaning, not tool names. Example: `visual-language-reviewer`, not `claude-visual-reviewer`.

## Completion Criteria Template

```markdown
## Completion Criteria
- [ ] All inspected paths are listed.
- [ ] All output files are under the allowed workspace.
- [ ] No protected source was modified, moved, renamed, uploaded, or summarized beyond the requested scope.
- [ ] External service use is recorded as `none`, `free-only`, or `approval-required`.
- [ ] Next action is one of: `complete`, `needs_user_decision`, `needs_hermes_review`, `blocked`.
```

## Root Placeholder

`${DESIGNER_UNIVERS_ROOT}` means the canonical Designer_Univers root selected by Hermes at runtime. In Hyeon's local environment this currently resolves to the Dropbox-backed Designer_Univers folder, but public fork artifacts should keep the placeholder instead of hard-coding a personal absolute path.
