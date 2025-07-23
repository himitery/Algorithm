import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        first = list(map(int, read().split()))
        min_dp, max_dp = first, first

        for _ in range(self.n - 1):
            row = list(map(int, read().split()))

            min_dp, max_dp = (
                [
                    row[0] + min(min_dp[0], min_dp[1]),
                    row[1] + min(min_dp[0], min_dp[1], min_dp[2]),
                    row[2] + min(min_dp[1], min_dp[2]),
                ],
                [
                    row[0] + max(max_dp[0], max_dp[1]),
                    row[1] + max(max_dp[0], max_dp[1], max_dp[2]),
                    row[2] + max(max_dp[1], max_dp[2]),
                ],
            )

        print(max(max_dp), min(min_dp))


if __name__ == "__main__":
    Problem().solve()
