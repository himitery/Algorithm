import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.mod = 1_000_000_000

    def solve(self) -> None:
        dp = [[[0] * 2**10 for _ in range(10)] for _ in range(self.n + 1)]
        for num in range(1, 10):
            dp[1][num][1 << num] = 1

        for size in range(1, self.n):
            for num in range(10):
                for bit in range(2**10):
                    if dp[size][num][bit] == 0:
                        continue

                    for next_num in filter(lambda x: 0 <= x <= 9, [num - 1, num + 1]):
                        dp[size + 1][next_num][bit | (1 << next_num)] += dp[size][num][bit]
                        dp[size + 1][next_num][bit | (1 << next_num)] %= self.mod

        print(sum([dp[self.n][num][-1] for num in range(10)]) % self.mod)


if __name__ == "__main__":
    Problem().solve()
