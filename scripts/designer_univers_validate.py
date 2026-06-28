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
    'skills/designer-univers-harness/SKILL.md',
    'skills/designer-univers-expert-router/SKILL.md',
    'skills/designer-univers-knowledge-base/SKILL.md',
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

agent_dir = ROOT / 'docs/designer-univers/custom-harnesses/designer-knowledge-base/agents'
expected_agents = {'knowledge-collector', 'taxonomy-designer', 'wiki-builder', 'search-optimizer', 'maintenance-planner', 'safety-reviewer'}
found_agents = {p.stem for p in agent_dir.glob('*.md')}
if found_agents != expected_agents: err(f'knowledge-base agents mismatch: {sorted(found_agents)}')
for p in agent_dir.glob('*.md'):
    text = p.read_text(encoding='utf-8', errors='ignore')
    rel = p.relative_to(ROOT)
    for marker in ['runtime_targets:', 'role_class:', 'Protected Source Rules', 'Workspace Rules', 'Completion Criteria']:
        if marker not in text: err(f'{rel}: missing common spec marker {marker}')

positive_bad_patterns = ['create root `_workspace` as workspace', '프로젝트 루트에 생성한다', 'Create `_workspace/`']
for p in list((ROOT / 'docs/designer-univers').rglob('*.md')) + list((ROOT / 'skills').glob('designer-univers*/**/*.md')):
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for pat in positive_bad_patterns:
        if pat in txt: err(f'{p.relative_to(ROOT)}: positive root workspace instruction: {pat}')

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
print(f'warnings={len(warnings)}')
for w in warnings: print('WARNING:', w)
if errors:
    print(f'errors={len(errors)}')
    for e in errors: print('ERROR:', e)
    sys.exit(1)
print('status=PASS')
