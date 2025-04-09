import itertools
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.grid = [list(map(lambda x: int(x == "."), list(read()))) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [defaultdict(int) for _ in range(self.n)]
        for state in self.find_states(0):
            dp[0][state] = self.count_one(state)

        for row in range(1, self.n):
            for current, previous in itertools.product(self.find_states(row), dp[row - 1]):
                if (current & (previous << 1)) == (current & (previous >> 1)) == 0:
                    dp[row][current] = max(dp[row][current], dp[row - 1][previous] + self.count_one(current))

        print(max([x for x in dp[-1].values()]))

    def find_states(self, row: int) -> list[int]:
        blocked = 0
        for col in range(self.m):
            if self.grid[row][col] == 0:
                blocked |= 1 << col

        return [state for state in range(1 << self.m) if (state & blocked) == 0 and (state & (state >> 1)) == 0]

    def count_one(self, num: int):
        return bin(num).count("1")


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
