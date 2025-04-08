import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.w = map(int, read().split())
        self.inner, self.outer = list(map(int, read().split())), list(map(int, read().split()))

    def solve(self) -> None:
        if self.n == 1:
            print(2 - int(self.inner[0] + self.outer[0] <= self.w))
            return

        minimum = min(
            self.find_minimum(
                [[1, 1, 2 - int(self.inner[0] + self.outer[0] <= self.w)]] + [[0, 0, 0] for _ in range(self.n - 1)],
                self.inner[:],
                self.outer[:],
            )[-1][2],
            (
                math.inf
                if self.inner[-1] + self.inner[0] > self.w
                else self.find_minimum(
                    [[1, 1, 2]] + [[0, 0, 0] for _ in range(self.n - 1)],
                    [math.inf] + self.inner[1:-1] + [math.inf],
                    self.outer[:],
                )[-1][1]
            ),
            (
                math.inf
                if self.outer[-1] + self.outer[0] > self.w
                else self.find_minimum(
                    [[1, 1, 2]] + [[0, 0, 0] for _ in range(self.n - 1)],
                    self.inner[:],
                    [math.inf] + self.outer[1:-1] + [math.inf],
                )[-1][0]
            ),
            (
                math.inf
                if (self.inner[-1] + self.inner[0] > self.w) or (self.outer[-1] + self.outer[0] > self.w)
                else self.find_minimum(
                    [[1, 1, 2]] + [[0, 0, 0] for _ in range(self.n - 1)],
                    [math.inf] + self.inner[1:-1] + [math.inf],
                    [math.inf] + self.outer[1:-1] + [math.inf],
                )[-2][2]
            ),
        )

        print(minimum)

    def find_minimum(self, dp: list[list[int]], inner: list[float], outer: list[float]) -> list[list[int]]:
        for idx in range(1, self.n):
            inner_count = 2 - int(inner[idx - 1] + inner[idx] <= self.w)
            outer_count = 2 - int(outer[idx - 1] + outer[idx] <= self.w)
            vertical_count = 2 - int(inner[idx] + outer[idx] <= self.w)

            dp[idx] = [
                min(dp[idx - 1][1] + inner_count, dp[idx - 1][2] + 1),
                min(dp[idx - 1][0] + outer_count, dp[idx - 1][2] + 1),
                min(
                    dp[idx - 2][2] + inner_count + outer_count,
                    dp[idx - 1][0] + outer_count + 1,
                    dp[idx - 1][1] + inner_count + 1,
                    dp[idx - 1][2] + vertical_count,
                ),
            ]

        return dp


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
