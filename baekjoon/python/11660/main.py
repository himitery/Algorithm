import itertools
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [list(map(int, read().split())) for _ in range(self.n)]
        self.queries = [list(map(int, read().split())) for _ in range(self.m)]

    def solve(self) -> None:
        prefix = self.calculate_prefix_sum()

        for x1, y1, x2, y2 in self.queries:
            print(prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])

    def calculate_prefix_sum(self) -> list[list[int]]:
        prefix = [[0] * (self.n + 1) for _ in range(self.n + 1)]
        for x, y in itertools.product(range(1, self.n + 1), repeat=2):
            prefix[y][x] = self.data[y - 1][x - 1] + prefix[y - 1][x] + prefix[y][x - 1] - prefix[y - 1][x - 1]

        return prefix


if __name__ == "__main__":
    Problem().solve()
