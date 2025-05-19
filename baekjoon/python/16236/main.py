import heapq
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.graph = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        graph = self.graph
        shark = self.find_shark(graph)

        shark_size, weight, time = 2, 0, 0
        while True:
            found = self.find_nearest_fish(
                graph,
                shark,
                shark_size,
            )
            if not found:
                break

            (y, x), append_time = found

            weight += 1
            if weight == shark_size:
                shark_size += 1
                weight = 0

            time += append_time
            graph[shark[0]][shark[1]] = 0
            shark = (y, x)
            graph[shark[0]][shark[1]] = 9

        print(time)

    def find_shark(
        self,
        graph: list[list[int]],
    ) -> tuple[int, int]:
        for row in range(self.n):
            for col in range(self.n):
                if graph[row][col] == 9:
                    return row, col

    def find_nearest_fish(
        self,
        graph: list[list[int]],
        shark: tuple[int, int],
        shark_size: int,
    ) -> tuple[tuple[int, int], int] | None:
        queue, visited, found = [(shark, 0)], {shark}, []
        while queue and not found:
            candidates = []
            for (y, x), time in queue:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (
                        (0 <= x + dx < self.n and 0 <= y + dy < self.n)
                        and graph[y + dy][x + dx] <= shark_size
                        and (
                            y + dy,
                            x + dx,
                        )
                        not in visited
                    ):
                        candidates.append(((y + dy, x + dx), time + 1))
                        visited.add((y + dy, x + dx))
                        if 0 < graph[y + dy][x + dx] < shark_size:
                            heapq.heappush(
                                found, ((y + dy, x + dx), ((y + dy, x + dx), time + 1))
                            )

            queue = candidates

        if found:
            return heapq.heappop(found)[1]

        return None


if __name__ == "__main__":
    Problem().solve()
