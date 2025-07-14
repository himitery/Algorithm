import heapq
import math
import sys

from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

        self.graph = defaultdict(list)
        for src, dest, distance in [map(int, read().split()) for _ in range(self.n - 1)]:
            self.graph[src].append((dest, distance))
            self.graph[dest].append((src, distance))

    def solve(self) -> None:
        if self.n == 1:
            print(0)
            return

        distances, target = self.dijkstra(1), (0, 0)
        for idx, distance in enumerate(distances):
            if distance > target[0]:
                target = (distance, idx + 1)

        print(max(self.dijkstra(target[1])))

    def dijkstra(self, start_vertex: int) -> list[int]:
        queue, distances = [(0, start_vertex)], [0 if idx == start_vertex else math.inf for idx in range(self.n + 1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue

            for next_vertex, distance in self.graph[current_vertex]:
                next_distance = current_distance + distance
                if next_distance < distances[next_vertex]:
                    distances[next_vertex] = next_distance
                    heapq.heappush(queue, (next_distance, next_vertex))

        return list(map(int, distances[1:]))


if __name__ == "__main__":
    Problem().solve()
