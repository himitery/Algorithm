import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.matrix = [list(map(int, list(read()))) for _ in range(self.n)]

    def solve(self) -> None:
        for row in self.update_matrix():
            print(*row, sep="")

    def update_matrix(self) -> list[list[int]]:
        for count, walls in self.find_group():
            for x, y in walls:
                self.matrix[y][x] += count
                self.matrix[y][x] %= 10

        return self.matrix

    def find_group(self) -> list[tuple[int, set[tuple[int, int]]]]:
        group, stack, visited = (
            [],
            deque([(1, {(x, y)}, set()) for x in range(self.m) for y in range(self.n) if self.matrix[y][x] == 0]),
            set(),
        )

        while stack:
            count, paths, walls = stack.pop()
            if len(paths - visited) != len(paths):
                continue

            new_path = set()
            for x, y in paths:
                visited.add((x, y))

                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in visited or not (0 <= nx < self.m and 0 <= ny < self.n):
                        continue

                    if self.matrix[ny][nx] == 0:
                        new_path.add((nx, ny))
                    else:
                        walls.add((nx, ny))

            if new_path:
                stack.append((count + len(new_path), new_path, walls))
            else:
                group.append((count, walls))

        return group


if __name__ == "__main__":
    Problem().solve()
