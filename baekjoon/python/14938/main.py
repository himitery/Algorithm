import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.r = map(int, read().split())
        self.items = list(map(int, read().split()))
        self.roads = [
            [16 * int(row != col) for col in range(self.n)] for row in range(self.n)
        ]

        for _ in range(self.r):
            src, dest, distance = map(int, read().split())
            self.roads[src - 1][dest - 1] = distance
            self.roads[dest - 1][src - 1] = distance

    def solve(self) -> None:
        path = self.find_path()

        maximum = 0
        for src in range(self.n):
            count = 0
            for dest in range(self.n):
                if path[src][dest] <= self.m:
                    count += self.items[dest]
            maximum = max(maximum, count)

        print(maximum)

    def find_path(self) -> list[list[int]]:
        path = self.roads[:]

        for stopover in range(self.n):
            for src in range(self.n):
                for dest in range(self.n):
                    path[src][dest] = min(
                        path[src][dest],
                        path[src][stopover] + path[stopover][dest],
                    )

        return path


if __name__ == "__main__":
    Problem().solve()
