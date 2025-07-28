import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.a, self.b, self.c = map(int, read().split())

    def solve(self) -> None:
        print(pow(self.a, self.b, self.c))


if __name__ == "__main__":
    Problem().solve()
