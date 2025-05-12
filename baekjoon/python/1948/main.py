import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = int(read()), int(read())
        self.graph, self.reverse_graph, self.in_degree = (
            defaultdict(list[tuple[int, int]]),
            defaultdict(list[tuple[int, int]]),
            [0 for _ in range(self.n)],
        )

        for src, dest, time in [map(int, read().split()) for _ in range(self.m)]:
            self.graph[src - 1].append((dest - 1, time))
            self.reverse_graph[dest - 1].append((src - 1, time))
            self.in_degree[dest - 1] += 1

        self.src, self.dest = map(lambda x: int(x) - 1, read().split())

    def solve(self) -> None:
        costs = self.topological_sort()

        print(costs[self.dest])
        print(self.count_critical_paths(costs))

    def topological_sort(self) -> list[int]:
        queue, costs = deque([self.src]), [0 for _ in range(self.n)]

        while queue:
            node = queue.popleft()

            for next_node, next_time in self.graph[node]:
                if costs[next_node] < costs[node] + next_time:
                    costs[next_node] = costs[node] + next_time

                self.in_degree[next_node] -= 1
                if self.in_degree[next_node] == 0:
                    queue.append(next_node)

        return costs

    def count_critical_paths(self, costs: list[int]) -> int:
        queue, visited, count = deque([self.dest]), {self.dest}, 0

        while queue:
            node = queue.popleft()

            for prev, cost in self.reverse_graph[node]:
                if costs[prev] + cost != costs[node]:
                    continue

                count += 1
                if prev not in visited:
                    visited.add(prev)
                    queue.append(prev)

        return count


if __name__ == "__main__":
    Problem().solve()
