import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        print(min(*[self.find_min_cost(color) for color in range(3)]))

    def find_min_cost(self, start_color: int) -> int:
        dp = [[math.inf for _ in range(3)] for _ in range(self.n)]
        dp[0][start_color] = self.data[0][start_color]

        for row in range(1, self.n):
            dp[row][0] = min(dp[row - 1][1], dp[row - 1][2]) + self.data[row][0]
            dp[row][1] = min(dp[row - 1][0], dp[row - 1][2]) + self.data[row][1]
            dp[row][2] = min(dp[row - 1][0], dp[row - 1][1]) + self.data[row][2]

        dp[-1][start_color] = math.inf
        return int(min(dp[-1]))


if __name__ == "__main__":
    Problem().solve()
