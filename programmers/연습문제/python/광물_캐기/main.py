import math

from collections import deque


def solution(picks, minerals):
    n = len(minerals)
    stack, minimum = deque([(0, 0, picks)]), math.inf

    mineral_cost = {"diamond": 25, "iron": 5, "stone": 1}
    while stack:
        idx, cost, remains = stack.pop()
        if cost > minimum:
            continue

        if idx == (n // 5 + int(n % 5 != 0)) or sum(remains) == 0:
            minimum = min(minimum, cost)
            continue

        for pick, remain in enumerate(remains):
            if remain == 0:
                continue

            new_cost = 0
            for mineral in minerals[idx * 5 : min((idx + 1) * 5, n)]:
                new_cost += max(mineral_cost[mineral] // 5 ** (2 - pick), 1)

            new_remains = remains[:]
            new_remains[pick] -= 1

            stack.append((idx + 1, cost + new_cost, new_remains))

    return minimum
