import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.c, self.n = map(int, read().split())
        self.cases = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [0 if idx == 0 else math.inf for idx in range(self.c + 101)]

        for cost, customer in self.cases:
            for idx in range(customer, self.c + 101):
                dp[idx] = min(dp[idx], dp[idx - customer] + cost)

        print(min(dp[self.c :]))


if __name__ == "__main__":
    Problem().solve()
