import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.v = int(read())
        self.data = defaultdict(list[tuple[int, int]])

        for line in [list(map(int, read().split())) for _ in range(self.v)]:
            for idx in range(1, len(line) - 1, 2):
                self.data[line[0]].append((line[idx], line[idx + 1]))

    def solve(self) -> None:
        node, maximum = self.dfs(1)

        print(max(maximum, self.dfs(node)[1]))

    def dfs(self, start_node: int) -> tuple[int, int]:
        queue, visited, maximum, node = deque([(start_node, 0)]), {start_node}, 0, start_node

        while queue:
            current, weight = queue.pop()
            if weight > maximum:
                maximum, node = weight, current

            for next_node, next_weight in self.data[current]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, weight + next_weight))

        return node, maximum


if __name__ == "__main__":
    Problem().solve()
