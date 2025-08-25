import math
import sys
from collections import deque
from typing import cast

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self, step: int):
        self.n, self.step = int(read()), step
        if self.n == 0:
            raise StopIteration

        self.coords = [cast(tuple[int, int], tuple(map(int, read().split()))) for _ in range(self.n)]

    def solve(self) -> None:
        if self.n < 2:
            print(f"Case {self.step}: 0.00")
            return

        hull = self.get_convex_hull()
        if len(hull) < 3:
            print(f"Case {self.step}: 0.00")
            return

        min_width_sq = math.inf

        x = 1
        for idx in range(len(hull)):
            p1, p2 = hull[idx], hull[(idx + 1) % len(hull)]
            while self.ccw(p1, p2, hull[x]) < self.ccw(p1, p2, hull[(x + 1) % len(hull)]):
                x = (x + 1) % len(hull)

            area_sq, dist_sq = self.ccw(p1, p2, hull[x]) ** 2, (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
            if dist_sq != 0:
                min_width_sq = min(min_width_sq, area_sq / dist_sq)

        print(f"Case {self.step}: {math.ceil((math.sqrt(min_width_sq) - 1e-9) * 100) / 100.0:.2f}")

    def get_convex_hull(self) -> list[tuple[int, int]]:
        self.coords.sort(key=lambda p: (p[1], p[0]))
        start_point = self.coords[0]

        sorted_coords = sorted(
            self.coords[1:],
            key=lambda p: (
                math.atan2(p[1] - start_point[1], p[0] - start_point[0]),
                (p[0] - start_point[0]) ** 2 + (p[1] - start_point[1]) ** 2,
            ),
        )

        hull = deque([start_point])
        for point in sorted_coords:
            while len(hull) >= 2 and self.ccw(hull[-2], hull[-1], point) <= 0:
                hull.pop()

            hull.append(point)

        return list(hull)

    def ccw(self, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> int:
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


if __name__ == "__main__":
    _step = 1
    while True:
        try:
            Problem(_step).solve()
            _step += 1
        except StopIteration:
            break
        except (EOFError, ValueError):
            break
