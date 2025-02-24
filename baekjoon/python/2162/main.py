import sys
from collections import Counter

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.lines = []
        self.root = list(range(self.n))

        for idx in range(self.n):
            x1, y1, x2, y2 = tuple(map(int, read().split()))
            self.lines.append(((x1, y1), (x2, y2)))

    def solve(self) -> None:
        for line_x in range(self.n - 1):
            for line_y in range(line_x + 1, self.n):
                (a, b), (c, d) = self.lines[line_x], self.lines[line_y]
                if self.is_cross(a, b, c, d):
                    self.union(line_x, line_y)

        group = [self.find(num) for num in range(self.n)]
        print(len(set(group)))
        print(max(Counter(group).values()))

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def find(self, num: int) -> int:
        if num != self.root[num]:
            self.root[num] = self.find(self.root[num])
        return self.root[num]

    def is_cross(self, a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int]) -> bool:
        ccw_ab, ccw_cd = self.ccw((a, b, c)) * self.ccw((a, b, d)), self.ccw((c, d, a)) * self.ccw((c, d, b))

        if ccw_ab == 0 and ccw_cd == 0:
            return self.is_overlap(a, b, c, d)

        return ccw_ab <= 0 and ccw_cd <= 0

    def ccw(self, points: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]) -> int:
        (x1, y1), (x2, y2), (x3, y3) = points
        result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        return 0 if result == 0 else (result // abs(result))

    def is_overlap(self, a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int]) -> bool:
        return (
            min(a[0], b[0]) <= max(c[0], d[0])
            and min(c[0], d[0]) <= max(a[0], b[0])
            and min(a[1], b[1]) <= max(c[1], d[1])
            and min(c[1], d[1]) <= max(a[1], b[1])
        )


if __name__ == "__main__":
    Problem().solve()
