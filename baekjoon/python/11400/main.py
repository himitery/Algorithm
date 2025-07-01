import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self) -> None:
        self.v, self.e = map(int, read().split())

        self.graph = defaultdict(list[int])
        for x, y in [map(int, read().split()) for _ in range(self.e)]:
            self.graph[x].append(y)
            self.graph[y].append(x)

    def solve(self) -> None:
        discovered, low, bridges, order = (
            [-1] * (self.v + 1),
            [-1] * (self.v + 1),
            [],
            0,
        )

        for node in range(1, self.v + 1):
            if discovered[node] == -1:
                order = self.find_bridges(node, discovered, low, bridges, order)

        print(len(bridges))
        for bridge in sorted(bridges):
            print(*bridge)

    def find_bridges(
        self,
        start_node: int,
        discovered: list[int],
        low: list[int],
        bridges: list[list[int]],
        order: int,
    ) -> int:
        stack = deque([(start_node, 0, iter(self.graph[start_node]))])

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
                    stack.append((neighbor, current_node, iter(self.graph[neighbor])))
                    break
            else:
                popped_node, parent_node, _ = stack.pop()

                if parent_node != 0:
                    low[parent_node] = min(low[parent_node], low[popped_node])
                    if low[popped_node] > discovered[parent_node]:
                        bridges.append(sorted([parent_node, popped_node]))

        return order


if __name__ == "__main__":
    Problem().solve()
