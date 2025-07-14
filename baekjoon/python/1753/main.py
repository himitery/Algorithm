import heapq
import math
import sys

from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.v, self.e = map(int, read().split())
        self.k = int(read())

        self.graph = defaultdict(list)
        for start, end, distance in [map(int, read().split()) for _ in range(self.e)]:
            self.graph[start].append((end, distance))

    def solve(self) -> None:
        distances = self.dijkstra()

        for vertex in range(self.v):
            print(distances[vertex] if distances[vertex] != math.inf else "INF")

    def dijkstra(self) -> list[float]:
        queue, distances = [(0, self.k)], [0 if idx == self.k else math.inf for idx in range(self.v + 1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for next_vertex, distance in self.graph[current_vertex]:
                next_distance = current_distance + distance
                if next_distance < distances[next_vertex]:
                    distances[next_vertex] = next_distance
                    heapq.heappush(queue, (next_distance, next_vertex))

        return distances[1:]


if __name__ == "__main__":
    Problem().solve()
