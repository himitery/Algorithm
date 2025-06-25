import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.v, self.e = map(int, read().split())

        self.graph = defaultdict(list[int])
        for x, y in [map(int, read().split()) for _ in range(self.e)]:
            self.graph[x].append(y)
            self.graph[y].append(x)

    def solve(self) -> None:
        discovered, low, points, order = (
            [-1] * (self.v + 1),
            [-1] * (self.v + 1),
            set(),
            0,
        )

        for node in range(1, self.v + 1):
            if discovered[node] == -1:
                order = self.dfs(node, discovered, low, points, order)

        print(len(points))
        print(*sorted(list(points)))

    def dfs(
        self,
        start_node: int,
        discovered: list[int],
        low: list[int],
        points: set[int],
        order: int,
    ) -> int:
        stack, root_children_count = deque([(start_node, 0, iter(self.graph[start_node]))]), 0

        while stack:
            current_node, parent, neighbors = stack[-1]

            if discovered[current_node] == -1:
                order += 1
                discovered[current_node] = low[current_node] = order

            for neighbor in neighbors:
                if neighbor == parent:
                    continue

                if discovered[neighbor] != -1:
                    low[current_node] = min(low[current_node], discovered[neighbor])
                else:
                    if parent == 0:
                        root_children_count += 1
                    stack.append((neighbor, current_node, iter(self.graph[neighbor])))
                    break
            else:
                stack.pop()
                if parent != 0:
                    low[parent] = min(low[parent], low[current_node])

                    if parent != start_node and low[current_node] >= discovered[parent]:
                        points.add(parent)

        if root_children_count > 1:
            points.add(start_node)

        return order


if __name__ == "__main__":
    Problem().solve()
