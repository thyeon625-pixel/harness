# Claude Code Review Request

Use this prompt when asking Claude Code to review the fork before absorption.

```text
You are reviewing the GitHub fork branch for Designer_Univers harness adaptation.

Repository/branch:
- https://github.com/thyeon625-pixel/harness/tree/feat/designer-univers-harness

Changed Designer_Univers output path rule:
- Do not write review output to root `_workspace`, `Agent Shared`, old iCloud paths, or the GitHub repo.
- The correct Claude Code result inbox is `Designer Master/System/Logs/Agent_Orchestration/Claude_Results/review/`.
- For this review, write the result JSON to the exact path supplied by Hermes dispatch:
  `Designer Master/System/Logs/Agent_Orchestration/Claude_Results/review/<task_id>.result.json`.
- The matching Hermes instruction record lives at:
  `Designer Master/System/Logs/Agent_Orchestration/Hermes_Instructions/review/<task_id>.md`.

Review scope:
1. Verify that the branch does not require direct absorption into Designer_Univers yet.
2. Check whether the common agent spec is runtime-portable across Hermes, Claude Code, Codex, and Kanban workers.
3. Check whether workspace Solution C is consistently applied: Runs for execution, _drafts for proposals, Designer Earth for approved knowledge, System/Rules for official governance.
4. Check whether protected-source rules are present and strong enough for _Identity, _Philosophy, Personal Thinking, Personal Inspiration originals, Eagle raw library, and Work Files originals.
5. Check whether the Expert Pool router prevents unnecessary full-team runs and includes safety-reviewer where needed.
6. Check whether H100 first-priority candidates are staged as custom harnesses rather than bulk imported.
7. Check whether designer-knowledge-base is safe as the first pilot.
8. Identify any missing files, contradictions, stale root _workspace assumptions, or risk of Claude Code becoming primary operator instead of Hermes.

Return a JSON-like report with:
- status: pass | pass_with_notes | needs_fix
- blocking_issues: []
- non_blocking_suggestions: []
- absorption_recommendation: do_not_absorb_yet | absorb_docs_only | absorb_pilot_runtime_candidate
- files_reviewed: []
```

Claude must not modify Designer_Univers canonical files during this review. If writing review output, write it as a review artifact only.
