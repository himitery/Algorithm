import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        left, right = 0, self.n - 1
        minimum, result = math.inf, (left, right)

        while 0 <= left < right < self.n:
            if abs(self.data[left] + self.data[right]) < minimum:
                minimum = abs(self.data[left] + self.data[right])
                result = (self.data[left], self.data[right])

            if self.data[left] + self.data[right] == 0:
                break
            elif self.data[left] + self.data[right] < 0:
                left += 1
            elif self.data[left] + self.data[right] > 0:
                right -= 1

        print(*result)


if __name__ == "__main__":
    Problem().solve()
