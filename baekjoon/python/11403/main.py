import itertools
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.graph = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        for stopover, start, end in itertools.product(range(self.n), repeat=3):
            if self.graph[start][stopover] and self.graph[stopover][end]:
                self.graph[start][end] = 1

        for row in self.graph:
            print(*row)


if __name__ == "__main__":
    Problem().solve()
