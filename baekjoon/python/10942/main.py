import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))
        self.m = int(read())
        self.questions = [
            tuple(map(lambda x: int(x) - 1, read().split())) for _ in range(self.m)
        ]

    def solve(self) -> None:
        dp = [[row == col for col in range(self.n)] for row in range(self.n)]

        for size in range(2, self.n + 1):
            for idx in range(self.n - size + 1):
                if self.data[idx] == self.data[idx + size - 1] and (
                    size <= 2 or dp[idx + 1][idx + size - 2]
                ):
                    dp[idx][idx + size - 1] = True

        for src, dest in self.questions:
            print(int(dp[src][dest]))


if __name__ == "__main__":
    Problem().solve()
