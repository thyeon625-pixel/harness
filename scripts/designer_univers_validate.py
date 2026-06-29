#!/usr/bin/env python3
"""Validate Designer_Univers harness adaptation branch before absorption."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)
def read(path): return (ROOT / path).read_text(encoding='utf-8', errors='ignore')

required = [
    'DESIGNER_UNIVERS.md',
    'docs/designer-univers/README.md',
    'docs/designer-univers/common-agent-spec.md',
    'docs/designer-univers/target-structure-current-aware.md',
    'docs/designer-univers/workspace-policy.md',
    'docs/designer-univers/protected-source-injection.md',
    'docs/designer-univers/external-service-policy.md',
    'docs/designer-univers/cost-expert-pool-policy.md',
    'docs/designer-univers/expert-pool-router-design.md',
    'docs/designer-univers/harness-100-first-priority-candidates.md',
    'docs/designer-univers/worker-profile-integration.md',
    'docs/designer-univers/custom-harnesses/README.md',
    'docs/designer-univers/custom-harnesses/designer-knowledge-base/HARNESS.md',
    'docs/designer-univers/pre-absorption/absorption-plan.md',
    'docs/designer-univers/pre-absorption/absorption-readiness-checklist.md',
    'docs/designer-univers/pre-absorption/dry-run-scenarios.md',
    'docs/designer-univers/pre-absorption/claude-review-request.md',
    'docs/designer-univers/pre-absorption/hermes-review-protocol.md',
    'docs/designer-univers/pre-absorption/sample-run-manifest.yaml',
    'docs/designer-univers/pre-absorption/validation-report.md',
    'skills/designer-univers-harness/SKILL.md',
    'skills/designer-univers-expert-router/SKILL.md',
    'skills/designer-univers-knowledge-base/SKILL.md',
    'skills/designer-univers-audit-report/SKILL.md',
    'skills/designer-univers-brand-identity/SKILL.md',
]
for rel in required:
    if not (ROOT / rel).exists(): err(f'missing required file: {rel}')

for path in sorted((ROOT / 'skills').glob('designer-univers*/SKILL.md')):
    content = path.read_text(encoding='utf-8', errors='ignore')
    rel = path.relative_to(ROOT)
    if not content.startswith('---'):
        err(f'{rel}: frontmatter must start at byte 0'); continue
    end = content.find('\n---\n', 3)
    if end == -1:
        err(f'{rel}: closing frontmatter missing'); continue
    fm = {}
    for line in content[3:end].splitlines():
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1); fm[k.strip()] = v.strip().strip('"')
    if not fm.get('name'): err(f'{rel}: missing name')
    if not fm.get('description'): err(f'{rel}: missing description')
    elif len(fm['description']) > 1024: err(f'{rel}: description too long')
    if not content[end+5:].strip(): err(f'{rel}: empty body')

harnesses = sorted((ROOT / 'docs/designer-univers/custom-harnesses').glob('*/HARNESS.md'))
if len(harnesses) != 10: err(f'expected 10 first-priority harness scaffolds, found {len(harnesses)}')

# Every first-priority scaffold must preserve strict protection and block direct absorption.
# The detailed pilot may include full Protected Source Rules; lightweight scaffolds must at
# least carry the pre-use conversion checklist so half-converted harnesses cannot be
# silently absorbed.
for h in harnesses:
    txt = h.read_text(encoding='utf-8', errors='ignore')
    rel = h.relative_to(ROOT)
    for marker in ['protected_scope: strict', 'safety-reviewer', 'System/Runs', 'promotion_candidates']:
        if marker not in txt:
            err(f'{rel}: missing scaffold safety marker {marker}')
    if 'Protected Source Rules' not in txt and 'Inject protected-source rules' not in txt:
        err(f'{rel}: missing protected-source conversion gate')
    if 'Canonical absorption' not in txt and 'approval' not in txt.lower():
        err(f'{rel}: missing canonical absorption approval gate')

agent_dir = ROOT / 'docs/designer-univers/custom-harnesses/designer-knowledge-base/agents'
expected_agents = {'knowledge-collector', 'taxonomy-designer', 'wiki-builder', 'search-optimizer', 'maintenance-planner', 'safety-reviewer'}
found_agents = {p.stem for p in agent_dir.glob('*.md')}
if found_agents != expected_agents: err(f'knowledge-base agents mismatch: {sorted(found_agents)}')
for p in agent_dir.glob('*.md'):
    text = p.read_text(encoding='utf-8', errors='ignore')
    rel = p.relative_to(ROOT)
    for marker in ['runtime_targets:', 'role_class:', 'Protected Source Rules', 'Workspace Rules', 'Completion Criteria']:
        if marker not in text: err(f'{rel}: missing common spec marker {marker}')

detailed_expected_agents = {
    'designer-audit-report': {'audit-scope-designer', 'checklist-builder', 'findings-analyst', 'recommendation-writer', 'tracking-manager'},
    'designer-brand-identity': {'brand-strategist', 'naming-specialist', 'copywriter', 'visual-director', 'identity-lens-reviewer'},
}
for harness_name, expected in detailed_expected_agents.items():
    hdir = ROOT / 'docs/designer-univers/custom-harnesses' / harness_name
    hfile = hdir / 'HARNESS.md'
    if not hfile.exists():
        err(f'{harness_name}: missing HARNESS.md')
        continue
    htext = hfile.read_text(encoding='utf-8', errors='ignore')
    for marker in ['## Agent Team', '## Routing Matrix', '## Run Artifact Contract', '## Protected Source Rules', '## Dry-Run Prompt']:
        if marker not in htext:
            err(f'{hfile.relative_to(ROOT)}: missing detailed harness marker {marker}')
    found = {p.stem for p in (hdir / 'agents').glob('*.md')}
    if found != expected:
        err(f'{harness_name} agents mismatch: expected {sorted(expected)}, found {sorted(found)}')
    for ap in (hdir / 'agents').glob('*.md'):
        atext = ap.read_text(encoding='utf-8', errors='ignore')
        rel = ap.relative_to(ROOT)
        for marker in ['runtime_targets:', 'protected_scope: strict', 'Protected Source Rules', 'Workspace Rules', 'Completion Criteria']:
            if marker not in atext:
                err(f'{rel}: missing detailed agent marker {marker}')

positive_bad_patterns = ['create root `_workspace` as workspace', '프로젝트 루트에 생성한다', 'Create `_workspace/`']
for p in list((ROOT / 'docs/designer-univers').rglob('*.md')) + list((ROOT / 'skills').glob('designer-univers*/**/*.md')):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for pat in positive_bad_patterns:
        if pat in txt: err(f'{p.relative_to(ROOT)}: positive root workspace instruction: {pat}')
    if 'canonical_root: /Users/taehyeon/' in txt:
        err(f'{p.relative_to(ROOT)}: hard-coded personal canonical_root path')

# Cost routing must remain cheap by default; full-team or canonical routes must be opt-in.
for h in harnesses:
    txt = h.read_text(encoding='utf-8', errors='ignore')
    rel = h.relative_to(ROOT)
    if 'default_cost_tier: L1' not in txt and 'cost_default: L1' not in txt:
        err(f'{rel}: missing L1 default cost tier')
    if 'L3' in txt and 'approval' not in txt.lower():
        err(f'{rel}: L3/canonical route lacks approval gate')

custom_readme = ROOT / 'docs/designer-univers/custom-harnesses/README.md'
if custom_readme.exists() and 'Shared Agents' not in custom_readme.read_text(encoding='utf-8', errors='ignore'):
    err('custom-harnesses/README.md: missing shared safety-reviewer note')
for rel in ['docs/designer-univers/custom-harnesses/designer-audit-report/HARNESS.md', 'docs/designer-univers/custom-harnesses/designer-brand-identity/HARNESS.md']:
    if (ROOT / rel).exists() and 'Shared Safety Reviewer' not in read(rel):
        err(f'{rel}: missing shared safety-reviewer cross-reference')

safety_terms = ['_Identity', '_Philosophy', 'Personal Thinking', 'Personal Inspiration', 'Eagle', 'Work Files']
for rel in ['docs/designer-univers/protected-source-injection.md', 'docs/designer-univers/custom-harnesses/designer-knowledge-base/HARNESS.md']:
    if (ROOT / rel).exists():
        txt = read(rel)
        for term in safety_terms:
            if term not in txt: warn(f'{rel}: safety term not mentioned: {term}')

if (ROOT / 'docs/designer-univers/external-service-policy.md').exists():
    txt = read('docs/designer-univers/external-service-policy.md')
    for term in ['free-only', 'approval-required', 'protected-source upload']:
        if term not in txt: err(f'external-service-policy missing {term}')
if (ROOT / 'docs/designer-univers/expert-pool-router-design.md').exists():
    txt = read('docs/designer-univers/expert-pool-router-design.md')
    for term in ['L0', 'L1', 'L2', 'L3', 'safety-reviewer']:
        if term not in txt: err(f'expert-pool-router-design missing {term}')

print('DESIGNER_UNIVERS_VALIDATE')
print(f'required_files={len(required)}')
print(f'custom_harnesses={len(harnesses)}')
print(f'knowledge_base_agents={len(found_agents)}')
print(f'detailed_harnesses={1 + len(detailed_expected_agents)}')
print(f'warnings={len(warnings)}')
for w in warnings: print('WARNING:', w)
if errors:
    print(f'errors={len(errors)}')
    for e in errors: print('ERROR:', e)
    sys.exit(1)
print('status=PASS')
