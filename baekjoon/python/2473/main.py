import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        data, minimum = sorted(self.data[:]), (math.inf, [])

        for num in range(self.n - 2):
            left, right = num + 1, self.n - 1

            while left < right:
                value = data[num] + data[left] + data[right]
                if abs(value) < minimum[0]:
                    minimum = (abs(value), [data[num], data[left], data[right]])

                if value < 0:
                    left += 1
                else:
                    right -= 1

        print(*minimum[1])


if __name__ == "__main__":
    Problem().solve()
