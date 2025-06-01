import itertools
import sys
from collections import defaultdict, deque
from typing import cast

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

        self.nodes = defaultdict(set[tuple[int, int]])
        for _ in range(self.n - 1):
            src, dest, distance = map(int, read().split())
            self.nodes[src - 1].add((dest - 1, distance))
            self.nodes[dest - 1].add((src - 1, distance))

        self.k = int(read())
        self.queries = [cast(tuple[int, int], tuple(map(lambda x: int(x) - 1, read().split()))) for _ in range(self.k)]

        self.depth, self.parent, self.weights = self.make_tree()

    def solve(self) -> None:
        for x, y in self.queries:
            print(*self.lca(x, y))

    def make_tree(self) -> tuple[list[int], list[list[int]], list[list[tuple[int, int]]]]:
        queue, visited = deque([(0, 0)]), {0}
        depth, parent, weights = (
            [0 for _ in range(self.n)],
            [[0 for _ in range(20)] for _ in range(self.n)],
            [[(1_000_000, 0) for _ in range(20)] for _ in range(self.n)],
        )

        while queue:
            idx, node = queue.popleft()
            depth[node] = idx

            for next_node, distance in self.nodes[node]:
                if next_node not in visited:
                    queue.append((idx + 1, next_node))
                    visited.add(next_node)
                    parent[next_node][0] = node
                    weights[next_node][0] = (distance, distance)

        for k, node in itertools.product(range(1, 20), range(self.n)):
            ancestor = parent[node][k - 1]
            parent[node][k] = parent[ancestor][k - 1]
            weights[node][k] = (
                min(weights[node][k - 1][0], weights[ancestor][k - 1][0]),
                max(weights[node][k - 1][1], weights[ancestor][k - 1][1]),
            )

        return depth, parent, weights

    def lca(self, x: int, y: int) -> tuple[int, int]:
        minimum, maximum = 1_000_000, 0
        if self.depth[x] < self.depth[y]:
            x, y = y, x

        for k in range(19, -1, -1):
            if self.depth[x] - (1 << k) >= self.depth[y]:
                minimum, maximum = min(minimum, self.weights[x][k][0]), max(maximum, self.weights[x][k][1])
                x = self.parent[x][k]

        if x == y:
            return minimum, maximum

        for k in range(19, -1, -1):
            if self.parent[x][k] != self.parent[y][k]:
                minimum, maximum = (
                    min(minimum, self.weights[x][k][0], self.weights[y][k][0]),
                    max(maximum, self.weights[x][k][1], self.weights[y][k][1]),
                )
                x, y = self.parent[x][k], self.parent[y][k]

        return (
            min(minimum, self.weights[x][0][0], self.weights[y][0][0]),
            max(maximum, self.weights[x][0][1], self.weights[y][0][1]),
        )


if __name__ == "__main__":
    Problem().solve()
