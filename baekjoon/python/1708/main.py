import math
import sys
from typing import cast

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.coordinates = sorted(
            {cast(tuple[int, int], tuple(map(int, read().split()))) for _ in range(self.n)},
            key=lambda p: (p[1], p[0]),
        )

    def solve(self) -> None:
        coords, stack = self.find_sorted_by_angle(), []

        for point in coords:
            while len(stack) >= 2 and self.ccw(*stack[-2], *stack[-1], *point) <= 0:
                stack.pop()

            stack.append(point)

        print(len(stack))

    def find_sorted_by_angle(self) -> list[tuple[int, int]]:
        start = self.coordinates[0]

        return [start] + sorted(
            self.coordinates[1:],
            key=lambda p: (
                math.atan2(p[1] - start[1], p[0] - start[0]),
                (p[1] - start[1]) ** 2 + (p[0] - start[0]) ** 2,
            ),
        )

    def ccw(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
        return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


if __name__ == "__main__":
    Problem().solve()
