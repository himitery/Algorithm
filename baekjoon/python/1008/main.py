import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.a, self.b = map(int, read().split())

    def solve(self) -> None:
        print(self.a / self.b)


if __name__ == "__main__":
    Problem().solve()
