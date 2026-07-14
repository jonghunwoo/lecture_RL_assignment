from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Operation:
    job_id: int
    op_id: int
    machine_id: int
    processing_time: int


def toy_instance() -> Dict[int, List[Operation]]:
    return {
        0: [Operation(0, 0, 0, 3), Operation(0, 1, 1, 2)],
        1: [Operation(1, 0, 1, 2), Operation(1, 1, 0, 4)],
        2: [Operation(2, 0, 0, 2), Operation(2, 1, 1, 3)],
    }


class JSSPLikeEnvironment:
    def __init__(self, jobs: Dict[int, List[Operation]]):
        self.jobs = jobs
        self.num_jobs = len(jobs)
        self.num_machines = len({op.machine_id for ops in jobs.values() for op in ops})
        self.reset()

    def reset(self):
        self.next_op = {job_id: 0 for job_id in self.jobs}
        self.job_ready_time = {job_id: 0 for job_id in self.jobs}
        self.machine_ready_time = {m: 0 for m in range(self.num_machines)}
        self.invalid_action_count = 0
        return self.get_state(), self.action_mask()

    def get_state(self) -> Tuple[int, ...]:
        job_progress = [self.next_op[j] for j in range(self.num_jobs)]
        machine_times = [self.machine_ready_time[m] for m in range(self.num_machines)]
        return tuple(job_progress + machine_times)

    def action_mask(self) -> List[bool]:
        return [self.next_op[j] < len(self.jobs[j]) for j in range(self.num_jobs)]

    def step(self, action: int, use_mask: bool = True):
        mask = self.action_mask()
        if action < 0 or action >= self.num_jobs or not mask[action]:
            self.invalid_action_count += 1
            if use_mask:
                raise ValueError(f"Invalid action under action mask: {action}")
            return self.get_state(), -10.0, self.is_done(), {"invalid": True}

        op = self.jobs[action][self.next_op[action]]
        start = max(self.job_ready_time[action], self.machine_ready_time[op.machine_id])
        finish = start + op.processing_time

        previous_makespan = self.makespan()
        self.job_ready_time[action] = finish
        self.machine_ready_time[op.machine_id] = finish
        self.next_op[action] += 1
        new_makespan = self.makespan()

        reward = self.compute_reward(previous_makespan, new_makespan)
        return self.get_state(), reward, self.is_done(), {"invalid": False, "finish": finish}

    def compute_reward(self, previous_makespan: int, new_makespan: int) -> float:
        return -float(new_makespan - previous_makespan)

    def makespan(self) -> int:
        return max(self.job_ready_time.values())

    def workload_imbalance(self) -> int:
        loads = list(self.machine_ready_time.values())
        return max(loads) - min(loads)

    def is_done(self) -> bool:
        return all(self.next_op[j] == len(self.jobs[j]) for j in self.jobs)


@dataclass(frozen=True)
class OperationRecord:
    job_id: int
    op_id: int
    machine_id: int
    start_time: int
    finish_time: int
    processing_time: int


def dispatch_spt(env: JSSPLikeEnvironment) -> Optional[int]:
    candidates = []
    for job_id, available in enumerate(env.action_mask()):
        if available:
            op = env.jobs[job_id][env.next_op[job_id]]
            candidates.append((op.processing_time, job_id))
    return min(candidates)[1] if candidates else None


def render_machine_timeline(env: JSSPLikeEnvironment, records: List[OperationRecord]) -> None:
    print("machine timeline:")
    for machine_id in range(env.num_machines):
        machine_records = [record for record in records if record.machine_id == machine_id]
        print(f"  machine {machine_id}:")
        if not machine_records:
            print("    <idle>")
            continue

        for record in machine_records:
            bar = "#" * max(1, record.processing_time)
            print(
                f"    job {record.job_id} op {record.op_id} "
                f"[{record.start_time}, {record.finish_time}) |{bar}|"
            )


def run_baseline() -> None:
    env = JSSPLikeEnvironment(toy_instance())
    state, mask = env.reset()
    sequence = []
    records: List[OperationRecord] = []

    while not env.is_done():
        action = dispatch_spt(env)
        op = env.jobs[action][env.next_op[action]]
        start_time = max(env.job_ready_time[action], env.machine_ready_time[op.machine_id])
        sequence.append(action)
        state, reward, done, info = env.step(action)
        finish_time = info.get("finish", start_time + op.processing_time)
        records.append(
            OperationRecord(
                job_id=action,
                op_id=env.next_op[action] - 1,
                machine_id=op.machine_id,
                start_time=start_time,
                finish_time=finish_time,
                processing_time=op.processing_time,
            )
        )

    render_machine_timeline(env, records)
    print("job selection sequence:", sequence)
    print("makespan:", env.makespan())
    print("workload imbalance:", env.workload_imbalance())
    print("invalid action count:", env.invalid_action_count)


if __name__ == "__main__":
    run_baseline()
