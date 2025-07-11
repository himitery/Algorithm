import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.matrix = [list(map(int, read())) for _ in range(self.n)]

    def solve(self) -> None:
        print(self.dijkstra())

    def dijkstra(self) -> int:
        queue, visited = deque([((0, 0), 1, True)]), {(True, 0, 0)}

        while queue:
            (x, y), depth, can_break = queue.popleft()
            if (x, y) == (self.m - 1, self.n - 1):
                return depth

            for nx, ny in [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                if not (0 <= nx < self.m and 0 <= ny < self.n):
                    continue

                if self.matrix[ny][nx] == 0 and (can_break, nx, ny) not in visited:
                    visited.add((can_break, nx, ny))
                    queue.append(((nx, ny), depth + 1, can_break))

                if self.matrix[ny][nx] == 1 and can_break and (False, nx, ny) not in visited:
                    visited.add((False, nx, ny))
                    queue.append(((nx, ny), depth + 1, False))

        return -1


if __name__ == "__main__":
    Problem().solve()
