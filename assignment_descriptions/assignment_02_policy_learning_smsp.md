# Program Assignment 2. Policy Learning: Learning in a Provided SMSP Environment

## 1. 목적

이 과제의 목적은 제공된 SMSP 기반 RL 환경에서 학습 policy를 구현하거나 수정하고, state feature, reward design, 학습 알고리즘 선택이 결과에 어떤 영향을 주는지 실험적으로 분석하는 것이다.

과제 1이 문제정의와 baseline 구축에 초점을 둔다면, 과제 2는 동일한 계열의 SMSP 환경에서 policy가 실제로 학습되는지 확인하는 데 초점을 둔다. 학생은 환경을 처음부터 새로 만드는 데 시간을 쓰기보다, 제공된 환경과 기본 학습 코드를 바탕으로 Q-learning, function approximation, DQN 중 하나를 적용하고 결과를 해석한다.

## 2. 배포 및 제출

- 배포: 6주차
- 제출: 10주차
- 비중: 10%

## 3. 문제 설정

제공된 SMSP 환경은 다음 구조를 갖는다.

- State: 완료된 작업 또는 남은 작업과 현재 시간의 feature vector
- Action: 아직 처리되지 않은 작업 중 하나 선택
- Reward: flow time, makespan 증가량, tardiness, 또는 shaped reward
- Transition: 선택한 작업을 현재 시간에 배정하고 완료 상태를 갱신
- Done: 모든 작업이 완료되면 episode 종료

기본 환경은 작은 작업 수에서 빠르게 학습되도록 구성한다. 학생은 환경의 구조를 이해하고, 지정된 위치의 state feature 또는 reward 함수를 바꾸어 실험한다.

## 4. 요구사항

### 4.1 학습 알고리즘

다음 중 하나 이상을 구현하거나 제공 코드에서 완성한다.

- Tabular Q-learning
- Linear or neural value/function approximation
- DQN

선택적으로 SARSA 또는 policy gradient 계열 알고리즘을 추가해도 된다.

### 4.2 실험 비교

다음 중 하나를 반드시 수행한다.

- state feature 설계 2개 이상 비교
- reward 설계 2개 이상 비교
- Q-learning과 DQN 등 알고리즘 2개 이상 비교

### 4.3 Baseline 비교

과제 1에서 구현한 baseline 또는 제공 baseline과 학습 policy를 비교한다.

최소 비교 대상:

- Random dispatching
- SPT 또는 EDD
- 학습된 policy

### 4.4 결과 분석

보고서에는 다음 항목을 포함한다.

1. 선택한 학습 알고리즘과 이유
2. 비교한 state feature 또는 reward 설계
3. reward curve
4. makespan, total flow time, tardiness 등 scheduling metric
5. baseline 대비 학습 policy의 장단점
6. 학습이 잘 되지 않은 경우 가능한 원인

실패 분석은 감점 대상이 아니라 중요한 평가 요소이다. 다음 관점에서 원인을 설명한다.

- state representation
- reward scale
- exploration
- learning rate
- episode length
- instance size
- invalid or unavailable action 처리

## 5. 제출물

- 실행 가능한 Python 코드
- 실험 설정 파일 또는 실행 명령
- 3쪽 내외의 실험 보고서

## 6. 제공 코드

학생 배포용 기본 제공 코드 위치:

```text
06_assignments/starter_code/assignment_02_policy_learning_smsp/smsp_q_learning_starter.py
```

제공 코드는 SMSP 환경, baseline policy, tabular Q-learning 학습 루프의 골격을 포함한다. 핵심 구현부는 `TODO` 또는 `NotImplementedError`로 남겨져 있으며, 학생은 state feature, reward, action selection, update rule, evaluation 부분을 완성하거나 확장한다.

교수자용 참고 solution 위치:

```text
06_assignments/instructor_solutions/assignment_02_policy_learning_smsp/solution.py
```

## 7. 재사용한 기존 자료

이 과제는 기존 `[TD] SMSP.ipynb`, `[VFA] SMSP.ipynb`, `[PG] SMSP.ipynb`의 SMSP 환경과 학습 알고리즘 구조를 2026년 과제 2 목적에 맞게 통합한 것이다. 기존 과제처럼 알고리즘별로 여러 과제를 나누지 않고, 하나의 제공 환경에서 설계 선택과 학습 결과 해석을 비교하도록 재구성한다.
