import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.memories = list(map(int, read().split()))
        self.weights = list(map(int, read().split()))

    def solve(self) -> None:
        max_weights = sum(self.weights)
        dp, maximum = [0 for _ in range(max_weights + 1)], max_weights

        for idx in range(self.n):
            for weight in range(max_weights, self.weights[idx] - 1, -1):
                dp[weight] = max(
                    dp[weight],
                    dp[weight - self.weights[idx]] + self.memories[idx],
                )
                if dp[weight] >= self.m:
                    maximum = min(maximum, weight)

        print(maximum)


if __name__ == "__main__":
    Problem().solve()
