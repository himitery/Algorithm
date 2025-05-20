import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, read().split())
        self.x3, self.y3, self.x4, self.y4 = map(int, read().split())

    def solve(self) -> None:
        a, b, c, d = (self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3), (self.x4, self.y4)
        ccw_ab, ccw_cd = self.ccw(a, b, c) * self.ccw(a, b, d), self.ccw(c, d, a) * self.ccw(c, d, b)

        result = ccw_ab <= 0 and ccw_cd <= 0
        if ccw_ab == 0 and ccw_cd == 0:
            result = self.is_overlap(a, b, c, d)

        print(int(result))

    def ccw(self, point1: tuple[int, int], point2: tuple[int, int], point3: tuple[int, int]) -> int:
        result = (point2[0] - point1[0]) * (point3[1] - point1[1]) - (point2[1] - point1[1]) * (point3[0] - point1[0])
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
