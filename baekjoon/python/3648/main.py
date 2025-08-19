import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [tuple(map(int, read().split())) for _ in range(self.m)]

    def solve(self) -> None:
        print("yes" if self.is_satisfiable() else "no")

    def is_satisfiable(self) -> bool:
        graph, reversed_graph = self.build_graph()
        order = self.get_topological_order(graph)
        scc_id = self.get_scc(reversed_graph, order)

        for idx in range(self.n):
            if scc_id[2 * idx] == scc_id[2 * idx + 1]:
                return False

        return True

    def build_graph(self) -> tuple[list[list[int]], list[list[int]]]:
        graph = [[] for _ in range(2 * self.n)]
        reversed_graph = [[] for _ in range(2 * self.n)]

        node_1_neg = self.literal_to_node(-1)
        node_1_pos = self.literal_to_node(1)
        graph[node_1_neg].append(node_1_pos)
        reversed_graph[node_1_pos].append(node_1_neg)

        for a, b in self.data:
            node_a_neg = self.literal_to_node(-a)
            node_b_neg = self.literal_to_node(-b)
            node_a_pos = self.literal_to_node(a)
            node_b_pos = self.literal_to_node(b)

            graph[node_a_neg].append(node_b_pos)
            graph[node_b_neg].append(node_a_pos)
            reversed_graph[node_b_pos].append(node_a_neg)
            reversed_graph[node_a_pos].append(node_b_neg)

        return graph, reversed_graph

    def literal_to_node(self, literal: int) -> int:
        if literal > 0:
            return (abs(literal) - 1) * 2

        return (abs(literal) - 1) * 2 + 1

    def get_topological_order(self, graph: list[list[int]]) -> list[int]:
        order, visited = [], set()
        for idx in range(self.n * 2):
            if idx in visited:
                continue

            stack = deque([(idx, 0)])
            visited.add(idx)
            while stack:
                node, neighbor_index = stack[-1]
                if neighbor_index < len(graph[node]):
                    neighbor = graph[node][neighbor_index]
                    stack[-1] = (node, neighbor_index + 1)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, 0))
                else:
                    order.append(node)
                    stack.pop()
        return order

    def get_scc(self, reversed_graph: list[list[int]], order: list[int]) -> list[int]:
        scc_id, scc_count = [-1] * (self.n * 2), 0

        for node in reversed(order):
            if scc_id[node] != -1:
                continue

            stack, scc_id[node] = [node], scc_count
            while stack:
                current_node = stack.pop()
                for neighbor in reversed_graph[current_node]:
                    if scc_id[neighbor] == -1:
                        scc_id[neighbor] = scc_count
                        stack.append(neighbor)

            scc_count += 1

        return scc_id


if __name__ == "__main__":
    while True:
        try:
            Problem().solve()
        except (EOFError, ValueError):
            break
