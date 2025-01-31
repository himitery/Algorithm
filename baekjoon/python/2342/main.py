import heapq
import math
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.data = list(map(int, read().split()))[:-1]

    def solve(self) -> None:
        queue, visited = [(0, 0, (0, 0))], defaultdict(lambda: math.inf)

        while queue:
            weight, step, (left, right) = heapq.heappop(queue)
            if step == len(self.data):
                print(weight)
                break

            if weight >= visited[(step, left, right)]:
                continue

            visited[(step, left, right)] = weight

            target = self.data[step]
            if target != left:
                heapq.heappush(
                    queue,
                    (
                        weight + self.calculate_weight(right, target),
                        step + 1,
                        (left, target),
                    ),
                )

            if target != right:
                heapq.heappush(
                    queue,
                    (
                        weight + self.calculate_weight(left, target),
                        step + 1,
                        (target, right),
                    ),
                )

    def calculate_weight(self, start: int, end: int) -> int:
        if start == end:
            return 1

        if start == 0 or end == 0:
            return 2

        return 4 if abs(start - end) == 2 else 3


if __name__ == "__main__":
    Problem().solve()
