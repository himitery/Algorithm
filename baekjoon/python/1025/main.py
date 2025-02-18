import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [list(map(int, read())) for _ in range(self.n)]

    def solve(self) -> None:
        maximum = -1
        for dx in range(self.m + 1):
            for dy in range(self.n + 1):
                if dx == 0 and dy == 0:
                    continue

                for value in self.find_num(dx, dy) + self.find_num(-dx, dy):
                    maximum = max(maximum, value)

        print(maximum)

    def find_num(self, dx: int, dy: int) -> list[int]:
        results = []
        for start_x in range(self.m):
            for start_y in range(self.n):
                x, y, num_str = start_x, start_y, ""
                while 0 <= x < self.m and 0 <= y < self.n:
                    num_str += str(self.data[y][x])
                    results.extend(filter(lambda n: int(n) == int(int(n) ** 0.5) ** 2, [num_str, num_str[-1::-1]]))
                    x, y = x + dx, y + dy

        return list(map(int, results))


if __name__ == "__main__":
    Problem().solve()
