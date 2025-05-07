import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.d, self.p, self.q = map(int, read().split())

    def solve(self) -> None:
        print(self.find_minimum())

    def find_minimum(self) -> int:
        if self.d % self.p == 0 or self.d % self.q == 0:
            return self.d

        p, q = max(self.p, self.q), min(self.p, self.q)

        minimum = math.inf
        for p_count in range(min(self.d // p, q) + 2):
            total = p_count * p
            if total >= self.d:
                minimum = min(minimum, total)
                break

            minimum = min(minimum, total + math.ceil((self.d - total) / q) * q)

        return minimum


if __name__ == "__main__":
    Problem().solve()
