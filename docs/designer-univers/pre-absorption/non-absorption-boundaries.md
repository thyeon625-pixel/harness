# Non-Absorption Boundaries

This file lists what must remain out of Designer_Univers until a separate explicit approval is given.

## Runtime Skills Not Approved

The fork contains staging skills under `skills/designer-univers-*`. They are not approved for direct installation into:

```text
Designer Master/.claude/skills/
Designer Master/.agents/skills/
```

## Active Agents Not Approved

The fork contains agent specs under custom harness directories. They are not approved for direct activation under:

```text
Designer Master/.claude/agents/
Designer Master/.codex/agents/
```

They can be reviewed as documentation only if copied into a draft folder.

## Governance Rules Not Approved

Do not modify these without a separate explicit governance decision:

```text
Designer Master/System/Rules/**
Designer Master/CLAUDE.md
Designer Master/AGENTS.md
Designer Earth/_AGENT.md
```

## Knowledge Writes Not Approved

Do not write generated knowledge into Designer Earth as part of absorption:

```text
Designer Earth/Designer World/**
Designer Earth/Research World/**
Designer Earth/System/**
```

## Protected Sources Remain Read-Only

Never modify, move, rename, delete, upload, or overwrite:

```text
_Identity
_Philosophy
Personal Thinking raw notes
Personal Inspiration Sources originals
Eagle raw library
Work Files originals
About Me
Storytelling_First
Background_Before_Design
```

## External/Automation Actions Not Approved

Do not perform these as part of absorption:

```text
paid market reports
surveys/interviews
scraping
private account access
BI/ERP/database connections
image generation
purchases
credential setup
launchd/cron/gateway changes
runtime code writes
CI/hosting deployment
```

## Principle

Absorption is a copying/documentation decision first. Runtime behavior changes require a separate decision.
