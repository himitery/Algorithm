import itertools
import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [list(read()) for _ in range(self.n)]

    def solve(self) -> None:
        print(res if (res := self.bfs(self.find_start())) else "TT")

    def find_start(self) -> tuple[int, int]:
        for x, y in itertools.product(range(self.m), range(self.n)):
            if self.data[y][x] == "I":
                return x, y

        return -1, -1

    def bfs(self, start: tuple[int, int]) -> int:
        queue, visited, count = deque([start]), {start}, 0

        while queue:
            x, y = queue.popleft()
            if self.data[y][x] == "P":
                count += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in visited and self.data[ny][nx] != "X":
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return count


if __name__ == "__main__":
    Problem().solve()
