import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [0] + [list(map(int, input().split())) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [[0, 0, 0], self.data[1]]

        for num in range(2, self.n + 1):
            dp.append(
                [
                    self.data[num][0] + min(dp[num - 1][1], dp[num - 1][2]),
                    self.data[num][1] + min(dp[num - 1][0], dp[num - 1][2]),
                    self.data[num][2] + min(dp[num - 1][0], dp[num - 1][1]),
                ]
            )

        print(min(dp[self.n]))


if __name__ == "__main__":
    Problem().solve()
