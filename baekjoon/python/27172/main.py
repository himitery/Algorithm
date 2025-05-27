import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        data, values, scores = (
            sorted((value, idx) for idx, value in enumerate(self.data)),
            defaultdict(int),
            [0 for _ in range(self.n)],
        )
        for idx, value in enumerate(self.data):
            values[value] = idx

        for value, idx in data:
            for num in range(value * 2, data[-1][0] + 1, value):
                if num in values:
                    scores[idx] += 1
                    scores[values[num]] -= 1

        print(*scores)


if __name__ == "__main__":
    Problem().solve()
