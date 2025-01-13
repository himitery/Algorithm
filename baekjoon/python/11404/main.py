import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.cities = int(read())
        self.buses = [map(int, read().split()) for _ in range(int(read()))]

    def solve(self) -> None:
        dp = [
            [0 if row == col else math.inf for col in range(self.cities)]
            for row in range(self.cities)
        ]

        for src, dest, price in self.buses:
            value = dp[src - 1][dest - 1]
            dp[src - 1][dest - 1] = price if value == -1 else min(price, value)

        for stopover in range(self.cities):
            for src in range(self.cities):
                for dest in range(self.cities):
                    dp[src][dest] = min(
                        dp[src][stopover] + dp[stopover][dest], dp[src][dest]
                    )

        for src in range(self.cities):
            for dest in range(self.cities):
                if dp[src][dest] == math.inf:
                    dp[src][dest] = 0

        for row in dp:
            print(*row)


if __name__ == "__main__":
    Problem().solve()
