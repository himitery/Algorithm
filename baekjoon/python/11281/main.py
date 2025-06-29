import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self) -> None:
        self.n, self.m = map(int, read().split())

        self.graph = defaultdict(list)
        for x, y in [map(int, read().split()) for _ in range(self.m)]:
            self.graph[self.literal_to_node(-x)].append(self.literal_to_node(y))
            self.graph[self.literal_to_node(-y)].append(self.literal_to_node(x))

    def literal_to_node(self, literal: int) -> int:
        if literal > 0:
            return literal

        return -literal + self.n

    def solve(self) -> None:
        discovered, low, scc_id, on_stack, scc_stack, order, scc_counter = (
            [-1] * (2 * self.n + 1),
            [-1] * (2 * self.n + 1),
            [-1] * (2 * self.n + 1),
            [False] * (2 * self.n + 1),
            deque(),
            0,
            0,
        )

        for node in range(1, 2 * self.n + 1):
            if discovered[node] == -1:
                order, scc_counter = self.tarjan_scc(
                    node,
                    discovered,
                    low,
                    scc_id,
                    on_stack,
                    scc_stack,
                    order,
                    scc_counter,
                )

        for idx in range(1, self.n + 1):
            if scc_id[idx] == scc_id[idx + self.n]:
                print(0)
                return

        print(1)
        print(*[0 if scc_id[idx] > scc_id[idx + self.n] else 1 for idx in range(1, self.n + 1)])

    def tarjan_scc(
        self,
        start_node: int,
        discovered: list[int],
        low: list[int],
        scc_id: list[int],
        on_stack: list[bool],
        scc_stack: deque,
        order: int,
        scc_counter: int,
    ) -> tuple[int, int]:
        stack = deque([(start_node, iter(self.graph[start_node]))])

        while stack:
            current_node, neighbors = stack[-1]

            if discovered[current_node] == -1:
                order += 1
                discovered[current_node] = low[current_node] = order
                scc_stack.append(current_node)
                on_stack[current_node] = True

            for neighbor in neighbors:
                if discovered[neighbor] == -1:
                    stack.append((neighbor, iter(self.graph[neighbor])))
                    break
                elif on_stack[neighbor]:
                    low[current_node] = min(low[current_node], discovered[neighbor])
            else:
                popped_node, _ = stack.pop()

                if low[popped_node] == discovered[popped_node]:
                    scc_counter += 1
                    while True:
                        node_in_scc = scc_stack.pop()
                        on_stack[node_in_scc] = False
                        scc_id[node_in_scc] = scc_counter
                        if node_in_scc == popped_node:
                            break

                if stack:
                    parent_node, _ = stack[-1]
                    low[parent_node] = min(low[parent_node], low[popped_node])

        return order, scc_counter


if __name__ == "__main__":
    Problem().solve()
