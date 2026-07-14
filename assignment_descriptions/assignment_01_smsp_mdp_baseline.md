# Program Assignment 1. Problem Formulation: SMSP as MDP and Baseline

## 1. 목적

이 과제의 목적은 Single Machine Scheduling Problem(SMSP)을 강화학습이 다룰 수 있는 MDP로 정확히 정식화하고, 학습 알고리즘 적용 전 기준 성능을 제공하는 dispatching/heuristic baseline을 구현하는 것이다.

이 과제는 학습 알고리즘 성능을 평가하는 과제가 아니다. 핵심은 문제를 상태, 행동, 보상, 전이, 종료조건으로 명확히 표현하고, makespan, total flow time, tardiness, utilization 등 성능지표를 계산할 수 있는 실험 구조를 만드는 것이다.

## 2. 배포 및 제출

- 배포: 2주차
- 제출: 5주차
- 비중: 10%

## 3. 문제 설정

N개의 작업이 하나의 기계에서 처리된다. 각 작업은 processing time을 가지며, 작업이 시작되면 중단 없이 완료되어야 한다. 기계는 한 번에 하나의 작업만 처리할 수 있고, setup time과 transportation time은 무시한다.

기본 예제:

| Job | Processing time | Due date |
|---|---:|---:|
| A | 5 | 10 |
| B | 3 | 7 |
| C | 8 | 15 |

학생은 위 기본 예제를 포함하고, 임의 개수의 작업에 대해서도 실행 가능한 코드를 작성한다.

## 4. 요구사항

### 4.1 MDP 정의

보고서에 다음을 명확히 정의한다.

- State: 현재까지 완료된 작업, 남은 작업, 현재 시간 등을 어떻게 표현하는가
- Action: 현재 상태에서 선택 가능한 작업은 무엇인가
- Reward: 작업 선택 후 어떤 보상 또는 비용을 부여하는가
- Transition: 작업을 하나 선택하면 상태가 어떻게 바뀌는가
- Terminal condition: 모든 작업이 완료된 상태를 어떻게 정의하는가

### 4.2 Baseline 구현

다음 중 최소 2개 이상의 baseline을 구현한다.

- Random dispatching
- SPT: shortest processing time
- LPT: longest processing time
- EDD: earliest due date
- 직접 정의한 간단한 heuristic

### 4.3 성능지표

다음 중 최소 3개를 계산한다.

- Makespan
- Total flow time
- Mean flow time
- Total tardiness
- Number of tardy jobs
- Machine utilization

### 4.4 분석

보고서에는 다음 질문에 대한 답을 포함한다.

1. 어떤 state representation을 선택했으며, 왜 그렇게 설계했는가?
2. reward를 어떻게 정의했으며, 그 reward가 어떤 scheduling objective를 유도하는가?
3. 구현한 baseline 중 어떤 방법이 가장 좋은 결과를 보였는가?
4. flow time 최소화와 tardiness 최소화는 같은 결정을 유도하는가?
5. 이 환경을 과제 2의 학습 실험으로 확장하려면 무엇을 추가해야 하는가?

## 5. 제출물

- 실행 가능한 Python 코드
- 실행 방법이 포함된 `README.md` 또는 보고서 내 실행 설명
- 2-3쪽 내외의 실험 보고서

## 6. 제공 코드

학생 배포용 기본 제공 코드 위치:

```text
06_assignments/starter_code/assignment_01_smsp_mdp_baseline/smsp_baseline.py
```

제공 코드는 최소한의 SMSP 인스턴스, baseline dispatching, 성능지표 계산 골격을 포함한다. 핵심 구현부는 `TODO` 또는 `NotImplementedError`로 남겨져 있으며, 학생은 필요한 부분을 완성하고 추가 baseline과 분석을 구현한다.

교수자용 참고 solution 위치:

```text
06_assignments/instructor_solutions/assignment_01_smsp_mdp_baseline/solution.py
```

## 7. 재사용한 기존 자료

이 과제는 기존 `assignment1_MDP_SMSP`와 `[DP] SMSP.ipynb`의 SMSP 문제 설정 및 baseline 아이디어를 2026년 평가 구조에 맞게 압축한 것이다.
