import heapq
import sys

from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.e = map(int, read().split())

        self.graph = defaultdict(list)
        for src, dest, distance in [map(int, read().split()) for _ in range(self.e)]:
            self.graph[src - 1].append((dest - 1, distance))
            self.graph[dest - 1].append((src - 1, distance))

        self.stopover = list(map(lambda x: int(x) - 1, read().split()))

    def solve(self) -> None:
        print(
            min(
                self.calculate_total_distance(
                    [
                        (0, self.stopover[0]),
                        (self.stopover[0], self.stopover[1]),
                        (self.stopover[1], self.n - 1),
                    ]
                ),
                self.calculate_total_distance(
                    [
                        (0, self.stopover[1]),
                        (self.stopover[1], self.stopover[0]),
                        (self.stopover[0], self.n - 1),
                    ]
                ),
            )
        )

    def dijkstra(self, start: int, end: int) -> int:
        if start == end:
            return 0

        heap, distances = [(0, start)], [-1] * (self.n + 1)

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            if current_vertex == end:
                return distances[end]

            if distances[current_vertex] is not -1 and current_distance > distances[current_vertex]:
                continue

            for next_vertex, distance in self.graph[current_vertex]:
                if distances[next_vertex] is -1 or current_distance + distance < distances[next_vertex]:
                    distances[next_vertex] = current_distance + distance
                    heapq.heappush(heap, (current_distance + distance, next_vertex))

        return -1

    def calculate_total_distance(self, paths: list[tuple[int, int]]) -> int:
        distances = [self.dijkstra(path[0], path[1]) for path in paths]

        return -1 if any(distance == -1 for distance in distances) else sum(distances)


if __name__ == "__main__":
    Problem().solve()
