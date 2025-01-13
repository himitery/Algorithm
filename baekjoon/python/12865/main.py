import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.k = map(int, read().split())
        self.items = []

        for _ in range(self.n):
            weight, value = map(int, read().split())

            self.items.append({"weight": weight, "value": value})

    def solve(self) -> None:
        dp = [[0 for _ in range(self.k + 1)] for _ in range(self.n + 1)]

        for idx, item in enumerate(self.items):
            for max_weight in range(1, self.k + 1):
                if item["weight"] <= max_weight:
                    dp[idx + 1][max_weight] = max(
                        item["value"] + dp[idx][max_weight - item["weight"]],
                        dp[idx][max_weight],
                    )
                if item["weight"] > max_weight:
                    dp[idx + 1][max_weight] = dp[idx][max_weight]

        print(max([item[-1] for item in dp]))


if __name__ == "__main__":
    Problem().solve()
