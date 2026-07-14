# Deep Reinforcement Learning Assignments for Manufacturing Scheduling

This repository contains the assignment descriptions, student starter code, and instructor reference solutions for a course on deep reinforcement learning for manufacturing scheduling.

The assignments are designed as a progressive learning sequence. Students begin by formulating a scheduling problem as a Markov Decision Process, proceed to learning a scheduling policy, and finally extend the framework to a more complex scheduling problem with explicit feasibility constraints.

## 1. Repository objectives

The repository supports the following learning objectives:

- Formulate manufacturing scheduling problems as Markov Decision Processes.
- Define appropriate states, actions, rewards, transitions, and terminal conditions.
- Implement and evaluate dispatching-rule and heuristic baselines.
- Train reinforcement learning policies in a provided scheduling environment.
- Analyze the effects of state representation, reward design, exploration, and learning algorithms.
- Handle precedence constraints, machine feasibility, and invalid actions.
- Compare reinforcement learning policies with conventional scheduling methods.
- Conduct reproducible computational experiments and interpret unsuccessful results.

The primary emphasis is not simply on achieving the best numerical performance. Students are expected to understand how the scheduling problem is represented, how the environment affects learning, and why a particular policy succeeds or fails.

## 2. Assignment overview

### Assignment 1: SMSP as an MDP and baseline implementation

**Topic:** Problem formulation and baseline construction

Students formulate the Single Machine Scheduling Problem (SMSP) as a Markov Decision Process and implement conventional dispatching or heuristic policies.

Main topics include:

- State, action, reward, transition, and terminal-condition design
- Random dispatching
- Shortest Processing Time (SPT)
- Longest Processing Time (LPT)
- Earliest Due Date (EDD)
- Scheduling performance metrics
- Baseline comparison and interpretation

Typical performance metrics include:

- Makespan
- Total and mean flow time
- Total tardiness
- Number of tardy jobs
- Machine utilization

This assignment establishes the environment and evaluation structure used in the subsequent learning assignment.

### Assignment 2: Policy learning in an SMSP environment

**Topic:** Reinforcement learning policy implementation and evaluation

Students use a provided SMSP environment to implement or complete a learning algorithm and investigate whether a useful scheduling policy can be learned.

Possible learning methods include:

- Tabular Q-learning
- SARSA
- Linear function approximation
- Neural value-function approximation
- Deep Q-Network (DQN)
- Optional policy-gradient methods

Students must compare at least one design choice, such as:

- Alternative state representations
- Alternative reward functions
- Different learning algorithms
- Different exploration or learning-rate settings

The learned policy is evaluated against conventional baselines such as random dispatching, SPT, and EDD.

Students are also expected to analyze unsuccessful learning results. Poor performance is not automatically considered a failure of the assignment when the causes are investigated systematically.

### Assignment 3: Constraint-aware reinforcement learning for JSSP

**Topic:** Feasibility constraints, action masking, and reward shaping

Students extend the previous scheduling framework to a Job Shop Scheduling Problem (JSSP) or a JSSP-like environment with explicit precedence and machine constraints.

Main topics include:

- Job precedence constraints
- Machine availability
- Feasible and infeasible actions
- Invalid-action handling
- Action masking
- Infeasible-action penalties
- Reward shaping
- State and action feature design

Students perform at least one comparative experiment involving:

- Action masking versus no action masking
- Alternative reward-shaping methods
- Alternative state or action features
- Reinforcement learning versus dispatching-rule baselines

Relevant evaluation metrics may include:

- Makespan
- Total flow time
- Total tardiness
- Machine-load imbalance
- Invalid-action ratio
- Feasibility-violation count
- Episode reward

The purpose of this assignment is not to develop a new reinforcement learning algorithm. The focus is on understanding how an RL environment should represent and enforce scheduling constraints.

## 3. Recommended repository structure

