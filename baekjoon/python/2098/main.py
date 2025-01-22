import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [[math.inf for _ in range(1 << self.n)] for _ in range(self.n)]
        dp[0][1 << 0] = 0

        for visited in range(1 << self.n):
            for node in range(self.n):
                if not (1 << node & visited):
                    continue

                for next_node, next_weight in enumerate(self.data[node]):
                    if (1 << next_node) & visited or next_weight == 0:
                        continue

                    dp[next_node][visited | 1 << next_node] = min(
                        dp[next_node][visited | 1 << next_node],
                        next_weight + dp[node][visited],
                    )

        minimum = math.inf
        for node in range(1, self.n):
            if self.data[node][0] != 0:
                minimum = min(minimum, dp[node][(1 << self.n) - 1] + self.data[node][0])

        print(minimum)


if __name__ == "__main__":
    Problem().solve()
