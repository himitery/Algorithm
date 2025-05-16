import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.v, self.e = map(int, read().split())
        self.graph, self.r_graph = defaultdict(set), defaultdict(set)

        for src, dest in [map(int, read().split()) for _ in range(self.e)]:
            self.graph[src].add(dest)
            self.r_graph[dest].add(src)

    def solve(self) -> None:
        order, visited = deque(), set()
        for node in range(1, self.v + 1):
            if node not in visited:
                self.dfs_postorder(node, visited, order)

        components, visited = [], set()
        while order:
            node = order.pop()
            if node not in visited:
                components.append(self.dfs_collect_scc(node, visited))

        print(len(components))
        for row in sorted(components, key=lambda x: x[0]):
            print(*row, -1)

    def dfs_postorder(self, start: int, visited: set[int], order: deque[int]):
        stack = deque([start])

        while stack:
            node = stack.pop()
            if node > 0 and node in visited:
                continue

            if node < 0:
                order.append(~node)
                continue

            visited.add(node)
            stack.append(~node)

            for next_node in self.graph[node] - visited:
                stack.append(next_node)

    def dfs_collect_scc(self, start: int, visited: set[int]) -> list[int]:
        stack, component = deque([start]), []

        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            component.append(node)

            for next_node in self.r_graph[node] - visited:
                stack.append(next_node)

        return sorted(component)


if __name__ == "__main__":
    Problem().solve()
