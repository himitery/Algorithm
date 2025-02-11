import sys
from collections import Counter, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = Counter(map(int, read().split()))

    def solve(self) -> None:
        print(*self.find())

    def find(self) -> list[int]:
        keys = sorted(self.data.keys(), reverse=True)
        stack = deque([([key], {key: 1}) for key in keys])

        while stack:
            sequence, history = stack.pop()
            if len(sequence) == self.n:
                return sequence

            for next_key in keys:
                if next_key != sequence[-1] + 1 and self.data[next_key] - history.get(next_key, 0) > 0:
                    stack.append((sequence + [next_key], {**history, next_key: history.get(next_key, 0) + 1}))

        return []


if __name__ == "__main__":
    Problem().solve()
