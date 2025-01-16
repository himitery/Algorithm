import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.m = int(read())
        self.data = [tuple(map(int, read().split())) for _ in range(self.m)]
        self.mod = 1_000_000_007

    def solve(self) -> None:
        values = [
            (self.find_square(n, self.mod - 2) * s) % self.mod if s % n != 0 else s // n
            for n, s in self.data
        ]

        print(sum(values) % self.mod)

    def find_square(self, num: int, mod: int) -> int:
        res = 1
        while mod > 0:
            if mod % 2 == 1:
                res *= num % self.mod
            mod //= 2
            num = num**2 % self.mod

        return res % self.mod


if __name__ == "__main__":
    Problem().solve()
