# Hybrid Architecture: Designer_Univers × Harness

## Principle

Designer_Univers is not replaced by Harness. Designer_Univers remains the upper governance and knowledge system. Harness becomes the execution-team design layer.

```text
Designer_Univers DNA / Constitution / Protection
    ↓ constrains
Designer_Univers Harness Layer
    ↓ dispatches
Hermes / Claude Code / Worker Profiles / Codex
    ↓ produces
Runs → Drafts → Review → Designer Earth Knowledge
```

## Layer Responsibilities

| Layer | Responsibility | Canonical Location |
|---|---|---|
| DNA / Constitution | identity, philosophy, protection, approval gates | `Designer Master/System/Rules` |
| Runtime Entry | instructions for Claude/Hermes/agents | `CLAUDE.md`, `AGENTS.md`, `_AGENT.md` |
| Harness Layer | reusable team/workflow definitions | fork first, later `Designer Master/System/Harnesses` if approved |
| Runs | bounded execution artifacts | `Designer Master/System/Runs/{run_id}` |
| Drafts | canonical-change candidates | `Designer Master/System/_drafts` |
| Knowledge | approved markdown knowledge | `Designer Earth` |
| Ledger | operation/review trace | `Designer Master/System/Logs/_ReviewLedger.md` |

## Recommended Final Structure

This is not a complete inventory of the current project. It is the target integration spine that should fit inside the existing richer structure.

```text
Designer_Univers/
├── Personal Inspiration Sources/          # raw user-selected references; read-only
├── Designer Earth/                        # Obsidian knowledge vault
│   ├── _AGENT.md
│   ├── Personal Thinking/                 # raw thinking; read-only
│   ├── Designer World/
│   │   ├── _Identity/                     # protected
│   │   ├── _Philosophy/                   # protected
│   │   ├── Knowledge/
│   │   ├── Personal Works/
│   │   ├── Personal Thinking Notes/
│   │   └── Eagle Library/
│   └── Research World/
└── Designer Master/                       # operations and governance
    ├── CLAUDE.md
    ├── AGENTS.md
    ├── .claude/agents/                    # selected runtime agents
    ├── .claude/skills/                    # selected runtime skills, SKILL.md standard
    ├── .agents/skills/                    # Codex mirror/stub policy remains separate
    ├── Work Files/                        # raw/working sources; protected by policy
    └── System/
        ├── Rules/                         # DNA source of truth
        ├── Templates/
        ├── Logs/
        ├── Scripts/
        ├── Runs/                          # harness execution artifacts
        ├── _drafts/                       # promotion/change candidates
        └── Harnesses/                     # optional later absorption target
```

## Import Rule

External Harness/H100 components can only enter the project after conversion:

```text
external agent/skill → common-agent-spec conversion → protected rule injection → workspace rewrite → cost/tool policy → Claude review → Hermes verification → user approval → project absorption
```
