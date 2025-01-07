import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.k = list(map(int, read().split()))

    def solve(self) -> None:
        result: int = 1
        for idx in range(self.n - self.k + 1, self.n + 1):
            result *= idx

        for idx in range(2, self.k + 1):
            result //= idx

        print(result)


if __name__ == "__main__":
    Problem().solve()
