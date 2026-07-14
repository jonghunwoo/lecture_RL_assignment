# Program Assignment 3. Constraint-Aware RL: JSSP or JSSP-like Scheduling

## 1. 목적

이 과제의 목적은 JSSP 또는 JSSP와 유사한 precedence-constrained scheduling 문제에서 제약조건을 반영한 RL 환경을 이해하고, action masking, reward shaping, feature design 중 하나 이상을 실험하는 것이다.

과제 1과 2가 SMSP를 중심으로 문제정의와 policy learning을 다룬다면, 과제 3은 더 복잡한 제약조건이 있는 스케줄링 문제로 확장한다. 핵심은 알고리즘을 새로 만드는 것이 아니라, precedence constraint, machine feasibility, invalid action이 있는 문제에서 RL agent가 선택 가능한 행동과 보상을 어떻게 다루어야 하는지 분석하는 것이다.

## 2. 배포 및 제출

- 배포: 11주차
- 제출: 14주차
- 비중: 10%

## 3. 문제 설정

JSSP는 여러 job과 여러 machine으로 구성된다. 각 job은 정해진 순서의 operation을 가지며, 각 operation은 지정된 machine에서 정해진 processing time만큼 처리되어야 한다.

기본 MDP 구조:

- State: job별 진행 상태, machine별 사용 가능 시간, 현재 가능한 operation 정보
- Action: 현재 선택 가능한 job 또는 operation 선택
- Action mask: precedence constraint와 machine feasibility에 따라 가능한 action만 허용
- Reward: makespan 증가량, job completion time 증가량, tardiness, workload imbalance 등을 반영
- Done: 모든 operation이 완료되면 episode 종료

## 4. 요구사항

### 4.1 제약조건 처리

다음 중 하나 이상을 명시적으로 구현하거나 수정한다.

- precedence constraint
- machine availability
- invalid action masking
- infeasible action penalty

### 4.2 개선 실험

다음 중 하나 이상을 선택해 실험한다.

- action masking 유무 비교
- reward shaping 방식 비교
- state/action feature 설계 비교
- dispatching/heuristic baseline과 RL policy 비교

### 4.3 성능지표

다음 중 최소 3개를 보고한다.

- Makespan
- Total flow time
- Total tardiness
- Workload leveling 또는 machine load imbalance
- Invalid action ratio
- Feasibility violation count
- Reward curve

### 4.4 결과 분석

보고서에는 다음 질문에 답한다.

1. 어떤 제약조건을 환경에 반영했는가?
2. action masking 또는 penalty 방식은 policy 학습에 어떤 영향을 주었는가?
3. reward shaping이 makespan 또는 workload leveling에 어떤 영향을 주었는가?
4. dispatching/heuristic baseline과 비교했을 때 RL policy의 장점과 한계는 무엇인가?
5. 결과가 개선되지 않았다면 원인은 무엇인가?

## 5. 제출물

- 실행 가능한 Python 코드
- 재현 가능한 실행 방법
- 3-4쪽 내외의 실험 보고서

## 6. 제공 코드

학생 배포용 기본 제공 코드 위치:

```text
06_assignments/starter_code/assignment_03_constraint_aware_jssp/jssp_masking_starter.py
```

제공 코드는 작은 JSSP-like toy environment와 action mask, reward 계산의 골격을 포함한다. 핵심 구현부는 `TODO` 또는 `NotImplementedError`로 남겨져 있으며, 학생은 reward shaping, action mask 비교, baseline evaluation, metric calculation을 완성한다.

교수자용 참고 solution 위치:

```text
06_assignments/instructor_solutions/assignment_03_constraint_aware_jssp/solution.py
```

## 7. 재사용한 기존 자료

이 과제는 기존 기말고사의 JSSP 노트북 구조를 참고한다. 기존 노트북에는 `JSSP_scheduler`, action feature, job availability mask, A2C agent 구조가 포함되어 있다. 2026년 과제에서는 이를 그대로 복잡하게 재현하기보다, 학생이 제약조건 처리와 실험 해석에 집중할 수 있도록 작은 JSSP-like 환경으로 단순화한다.
