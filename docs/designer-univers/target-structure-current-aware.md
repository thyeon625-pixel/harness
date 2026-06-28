# Designer_Univers Target Structure — Current-Aware Harness Integration

This document refines the earlier simplified spine into a current-aware target structure. It does **not** delete existing Designer_Univers folders. It defines where Harness-derived artifacts fit without losing the current governance, logs, workers, backups, and Obsidian knowledge zones.

## Current High-Level Root

Observed canonical root:

```text
Designer_Univers/
├── 00_ORGANIZATION.md
├── Designer Earth/
├── Designer Master/
├── Eagle Library/
├── Hermes_Backups/
└── Personal Inspiration Sources/
```

The Harness adaptation must preserve this root identity. It must not introduce root `_workspace/`, root `.claude/`, or root agent folders.

## Target Integration Spine Inside Existing Structure

```text
Designer_Univers/
├── Personal Inspiration Sources/                  # raw reference drop zone; immutable by default
├── Eagle Library/                                 # app-managed raw library; protected by policy
├── Hermes_Backups/                                # backups; not an execution workspace
├── Designer Earth/                                # approved Markdown knowledge vault
│   ├── _AGENT.md
│   ├── System/                                    # vault-side guides/templates/MOCs
│   ├── Personal Thinking/                         # raw user thinking; immutable
│   ├── Designer World/
│   │   ├── _Identity/                             # protected identity sources
│   │   ├── _Philosophy/                           # protected philosophy sources
│   │   ├── Knowledge/
│   │   │   ├── Reference Analyses/
│   │   │   ├── Decisions/
│   │   │   ├── Indexes/
│   │   │   └── Patterns/
│   │   ├── Personal Works/
│   │   ├── Personal Thinking Notes/
│   │   └── Eagle Library/
│   └── Research World/
│       └── Trend Analysis/
└── Designer Master/                               # operations, governance, execution
    ├── CLAUDE.md                                  # slim runtime entry, not a full harness dump
    ├── AGENTS.md                                  # Hermes/Codex/agent entry
    ├── .claude/
    │   ├── agents/                                # selected Claude-compatible agent specs
    │   └── skills/                                # selected SKILL.md skills only after absorption
    ├── .agents/skills/                            # Codex mirror/stub policy; do not overwrite casually
    ├── .codex/agents/                             # Codex-specific specs if needed
    ├── Work Files/                                # protected raw/working project sources
    └── System/
        ├── Rules/                                 # official DNA/constitution; highest project rule
        ├── Templates/                             # reusable output templates
        ├── Scripts/                               # deterministic helpers and audits
        ├── Logs/
        │   ├── _ReviewLedger.md                   # single review entrypoint
        │   ├── _SystemState.md
        │   ├── _Lessons.md
        │   ├── Worker_Profiles/
        │   ├── Session_Handoffs/
        │   └── Agent_Orchestration/
        ├── Runs/                                  # NEW/standardized: all harness execution artifacts
        │   └── {run_id}/
        │       ├── run_manifest.yaml
        │       ├── input/
        │       ├── workspace/
        │       ├── outputs/
        │       ├── review/
        │       └── promotion_candidates/
        ├── _drafts/                               # canonical-change proposals and promotion candidates
        └── Harnesses/                             # optional later absorption target for validated custom harnesses
```

## Import Boundary

The GitHub fork branch is the staging area. Designer_Univers itself receives only validated artifacts.

```text
thyeon625-pixel/harness:feat/designer-univers-harness
    ↓ design, convert, test, review
Designer Master/System/Harnesses/                  # optional, after approval
Designer Master/.claude/{agents,skills}/           # selected runtime specs, after approval
Designer Master/System/Rules or Templates/         # official policy/template changes, after approval
```

## What Can Be Changed Aggressively Later

The user authorized considering bold structure changes, but in the current fork-first stage they remain proposals until explicit absorption:

- Root `_workspace/` should be prohibited and any existing equivalent should be migrated to `System/Runs` or archived.
- Duplicate imported agents should be merged into existing worker profiles instead of accumulating.
- H100 `skill.md` should be converted to `SKILL.md`; lowercase skill files should not be absorbed as-is.
- Any stale `.agents/skills` mirror policy should be decided before deletion or mass rewrite.

## Completion Criteria for This Structure

- [ ] No new root execution folder is required.
- [ ] Every temporary output has a run id and manifest.
- [ ] Designer Earth remains approved knowledge, not scratch space.
- [ ] Designer Master remains governance/execution, not a raw media vault.
- [ ] ReviewLedger remains the single review entrypoint.
- [ ] Existing worker profiles have a mapping before new agents are created.