```text
.
├── README.md
├── assignment_descriptions/
│   ├── assignment_01_smsp_mdp_baseline.md
│   ├── assignment_02_policy_learning_smsp.md
│   └── assignment_03_constraint_aware_jssp.md
├── starter_code/
│   ├── assignment_01_smsp_mdp_baseline/
│   │   └── smsp_baseline.py
│   ├── assignment_02_policy_learning_smsp/
│   │   └── smsp_q_learning_starter.py
│   └── assignment_03_constraint_aware_jssp/
│       └── jssp_masking_starter.py
├── instructor_solutions/
│   ├── assignment_01_smsp_mdp_baseline/
│   │   └── solution.py
│   ├── assignment_02_policy_learning_smsp/
│   │   └── solution.py
│   └── assignment_03_constraint_aware_jssp/
│       └── solution.py
├── examples/
│   └── sample_instances/
├── reports/
│   └── report_templates/
├── requirements.txt
└── .gitignore
```

The actual folder names may differ depending on the course repository structure.

## 4. Student and instructor materials

### Student starter code

The starter_code directory contains the files distributed to students.

The starter code may include:

- Basic scheduling instances
- Environment classes
- Baseline policy functions
- Metric-calculation functions
- Training-loop structure
- Evaluation utilities
- Partially implemented functions
- TODO comments
- NotImplementedError placeholders

Students are expected to complete, modify, and extend these files according to the corresponding assignment description.

### Instructor reference solutions

The instructor_solutions directory contains reference implementations for instructors and teaching assistants.

These solutions are intended for:

- Verifying assignment feasibility
- Checking expected program behavior
- Supporting grading
- Diagnosing student implementation errors
- Demonstrating one possible implementation

The reference solutions should not be interpreted as the only correct solution. Alternative implementations are acceptable when they satisfy the assignment requirements and produce valid, reproducible results.

> Important: do not distribute the instructor_solutions directory to students before the assignment deadline.

## 5. Environment setup

A Python virtual environment is recommended.

### Using venv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

A minimal dependency configuration may include:

```text
numpy
pandas
matplotlib
gymnasium
torch
```

The exact dependencies depend on the algorithms included in the starter code.

## 6. Running the assignments

Example commands are shown below.

### Assignment 1

```bash
python3 starter_code/assignment_01_smsp_mdp_baseline/smsp_baseline.py
```

### Assignment 2

```bash
python3 starter_code/assignment_02_policy_learning_smsp/smsp_q_learning_starter.py
```

### Assignment 3

```bash
python3 starter_code/assignment_03_constraint_aware_jssp/jssp_masking_starter.py
```

Each assignment folder should include its own README.md containing:

- Required Python version
- Required packages
- Execution command
- Main configuration options
- Random-seed settings
- Expected outputs
- Output-file locations

## 7. Reproducibility guidelines

Students should make their experiments reproducible.

At minimum, submitted code should specify:

- Random seed
- Number of training episodes
- Learning rate
- Discount factor
- Exploration strategy
- Environment or instance size
- Reward definition
- State representation
- Baseline definitions
- Evaluation instance set

When neural networks are used, the random seeds of relevant libraries should also be controlled.

Example:

```python
import random
import numpy as np

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
```

For PyTorch-based implementations:

```python
import torch

torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
```

## 8. Expected experimental workflow

A recommended workflow is:

1. Read the assignment description.
2. Run the provided starter code without modification.
3. Identify the incomplete functions and experiment settings.
4. Verify the environment using a small scheduling instance.
5. Implement the required baseline or learning component.
6. Test each component independently.
7. Run comparative experiments using identical instances.
8. Record the random seed and hyperparameters.
9. Save scheduling metrics and learning curves.
10. Interpret both successful and unsuccessful results.
11. Prepare the code and report for submission.

Students should avoid evaluating different methods on different problem instances unless this difference is explicitly part of the experiment.

## 9. Evaluation principles

