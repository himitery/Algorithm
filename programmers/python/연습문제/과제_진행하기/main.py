from collections import deque
from typing import List


def solution(plans: List[List[str]]) -> List[str]:
    data = sorted(
        [(plan[0], int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1]), int(plan[2])) for plan in plans],
        key=lambda p: p[1],
    )
    stack, sequence, remain = deque([]), [], 0

    for idx, (name, time, duration) in enumerate(data):
        remain = 0 if idx == 0 else time - data[idx - 1][1]
        while stack and remain:
            p_name, p_duration = stack.pop()

            if p_duration <= remain:
                sequence.append(p_name)
                remain -= p_duration
            else:
                stack.append((p_name, p_duration - remain))
                break

        stack.append((name, duration))

    while stack:
        sequence.append(stack.pop()[0])

    return sequence
