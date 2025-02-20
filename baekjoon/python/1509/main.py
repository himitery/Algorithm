import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.data = list(read())
        self.size = len(self.data)

    def solve(self) -> None:
        palindrome, dp = self.find_palindrome(), [math.inf for _ in range(self.size)]

        for end in range(self.size):
            if palindrome[0][end]:
                dp[end] = 1
                continue

            for mid in range(end):
                if palindrome[mid + 1][end]:
                    dp[end] = min(dp[end], dp[mid] + 1)

        print(dp[-1])

    def find_palindrome(self) -> list[list[bool]]:
        palindrome = [[True for _ in range(self.size)] for _ in range(self.size)]
        for size in range(1, self.size):
            for start in range(self.size - size):
                end = start + size
                palindrome[start][end] = self.data[start] == self.data[end] and palindrome[start + 1][end - 1]

        return palindrome


if __name__ == "__main__":
    Problem().solve()
