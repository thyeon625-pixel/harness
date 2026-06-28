# Absorption Readiness Checklist

Use this checklist before moving any artifact from the GitHub fork into the canonical Designer_Univers workspace.

## Repository Readiness

- [ ] Branch is pushed to `thyeon625-pixel/harness:feat/designer-univers-harness`.
- [ ] Latest remote commit is recorded in the absorption plan.
- [ ] Validation script passes locally.
- [ ] Raw GitHub URLs for key files are reachable.
- [ ] No private tokens, secrets, or protected-source content are present in the fork.

## Structural Readiness

- [ ] Target structure preserves current root: `Designer Earth`, `Designer Master`, `Eagle Library`, `Hermes_Backups`, `Personal Inspiration Sources`.
- [ ] Root `_workspace` is prohibited.
- [ ] Execution artifacts route to `Designer Master/System/Runs/{run_id}`.
- [ ] Canonical-change proposals route to `Designer Master/System/_drafts`.
- [ ] Approved knowledge routes to `Designer Earth` only after approval.
- [ ] Official governance routes to `Designer Master/System/Rules` only after approval.

## Skill/Agent Readiness

- [ ] Every Designer_Univers skill has valid `SKILL.md` frontmatter.
- [ ] H100 lowercase `skill.md` files are not absorbed as-is.
- [ ] Every imported/derived agent follows the common agent spec.
- [ ] Every agent declares runtime targets, role class, mode, cost tier, and external-service policy.
- [ ] Existing worker profiles are mapped before new workers are proposed.

## Safety Readiness

- [ ] Protected Source Rule is present in every custom harness/agent/skill.
- [ ] `_Identity`, `_Philosophy`, Personal Thinking, Personal Inspiration originals, Eagle raw library, and Work Files originals remain read-only.
- [ ] External service policy is `none`, `free-only`, or `approval-required`.
- [ ] Any paid/private/API use requires a user call.
- [ ] `safety-reviewer` is included for protected or promotion scope.

## Cost Readiness

- [ ] Expert Pool router is defined.
- [ ] Full-team execution requires a reason.
- [ ] L0/L1/L2/L3 tier definitions are present.
- [ ] Batch strategy uses inventory → sample → cluster → selected deep review.

## Review Readiness

- [ ] Claude review request is prepared.
- [ ] Hermes review protocol is prepared.
- [ ] Dry-run scenarios are prepared.
- [ ] Absorption plan lists exact target paths and rollback options.
- [ ] User approval is required before canonical absorption.
