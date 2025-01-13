import sys

from itertools import permutations

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        for perm in sorted(set(permutations(self.data, self.m))):
            print(" ".join(map(str, perm)))


if __name__ == "__main__":
    Problem().solve()
