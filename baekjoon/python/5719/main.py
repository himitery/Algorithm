import heapq
import math
import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.s, self.d = map(int, read().split())

        self.graph = defaultdict(list[tuple[int, int]])
        for _ in range(self.m):
            u, v, p = map(int, read().split())
            self.graph[u].append((v, p))

    def solve(self) -> None:
        result = self.dijkstra(self.s, self.remove_edges(self.dijkstra(self.s)))[self.d]
        print(result if result != math.inf else -1)

    def dijkstra(self, start_node: int, removed: list[set[int]] = None):
        heap, dist, prev = (
            [(0, start_node)],
            [0 if x == start_node else math.inf for x in range(self.n)],
            [[] for _ in range(self.n)],
        )

        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue

            for next_node, weight in self.graph[node]:
                if removed and next_node in removed[node]:
                    continue

                if cost + weight < dist[next_node]:
                    dist[next_node] = cost + weight
                    prev[next_node] = [node]
                    heapq.heappush(heap, (cost + weight, next_node))
                elif removed is None and cost + weight == dist[next_node]:
                    prev[next_node].append(node)

        return prev if removed is None else dist

    def remove_edges(self, prev: list[list[int]]) -> list[set[int]]:
        queue, removed, visited = deque([self.d]), [set() for _ in range(self.n)], {self.d}

        while queue:
            node = queue.popleft()

            for prev_node in prev[node]:
                removed[prev_node].add(node)
                if prev_node not in visited:
                    visited.add(prev_node)
                    queue.append(prev_node)

        return removed


if __name__ == "__main__":
    while True:
        try:
            Problem().solve()
        except (EOFError, ValueError):
            break
