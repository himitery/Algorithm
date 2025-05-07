import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [tuple(map(int, read().split())) for _ in range(self.n)]

        self.mod = 1_000_000_007

    def solve(self) -> None:
        factorial, inverse_factorial = self.precompute_factorial()

        for n, r in self.data:
            print(self.comb(factorial, inverse_factorial, n, r))

    def precompute_factorial(self) -> tuple[list[int], list[int]]:
        maximum = max(n for n, _ in self.data)
        factorial, inverse_factorial = [1] * (maximum + 1), [1] * (maximum + 1)

        for idx in range(1, maximum + 1):
            factorial[idx] = factorial[idx - 1] * idx % self.mod

        inverse_factorial[maximum] = pow(factorial[maximum], self.mod - 2, self.mod)
        for idx in range(maximum - 1, -1, -1):
            inverse_factorial[idx] = inverse_factorial[idx + 1] * (idx + 1) % self.mod

        return factorial, inverse_factorial

    def comb(self, factorial: list[int], inverse_factorial: list[int], n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0

        return factorial[n] * inverse_factorial[r] % self.mod * inverse_factorial[n - r] % self.mod


if __name__ == "__main__":
    Problem().solve()
