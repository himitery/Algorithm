import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [list(map(int, read().split())) for _ in range(2)]

    def solve(self) -> None:
        print(max(self.data[0][0], self.data[1][0]) if self.n == 1 else self.dp())

    def dp(self) -> int:
        dp = [[0] * self.n for _ in range(2)]
        dp[0][0], dp[1][0] = self.data[0][0], self.data[1][0]
        dp[0][1], dp[1][1] = self.data[0][1] + dp[1][0], self.data[1][1] + dp[0][0]

        for idx in range(2, self.n):
            dp[0][idx] = self.data[0][idx] + max(dp[1][idx - 1], dp[1][idx - 2])
            dp[1][idx] = self.data[1][idx] + max(dp[0][idx - 1], dp[0][idx - 2])

        return max(dp[0][-1], dp[1][-1])


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
