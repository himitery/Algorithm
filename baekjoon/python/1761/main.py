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
            self.nodes[src].add((dest, distance))
            self.nodes[dest].add((src, distance))

        self.queries = [cast(tuple[int, int], tuple(map(int, read().split()))) for _ in range(int(read()))]

        self.depth, self.parent, self.weights = self.make_tree()

    def solve(self) -> None:
        for x, y in self.queries:
            print(self.weights[x] + self.weights[y] - 2 * self.weights[self.lca(x, y)])

    def make_tree(self) -> tuple[list[int], list[list[int]], list[int]]:
        queue, visited = deque([(1, 0)]), {1}
        depth, parent, weights = (
            [0 for _ in range(self.n + 1)],
            [[0 for _ in range(20)] for _ in range(self.n + 1)],
            [0 for _ in range(self.n + 1)],
        )

        while queue:
            node, idx = queue.popleft()
            depth[node] = idx

            for child, distance in self.nodes[node]:
                if child not in visited:
                    queue.append((child, idx + 1))
                    visited.add(child)
                    parent[child][0] = node
                    weights[child] = weights[node] + distance

        for k in range(1, 20):
            for node in range(1, self.n + 1):
                parent[node][k] = parent[parent[node][k - 1]][k - 1]

        return depth, parent, weights

    def lca(self, x: int, y: int) -> int:
        if self.depth[x] < self.depth[y]:
            x, y = y, x

        for k in range(20)[::-1]:
            if self.depth[x] - (1 << k) >= self.depth[y]:
                x = self.parent[x][k]

        if x == y:
            return x

        for k in range(20)[::-1]:
            if self.parent[x][k] != self.parent[y][k]:
                x, y = self.parent[x][k], self.parent[y][k]

        return self.parent[x][0]


if __name__ == "__main__":
    Problem().solve()
