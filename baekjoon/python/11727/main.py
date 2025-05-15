import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.mod = 10_007

    def solve(self) -> None:
        dp = [0, 1, 3] + [0] * max(1, self.n - 2)

        for num in range(3, self.n + 1):
            dp[num] = (dp[num - 1] + dp[num - 2] * 2) % self.mod

        print(dp[self.n] % self.mod)


if __name__ == "__main__":
    Problem().solve()
