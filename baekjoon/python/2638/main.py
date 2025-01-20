import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        graph, air_area = self.data, self.find_air_area(self.data, [], set())

        time = 0
        while True:
            melting_area = self.find_melting_area(graph, air_area)
            if not melting_area:
                break

            for y, x in melting_area:
                graph[y][x] = 0

            air_area = self.find_air_area(
                graph,
                list(melting_area),
                air_area | melting_area,
            )
            time += 1

        print(time)

    def find_air_area(
        self,
        graph: list[list[int]],
        queue: list[tuple[int, int]],
        visited: set[tuple[int, int]],
    ) -> set[tuple[int, int]]:
        queue, visited = deque(queue or [(0, 0)]), visited | {(0, 0)}
        while queue:
            y, x = queue.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    (0 <= y + dy < self.n and 0 <= x + dx < self.m)
                    and graph[y + dy][x + dx] == 0
                    and (y + dy, x + dx) not in visited
                ):
                    queue.append((y + dy, x + dx))
                    visited.add((y + dy, x + dx))

        return visited

    def find_melting_area(
        self,
        graph: list[list[int]],
        air_area: set[tuple[int, int]],
    ) -> set[tuple[int, int]]:
        area = set()
        for row in range(self.n):
            for col in range(self.m):
                if graph[row][col] == 1 and self.can_melt(air_area, (row, col)):
                    area.add((row, col))

        return area

    def can_melt(
        self,
        air_area: set[tuple[int, int]],
        position: tuple[int, int],
    ) -> bool:
        (y, x), count = position, 0
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (0 <= y + dy < self.n and 0 <= x + dx < self.m) and (
                y + dy,
                x + dx,
            ) in air_area:
                count += 1

        return count >= 2


if __name__ == "__main__":
    Problem().solve()
