import math
import sys
from functools import lru_cache
from itertools import combinations

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.store, self.house = [], []

        for row in range(self.n):
            for col, value in enumerate(list(map(int, read().split()))):
                if value == 1:
                    self.house.append((row, col))
                if value == 2:
                    self.store.append((row, col))

    def solve(self) -> None:
        candidates = list(
            filter(lambda perm: len(perm) == self.m, combinations(self.store, self.m))
        )

        minimum = math.inf
        for candidate in candidates:
            values = []
            for dest in self.house:
                values.append(
                    min([self.calculate_diff(src, dest) for src in candidate])
                )
            minimum = min(sum(values), minimum)

        print(minimum)

    @lru_cache
    def calculate_diff(self, src: tuple[int, int], dest: tuple[int, int]) -> int:
        return abs(src[0] - dest[0]) + abs(src[1] - dest[1])


if __name__ == "__main__":
    Problem().solve()
