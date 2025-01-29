import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.s = map(int, read().split())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        print(self.find_min_length() if self.s != 0 else 0)

    def find_min_length(self) -> int:
        minimum, left, total = self.n + 1, 0, 0

        for right in range(self.n):
            total += self.data[right]

            while total >= self.s:
                minimum = min(minimum, right - left + 1)
                total -= self.data[left]
                left += 1

        return minimum if minimum <= self.n else 0


if __name__ == "__main__":
    Problem().solve()
