import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [tuple(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        area = 0
        for idx in range(self.n):
            area += (
                self.data[idx][0] * self.data[(idx + 1) % self.n][1]
                - self.data[idx][1] * self.data[(idx + 1) % self.n][0]
            )

        print(round(abs(area) / 2, 1))


if __name__ == "__main__":
    Problem().solve()
