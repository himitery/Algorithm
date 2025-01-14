import sys

from itertools import combinations_with_replacement

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        perms = sorted(
            set(
                [
                    tuple(sorted(perm))
                    for perm in combinations_with_replacement(self.data, self.m)
                ]
            )
        )

        for perm in perms:
            print(*perm)


if __name__ == "__main__":
    Problem().solve()
