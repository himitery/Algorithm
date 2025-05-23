import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        print(self.find_minimum(self.n))

    def find_minimum(self, num: int) -> int:
        if math.isqrt(num) ** 2 == num:
            return 1

        while num % 4 == 0:
            num //= 4

        if num % 8 == 7:
            return 4

        for idx in range(1, math.isqrt(self.n) + 1):
            if math.isqrt(self.n - idx**2) ** 2 == self.n - idx**2:
                return 2

        return 3


if __name__ == "__main__":
    Problem().solve()
