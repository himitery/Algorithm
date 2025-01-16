import sys
from collections import deque
from itertools import combinations

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.row, self.col = map(int, read().split())
        self.data = [list(map(int, read().split())) for _ in range(self.row)]

    def solve(self) -> None:
        normal_area, virus_area = self.find_area()
        size_of_normal_area, size_of_virus_area = len(normal_area), len(virus_area)

        maximum, min_count = 0, self.row * self.col
        for walls in combinations(normal_area, 3):
            count = self.count_virus_area(virus_area, list(walls), min_count)
            if count < min_count:
                min_count = count
                maximum = size_of_normal_area - (min_count - size_of_virus_area + 3)

        print(maximum)

    def find_area(self) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        normal, virus = [], []
        for row in range(self.row):
            for col in range(self.col):
                if self.data[row][col] == 0:
                    normal.extend([(row, col)])
                elif self.data[row][col] == 2:
                    virus.append((row, col))

        return normal, virus

    def can_move(self, row: int, col: int) -> bool:
        return 0 <= row < self.row and 0 <= col < self.col

    def count_virus_area(
        self,
        virus_area: list[tuple[int, int]],
        walls: list[tuple[int, int]],
        min_count: int,
    ) -> int:
        queue, visited = deque(virus_area), {*virus_area}

        while queue:
            row, col = queue.popleft()
            if len(visited) >= min_count:
                return len(visited)

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (
                    self.can_move(row + y, col + x)
                    and (row + y, col + x) not in walls
                    and self.data[row + y][col + x] == 0
                    and (row + y, col + x) not in visited
                ):
                    visited.add((row + y, col + x))
                    queue.append((row + y, col + x))

        return len(visited)


if __name__ == "__main__":
    Problem().solve()
