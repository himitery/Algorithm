import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        line = list(map(int, read().split()))

        self.n, self.coordinates = line[0], []
        for idx in range(self.n):
            self.coordinates.append((line[idx * 2 + 1], line[idx * 2 + 2], idx))

    def solve(self) -> None:
        coords = sorted(self.coordinates, key=lambda p: (p[1], p[0]))
        start_point = coords[0]
        others = sorted(
            coords[1:],
            key=lambda p: (
                math.atan2(p[1] - start_point[1], p[0] - start_point[0]),
                (p[0] - start_point[0]) ** 2 + (p[1] - start_point[1]) ** 2,
            ),
        )

        last_collinear = []
        if self.n > 1:
            last_collinear.append(others[-1])

            for idx in range(len(others) - 2, -1, -1):
                if self.ccw(start_point, others[-1], others[idx]) != 0:
                    break

                last_collinear.append(others[idx])

        print(*[p[2] for p in [start_point] + others[: len(others) - len(last_collinear)] + last_collinear])

    def ccw(self, p1: tuple[int, int, int], p2: tuple[int, int, int], p3: tuple[int, int, int]) -> int:
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