Assignments are evaluated based on both implementation quality and analytical reasoning.

Typical evaluation criteria include:

- Correctness of the scheduling formulation
- Correct implementation of constraints
- Correctness of performance metrics
- Completeness of the required experiments
- Fairness of baseline comparisons
- Reproducibility
- Code readability
- Quality of figures and tables
- Interpretation of results
- Analysis of limitations and unsuccessful experiments

A high episode reward does not necessarily imply a high-quality scheduling policy. Scheduling metrics must be reported separately and interpreted in relation to the reward function.

## 10. Coding guidelines

Students are encouraged to follow these practices:

- Use meaningful variable and function names.
- Separate the environment, agent, training, and evaluation logic.
- Avoid hard-coding a single scheduling instance.
- Validate actions before updating the environment.
- Keep reward calculation separate from state transition when possible.
- Add comments to non-obvious scheduling logic.
- Store experiment settings in one location.
- Save results in structured formats such as CSV or JSON.
- Do not modify the evaluation metric solely to make a method appear better.
- Preserve the original starter file or use Git commits to track major changes.

## 11. Git usage

Students are encouraged to commit their work incrementally.

Example:

```bash
git add .
git commit -m "Implement SMSP baseline policies"
```

```bash
git add .
git commit -m "Add Q-learning update and evaluation"
```

```bash
git add .
git commit -m "Compare JSSP action masking strategies"
```

Do not commit:

- Virtual environments
- Python cache files
- Large temporary outputs
- Instructor solution files
- Personal access tokens
- API keys
- Passwords
- Sensitive student information

A typical .gitignore may include:

```text
.venv/
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
outputs/
checkpoints/
*.pt
*.pth
```

## 12. Academic integrity

Students may discuss general concepts, debugging approaches, and experimental design with classmates. However, submitted implementations, results, figures, and written analyses must be their own work unless collaboration is explicitly permitted.

The use of generative AI or coding assistants must follow the course policy.

When such tools are permitted, students remain responsible for:

- Understanding the submitted code
- Verifying algorithm correctness
- Identifying generated-code errors
- Reporting external assistance when required
- Explaining all major implementation decisions
- Reproducing the submitted results

Code that executes successfully but cannot be explained by the student may not receive full credit.

## 13. Notes for instructors

Before distributing an assignment:

1. Verify that the starter code runs in a clean environment.
2. Confirm that all required tasks are identifiable.
3. Test the reference solution using the published instructions.
4. Check that the assignment can be completed with reasonable computational resources.
5. Confirm that expected results are not dependent on a single random seed.
6. Ensure that student code does not contain access to the instructor solution.
7. Tag or archive the distributed version in Git.

Recommended Git tags:

```bash
git tag assignment-01-release
git tag assignment-02-release
git tag assignment-03-release
```

A separate release branch may also be maintained for student distribution.

## 14. Assignment progression

The three assignments follow this conceptual progression:

```text
Scheduling problem
        ↓
MDP formulation
        ↓
Heuristic baselines
        ↓
Policy learning
        ↓
State and reward design
        ↓
Constraint-aware action selection
        ↓
Evaluation and interpretation
```

By completing the sequence, students should be able to distinguish among:

- A scheduling problem
- A simulation or RL environment
- A conventional dispatching rule
- A learned policy
- A reward function
- An actual scheduling performance objective
- A feasible action
- An infeasible action
- Successful policy learning
- Misleading improvement in episode reward

## 15. License and use

These materials are intended for educational use in the course.

Unless otherwise stated, redistribution, publication, or commercial reuse of the assignment descriptions, starter code, and instructor solutions requires permission from the course instructor.

## 16. Contact

Questions regarding the assignments should be submitted through the communication channel designated for the course.

When reporting a code issue, include:

- Assignment number
- Python version
- Operating system
- Error message
- Execution command
- Relevant code section
- Steps required to reproduce the issue
