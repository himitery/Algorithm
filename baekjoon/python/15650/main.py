import sys

from itertools import combinations

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())

    def solve(self) -> None:
        for row in combinations([num for num in range(1, self.n + 1)], self.m):
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    Problem().solve()
