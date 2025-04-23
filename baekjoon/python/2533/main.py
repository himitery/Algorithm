import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.graph = defaultdict(set)

        for _ in range(self.n - 1):
            u, v = map(lambda x: int(x) - 1, read().split())
            self.graph[u].add(v)
            self.graph[v].add(u)

    def solve(self) -> None:
        dp, post_order = [[0, 1] for _ in range(self.n)], self.find_post_order()

        for node, parent in reversed(post_order):
            for child in self.graph[node] - {parent}:
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child])

        print(min(dp[0]))

    def find_post_order(self) -> list[tuple[int, int]]:
        stack, post_order = deque([(0, -1)]), []

        while stack:
            node, parent = stack.pop()
            post_order.append((node, parent))

            for child in self.graph[node] - {parent}:
                stack.append((child, node))

        return post_order


if __name__ == "__main__":
    Problem().solve()
