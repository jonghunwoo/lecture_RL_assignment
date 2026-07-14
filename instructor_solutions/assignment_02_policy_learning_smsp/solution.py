import random
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Job:
    name: str
    processing_time: int
    due_date: int


class SMSPEnvironment:
    def __init__(self, jobs: List[Job]):
        self.jobs = jobs
        self.reset()

    def reset(self) -> Tuple[int, ...]:
        self.time = 0
        self.completed = set()
        return self.get_state()

    def get_state(self) -> Tuple[int, ...]:
        # TODO: compare this binary state with at least one alternative feature design.
        return tuple(1 if i in self.completed else 0 for i in range(len(self.jobs)))

    def available_actions(self) -> List[int]:
        return [i for i in range(len(self.jobs)) if i not in self.completed]

    def step(self, action: int):
        if action not in self.available_actions():
            raise ValueError(f"Invalid action: {action}")

        job = self.jobs[action]
        previous_time = self.time
        self.time += job.processing_time
        self.completed.add(action)
        done = len(self.completed) == len(self.jobs)

        reward = self.compute_reward(job, previous_time, self.time, done)
        return self.get_state(), reward, done, {"completion_time": self.time}

    def compute_reward(self, job: Job, start_time: int, completion_time: int, done: bool) -> float:
        # TODO: compare at least two reward designs.
        # Example 1: negative completion time increment.
        return -float(completion_time - start_time)


def default_jobs() -> List[Job]:
    return [
        Job("A", 5, 10),
        Job("B", 3, 7),
        Job("C", 8, 15),
    ]


def epsilon_greedy_action(
    q_table: Dict[Tuple[int, ...], Dict[int, float]],
    state: Tuple[int, ...],
    available_actions: List[int],
    epsilon: float,
) -> int:
    if random.random() < epsilon:
        return random.choice(available_actions)

    values = q_table.setdefault(state, {a: 0.0 for a in available_actions})
    return max(available_actions, key=lambda a: values.get(a, 0.0))


def train_q_learning(
    episodes: int = 500,
    alpha: float = 0.1,
    gamma: float = 1.0,
    epsilon: float = 0.2,
) -> Dict[Tuple[int, ...], Dict[int, float]]:
    env = SMSPEnvironment(default_jobs())
    q_table: Dict[Tuple[int, ...], Dict[int, float]] = {}

    for _ in range(episodes):
        state = env.reset()
        done = False

        while not done:
            actions = env.available_actions()
            action = epsilon_greedy_action(q_table, state, actions, epsilon)
            next_state, reward, done, _ = env.step(action)
            next_actions = env.available_actions()

            state_values = q_table.setdefault(state, {a: 0.0 for a in actions})
            next_values = q_table.setdefault(next_state, {a: 0.0 for a in next_actions})
            best_next = max(next_values.values()) if next_values else 0.0

            # TODO: explain this update rule in the report.
            state_values[action] += alpha * (reward + gamma * best_next - state_values[action])
            state = next_state

    return q_table


def render_schedule(sequence: List[str], completion_time: int) -> None:
    print("timeline:")
    current_time = 0
    for job_name in sequence:
        job = next(job for job in default_jobs() if job.name == job_name)
        start_time = current_time
        completion_time_for_job = start_time + job.processing_time
        bar = "#" * job.processing_time
        print(f"  {job_name:>3} |{bar:<{completion_time}}| start={start_time}, end={completion_time_for_job}")
        current_time = completion_time_for_job
    print("final completion time:", completion_time)


def evaluate_greedy_policy(q_table: Dict[Tuple[int, ...], Dict[int, float]]) -> None:
    env = SMSPEnvironment(default_jobs())
    state = env.reset()
    done = False
    sequence = []

    while not done:
        actions = env.available_actions()
        values = q_table.get(state, {a: 0.0 for a in actions})
        action = max(actions, key=lambda a: values.get(a, 0.0))
        sequence.append(env.jobs[action].name)
        state, _, done, _ = env.step(action)

    print("learned sequence:", sequence)
    render_schedule(sequence, env.time)


if __name__ == "__main__":
    random.seed(0)
    q = train_q_learning()
    evaluate_greedy_policy(q)
