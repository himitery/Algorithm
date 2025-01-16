import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.row, self.col, self.time = map(int, read().split())
        self.data = [list(map(int, read().split())) for _ in range(self.row)]

    def solve(self) -> None:
        air_purifiers, graph = self.find_air_purifiers(), self.data[:]

        for _ in range(self.time):
            graph = self.spread_dust(graph)
            graph = self.filter_dust(air_purifiers, graph)

        print(self.calculate_dust(graph))

    def find_air_purifiers(self) -> tuple[tuple[int, int], tuple[int, int]]:
        for idx in range(self.row - 1):
            if self.data[idx][0] == -1:
                return (idx, 0), (idx + 1, 0)

    def spread_dust(self, graph: list[list[int]]) -> list[list[int]]:
        diff = [[0 for _ in range(self.col)] for _ in range(self.row)]

        for row in range(self.row):
            for col in range(self.col):
                if graph[row][col] > 1:
                    dust, count = graph[row][col] // 5, 0
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_x, new_y = col + dx, row + dy
                        if (
                            0 <= new_x < self.col
                            and 0 <= new_y < self.row
                            and graph[new_y][new_x] != -1
                        ):
                            diff[new_y][new_x] += dust
                            count += 1

                    diff[row][col] -= count * dust

        for row in range(self.row):
            for col in range(self.col):
                graph[row][col] += diff[row][col]

        return graph

    def filter_dust(
        self,
        air_purifiers: tuple[tuple[int, int], tuple[int, int]],
        graph: list[list[int]],
    ) -> list[list[int]]:
        y, x = air_purifiers[0]
        for idx in range(y - 1, 0, -1):
            graph[idx][0] = graph[idx - 1][0]
        graph[0] = graph[0][1:] + [0]
        for idx in range(y):
            graph[idx][-1] = graph[idx + 1][-1]
        graph[y] = [-1, 0] + graph[y][1:-1]

        y, x = air_purifiers[1]
        for idx in range(y + 1, self.row - 1):
            graph[idx][0] = graph[idx + 1][0]
        graph[-1] = graph[-1][1:] + [0]
        for idx in range(self.row - 1, y, -1):
            graph[idx][-1] = graph[idx - 1][-1]
        graph[y] = [-1, 0] + graph[y][1:-1]

        return graph

    def calculate_dust(self, graph: list[list[int]]) -> int:
        count = 0
        for row in graph:
            for value in row:
                if value != -1:
                    count += value

        return count


if __name__ == "__main__":
    Problem().solve()
