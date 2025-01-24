import heapq
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = defaultdict(list)

        for _ in range(self.m):
            src, dest, cost = map(int, read().split())
            self.data[src].append((cost, dest))
            self.data[dest].append((cost, src))

    def solve(self) -> None:
        print(self.mst(1))

    def mst(self, start_node: int) -> int:
        queue, visited, costs, max_cost = ([(0, start_node)], set(), 0, 0)

        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue

            visited.add(node)
            costs, max_cost = costs + cost, max(max_cost, cost)

            for new_cost, dest in self.data[node]:
                if dest not in visited:
                    heapq.heappush(queue, (new_cost, dest))

        return costs - max_cost


if __name__ == "__main__":
    Problem().solve()
