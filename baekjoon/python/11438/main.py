import itertools
import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

        self.nodes = defaultdict(list[int])
        for src, dest in [map(lambda x: int(x) - 1, read().split()) for _ in range(self.n - 1)]:
            self.nodes[src].append(dest)
            self.nodes[dest].append(src)

        self.queries = [map(lambda x: int(x) - 1, read().split()) for _ in range(int(read()))]
        self.depth, self.parent = self.make_tree()

    def solve(self) -> None:
        for x, y in self.queries:
            print(self.lca(x, y) + 1)

    def make_tree(self):
        stack, visited = deque([(0, 0)]), {0}
        depth, parent = [0 for _ in range(self.n)], [[0 for _ in range(17)] for _ in range(self.n)]

        while stack:
            idx, node = stack.pop()
            depth[node] = idx

            for next_node in self.nodes[node]:
                if next_node not in visited:
                    stack.append((idx + 1, next_node))
                    visited.add(next_node)
                    parent[next_node][0] = node

        for k, node in itertools.product(range(1, 17), range(self.n)):
            parent[node][k] = parent[parent[node][k - 1]][k - 1]

        return depth, parent

    def lca(self, x: int, y: int) -> int:
        if self.depth[x] < self.depth[y]:
            x, y = y, x

        for k in range(16, -1, -1):
            if self.depth[x] - (1 << k) >= self.depth[y]:
                x = self.parent[x][k]

        if x == y:
            return x

        for k in range(16, -1, -1):
            if self.parent[x][k] != self.parent[y][k]:
                x, y = self.parent[x][k], self.parent[y][k]

        return self.parent[x][0]


if __name__ == "__main__":
    Problem().solve()
