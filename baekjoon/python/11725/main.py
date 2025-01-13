import sys

from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.number_of_nodes = int(read())
        self.paris = defaultdict(set[int])

        for _ in range(self.number_of_nodes - 1):
            x, y = map(int, read().split())

            self.paris[x].add(y)
            self.paris[y].add(x)

    def solve(self) -> None:
        self.heads = [0] * (self.number_of_nodes + 1)

        queue, visited = deque([1]), {1}
        while queue:
            node = queue.popleft()
            for next_node in self.paris[node]:
                if next_node not in visited:
                    self.heads[next_node] = node
                    queue.append(next_node)
                    visited.add(next_node)

        for head in self.heads[2:]:
            print(head)


if __name__ == "__main__":
    Problem().solve()
