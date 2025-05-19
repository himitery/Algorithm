import itertools
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.mod = 10_007

    def solve(self) -> None:
        cached = [[int(x == 0) for x in range(53)] for _ in range(53)]
        for x, y in itertools.product(range(53), repeat=2):
            cached[y][x] = (
                1 if x == y else (cached[y - 1][x - 1] + cached[y - 1][x]) % self.mod
            )

        result = 0
        for num in range(1, self.n // 4 + 1):
            ways = cached[13][num] * cached[52 - 4 * num][self.n - 4 * num] % self.mod
            result = (
                (result + ways) % self.mod
                if num % 2 == 1
                else (result - ways + self.mod) % self.mod
            )

        print(result)


if __name__ == "__main__":
    Problem().solve()
