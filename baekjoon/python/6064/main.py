import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.m, self.n, self.x, self.y = map(int, read().split(" "))

    def solve(self) -> None:
        print(self.find())

    def find(self) -> int:
        for value in range(self.x, self.m * self.n + 1, self.m):
            if value % self.n == self.y or (self.n == self.y and value % self.n == 0):
                return value

        return -1


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
