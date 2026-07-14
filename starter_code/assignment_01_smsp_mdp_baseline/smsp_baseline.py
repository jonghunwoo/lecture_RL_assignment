from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple


@dataclass(frozen=True)
class Job:
    name: str
    processing_time: int
    due_date: int


def default_jobs() -> List[Job]:
    return [
        Job("A", 5, 10),
        Job("B", 3, 7),
        Job("C", 8, 15),
    ]


def dispatch_random(available_jobs: List[Job]) -> Job:
    return available_jobs[0]


def dispatch_spt(available_jobs: List[Job]) -> Job:
    return min(available_jobs, key=lambda job: job.processing_time)


def dispatch_lpt(available_jobs: List[Job]) -> Job:
    return max(available_jobs, key=lambda job: job.processing_time)


def dispatch_edd(available_jobs: List[Job]) -> Job:
    return min(available_jobs, key=lambda job: job.due_date)


def build_schedule(
    jobs: List[Job],
    dispatch_rule: Callable[[List[Job]], Job],
) -> List[Tuple[str, int, int, int]]:
    """Return rows of (job_name, start_time, completion_time, due_date)."""
    remaining = list(jobs)
    current_time = 0
    schedule = []

    while remaining:
        selected = dispatch_rule(remaining)
        start_time = current_time
        completion_time = start_time + selected.processing_time
        schedule.append((selected.name, start_time, completion_time, selected.due_date))
        current_time = completion_time
        remaining.remove(selected)

    return schedule


def calculate_metrics(schedule: List[Tuple[str, int, int, int]]) -> Dict[str, float]:
    completion_times = [row[2] for row in schedule]
    due_dates = [row[3] for row in schedule]
    tardiness = [max(0, c - d) for c, d in zip(completion_times, due_dates)]
    makespan = max(completion_times) if completion_times else 0

    return {
        "makespan": makespan,
        "total_flow_time": sum(completion_times),
        "mean_flow_time": sum(completion_times) / len(completion_times),
        "total_tardiness": sum(tardiness),
        "num_tardy_jobs": sum(t > 0 for t in tardiness),
        "machine_utilization": 1.0 if makespan > 0 else 0.0,
    }


def render_gantt_chart(schedule: List[Tuple[str, int, int, int]]) -> None:
    """Render a simple ASCII Gantt chart for the schedule."""
    if not schedule:
        print("timeline: <empty>")
        return

    makespan = max(row[2] for row in schedule)
    print("timeline:")
    for name, start_time, completion_time, due_date in schedule:
        duration = completion_time - start_time
        bar = "#" * duration
        print(f"  {name:>3} |{bar:<{makespan}}| start={start_time}, end={completion_time}, due={due_date}")


def describe_mdp() -> Dict[str, str]:
    """Fill this out and use it in your report."""
    return {
        "state": "TODO: define your state representation.",
        "action": "TODO: define selectable jobs at each state.",
        "reward": "TODO: define reward/cost after selecting a job.",
        "transition": "TODO: define how selected jobs update the state.",
        "terminal_condition": "TODO: define when an episode ends.",
    }


def run_baselines() -> None:
    jobs = default_jobs()
    rules = {
        "SPT": dispatch_spt,
        "LPT": dispatch_lpt,
        "EDD": dispatch_edd,
        "RandomPlaceholder": dispatch_random,
    }

    for name, rule in rules.items():
        schedule = build_schedule(jobs, rule)
        metrics = calculate_metrics(schedule)
        print(f"\n{name}")
        print("schedule:", schedule)
        render_gantt_chart(schedule)
        print("metrics:", metrics)


if __name__ == "__main__":
    print("MDP description template:")
    print(describe_mdp())
    run_baselines()
