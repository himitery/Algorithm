import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [tuple(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [
            [0 if row == col else math.inf for col in range(self.n)]
            for row in range(self.n)
        ]

        for size in range(2, self.n + 1):
            for start in range(self.n - size + 1):
                end = start + size - 1

                for mid in range(start, end):
                    dp[start][end] = min(
                        dp[start][end],
                        (
                            dp[start][mid]
                            + dp[mid + 1][end]
                            + self.data[start][0]
                            * self.data[mid][1]
                            * self.data[end][1]
                        ),
                    )

        print(int(dp[0][self.n - 1]))


if __name__ == "__main__":
    Problem().solve()
