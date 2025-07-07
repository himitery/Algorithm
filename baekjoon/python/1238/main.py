import heapq
import math
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.x = map(int, read().split())
        self.graph = defaultdict(list)

        for start, end, weight in [map(int, read().split()) for _ in range(self.m)]:
            self.graph[start - 1].append((end - 1, weight))

    def solve(self) -> None:
        dist = self.dijkstra(self.x - 1)

        print(
            max([self.dijkstra(person)[self.x - 1] + dist[person] for person in range(self.n) if person != self.x - 1])
        )

    def dijkstra(self, start_node: int) -> list[int]:
        heap, distance = [(0, start_node)], [math.inf] * self.n

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distance[current_node]:
                continue

            for next_node, next_distance in self.graph[current_node]:
                if current_distance + next_distance < distance[next_node]:
                    distance[next_node] = current_distance + next_distance
                    heapq.heappush(heap, (current_distance + next_distance, next_node))

        return list(map(int, distance))


if __name__ == "__main__":
    Problem().solve()
