import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.nums = [read() for _ in range(self.n)]
        self.k = int(read())

    def solve(self) -> None:
        mod_nums, len_nums = [int(num) % self.k for num in self.nums], [len(num) for num in self.nums]
        max_len = max(len_nums)

        pow_ten = [1 for _ in range(max_len + 1)]
        for idx in range(max_len):
            pow_ten[idx + 1] = (pow_ten[idx] * 10) % self.k

        dp = [[0 for _ in range(self.k)] for _ in range(1 << self.n)]
        dp[0][0] = 1

        for mask in range(1 << self.n):
            for idx in range(self.n):
                if mask & (1 << idx):
                    continue

                for remain in range(self.k):
                    next_remain = (remain * pow_ten[len_nums[idx]] + mod_nums[idx]) % self.k
                    dp[mask | (1 << idx)][next_remain] += dp[mask][remain]

        numerator, denominator = dp[(1 << self.n) - 1][0], math.factorial(self.n)
        gcd = math.gcd(dp[(1 << self.n) - 1][0], math.factorial(self.n))

        print(f"{numerator // gcd}/{denominator // gcd}")


if __name__ == "__main__":
    Problem().solve()
