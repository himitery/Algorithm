import itertools
import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.grid = [read() for _ in range(self.n)]

    def solve(self) -> None:
        print(self.count_areas(is_weak=False), self.count_areas(is_weak=True))

    def count_areas(self, is_weak: bool) -> int:
        count, visited = 0, set()

        for x, y in itertools.product(range(self.n), repeat=2):
            if (x, y) not in visited:
                visited = self.bfs(x, y, visited, is_weak)
                count += 1

        return count

    def bfs(self, x: int, y: int, visited: set[tuple[int, int]], is_weak: bool) -> set[tuple[int, int]]:
        queue, visited = deque([(x, y)]), visited | {(x, y)}

        while queue:
            current_x, current_y = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = current_x + dx, current_y + dy
                if not (0 <= nx < self.n and 0 <= ny < self.n) or (nx, ny) in visited:
                    continue

                if (is_weak and (self.grid[x][y] in "RG") and (self.grid[nx][ny] in "RG")) or (
                    self.grid[x][y] == self.grid[nx][ny]
                ):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return visited


if __name__ == "__main__":
    Problem().solve()
