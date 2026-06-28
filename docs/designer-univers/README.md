# Designer_Univers Harness Adaptation

이 디렉터리는 `thyeon625-pixel/harness` fork를 **Designer_Univers용 하네스 설계/검증 브랜치**로 발전시키기 위한 적응 문서다. 목적은 원본 `harness`와 `harness-100`을 그대로 프로젝트에 복사하는 것이 아니라, Designer_Univers의 DNA를 상위 규칙으로 고정한 뒤 필요한 팀 아키텍처와 하네스만 안전하게 흡수하는 것이다.

## 확정된 운영 방향

1. **공용 에이전트 규격으로 수정한다.** Claude Code 전용 표현은 Hermes/Kanban/Codex/파일 기반 오케스트레이션에서도 해석 가능한 범용 규격으로 변환한다.
2. **GitHub fork에서 먼저 완성한다.** 이 fork에서 `Designer_Univers용 harness`를 설계·검증하고, 실제 디자이너유니버스 본체에는 완성도가 충분할 때 선별 흡수한다.
3. **하이브리드 최종 구조를 채택한다.** Designer_Univers는 헌법/보호/지식 저장소, Harness는 작업팀 설계·실행층, Harness-100은 선별 부품 카탈로그로 사용한다.
4. **Designer_Univers DNA를 상위 규칙으로 고정한다.** `_Identity`, `_Philosophy`, Personal Thinking 원문, Personal Inspiration 원본, Eagle/Work Files 원본은 read-only reference다.
5. **Workspace 정책은 해결안 C를 채택한다.** 실행 중간 산출물은 `System/Runs`, canonical 반영 전 제안은 `System/_drafts`, 최종 지식은 `Designer Earth`, 공식 규칙은 `System/Rules`로 분리한다.
6. **보호 규칙은 에이전트별로 세분화해 주입한다.** 모든 agent/skill은 공통 보호 규칙 + 역할별 금지/허용 범위를 가진다.
7. **외부 API/서비스는 free-only 기본 정책으로 검토한다.** 사용자 정책 변경 가능성을 인정하되, 비용·원본 업로드·토큰 사용은 실행 전 명시한다.
8. **비용 정책은 Expert Pool과 결합한다.** 모든 작업에 full team을 쓰지 않고, router가 필요 전문가만 호출한다.
9. **custom harness를 우선 생성한다.** Harness-100은 그대로 복사하지 않고, 일부만 선별·변환한다.

## 문서 구성

- `common-agent-spec.md` — 공용 에이전트 규격
- `hybrid-architecture.md` — Designer_Univers × Harness 하이브리드 최종 구조
- `workspace-policy.md` — 해결안 C 기반 Run/Draft/Knowledge/Rules 분리 정책
- `protected-source-injection.md` — 공통/역할별 보호 규칙 주입 템플릿
- `external-service-policy.md` — 외부 API/서비스 free-only 정책
- `cost-expert-pool-policy.md` — 비용 등급 + Expert Pool 결합 정책
- `harness-100-first-priority-candidates.md` — H100 1순위 후보 선별표
- `worker-profile-integration.md` — 기존 Hermes worker profile의 역할과 흡수 방식

## 본체 흡수 기준

이 fork의 산출물은 다음 조건을 만족할 때만 Designer_Univers 본체로 흡수한다.

- [ ] 모든 imported/derived skill은 `SKILL.md` 표준을 따른다.
- [ ] 모든 agent는 `common-agent-spec.md` 필드를 가진다.
- [ ] root `_workspace/` 사용이 제거되고 `System/Runs/{run_id}/workspace`로 치환된다.
- [ ] Protected Source Rule이 모든 agent/skill에 주입되어 있다.
- [ ] 외부 API/서비스 사용은 free-only/no-upload 기본값이다.
- [ ] 기존 Hermes worker profile과 중복/승격/폐기 후보가 분리되어 있다.
- [ ] Claude Code review와 Hermes 검증을 통과한다.
- [ ] 사용자 승인 후 Designer_Univers 본체에 반영한다.

## Added in the second integration pass

- `target-structure-current-aware.md` — current-aware final structure, preserving existing Designer_Univers folders.
- `expert-pool-router-design.md` — practical router design that combines cost policy and Expert Pool execution.
- `custom-harnesses/` — first-priority Designer_Univers custom harnesses, including the detailed `designer-knowledge-base` pilot.
- `skills/designer-univers-expert-router/SKILL.md` — runtime skill for cost-aware expert selection.
- `skills/designer-univers-knowledge-base/SKILL.md` — first converted pilot skill from H100 `64-knowledge-base-builder`.
