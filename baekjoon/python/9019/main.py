import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


precomputed = [
    {
        "D": (idx * 2) % 10_000,
        "S": idx - 1 if idx > 0 else 9_999,
        "L": (idx % 1_000) * 10 + (idx // 1_000),
        "R": (idx % 10) * 1_000 + (idx // 10),
    }
    for idx in range(10_000)
]


class Problem:
    def __init__(self):
        self.initial, self.target = map(int, read().split())

    def solve(self) -> None:
        print(self.bfs())

    def bfs(self) -> str:
        queue, visited, prev, command = deque([self.initial]), {self.initial}, [-1] * 10_000, [""] * 10_000

        while queue:
            current = queue.popleft()

            for op, next_value in precomputed[current].items():
                if next_value not in visited:
                    visited.add(next_value)
                    prev[next_value], command[next_value] = current, op

                    if next_value == self.target:
                        path, trace = [], self.target
                        while trace != self.initial:
                            path.append(command[trace])
                            trace = prev[trace]

                        return "".join(reversed(path))

                    queue.append(next_value)

        return ""


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
