import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.r, self.q = map(int, read().split())

        self.edges = defaultdict(list)
        for _ in range(self.n - 1):
            x, y = map(int, read().split())
            self.edges[x].append(y)
            self.edges[y].append(x)

        self.queries = [int(read()) for _ in range(self.q)]

    def solve(self) -> None:
        children = self.find_children(self.r)

        for query in self.queries:
            print(children[query])

    def find_children(self, num: int) -> list[int]:
        stack, cached = deque([(num, -1)]), []

        while stack:
            node, head = stack.pop()
            cached.append((node, head))

            for child in self.edges[node]:
                if child != head:
                    stack.append((child, node))

        children = [1] * (self.n + 1)
        for node, head in reversed(cached):
            if head != -1:
                children[head] += children[node]

        return children


if __name__ == "__main__":
    Problem().solve()
