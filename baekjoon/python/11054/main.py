import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.size = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        up, down = [1] * self.size, [1] * self.size

        for end in range(1, self.size):
            for start in range(end):
                if self.data[start] < self.data[end]:
                    up[end] = max(up[end], up[start] + 1)

        for end in range(self.size - 1, 0, -1):
            for start in range(end):
                if self.data[start] > self.data[end]:
                    down[start] = max(down[start], down[end] + 1)

        maximum = 0
        for idx in range(self.size):
            maximum = max(maximum, up[idx] + down[idx] - 1)
        print(maximum)


if __name__ == "__main__":
    Problem().solve()
