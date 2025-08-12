import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.fruits = list(map(int, read().split()))

    def solve(self) -> None:
        fruit_counts, maximum, left = defaultdict(int), 0, 0

        for right in range(self.n):
            fruit_counts[self.fruits[right]] += 1

            while len(fruit_counts) > 2:
                fruit_counts[self.fruits[left]] -= 1
                if fruit_counts[self.fruits[left]] == 0:
                    del fruit_counts[self.fruits[left]]

                left += 1

            maximum = max(maximum, right - left + 1)

        print(maximum)


if __name__ == "__main__":
    Problem().solve()
