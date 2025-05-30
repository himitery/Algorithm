import heapq
import itertools
import math
from typing import List


def solution(k: int, n: int, reqs: List[List[int]]) -> int:
    waiting = [[] for _ in range(k)]
    for a, b, c in reqs:
        waiting[c - 1].append((a, b))

    minimum = math.inf
    for batch in itertools.product(range(n - k + 1), repeat=k):
        if sum(batch) != n - k:
            continue

        minimum = min(
            minimum,
            simulate([x + 1 for x in batch], waiting),
        )

    return minimum


def simulate(mentos: List[int], waiting: List[List[int]]) -> int:
    total = 0

    for idx in range(len(mentos)):
        heap = [0] * mentos[idx]

        for start, duration in waiting[idx]:
            available_time = heapq.heappop(heap)

            wait, end = (
                (0, start + duration)
                if available_time <= start
                else (available_time - start, available_time + duration)
            )

            total += wait
            heapq.heappush(heap, end)

    return total
