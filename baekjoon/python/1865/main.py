import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.w = map(int, read().split())
        self.graph, self.visited = [], set()

        for _ in range(self.m):
            src, dest, time = map(int, read().split())
            self.graph.append((src - 1, dest - 1, time))
            self.graph.append((dest - 1, src - 1, time))

        for _ in range(self.w):
            src, dest, time = map(int, read().split())
            self.graph.append((src - 1, dest - 1, -time))

    def solve(self) -> None:
        for node in range(self.n):
            if node not in self.visited and self.bellman_ford(node):
                print("YES")
                return

        print("NO")

    def bellman_ford(self, node: int) -> bool:
        distances = [0 if node == idx else math.inf for idx in range(self.n)]

        for idx in range(self.n):
            updated = False
            for src, dest, time in self.graph:
                if distances[src] != math.inf and distances[dest] > distances[src] + time:
                    distances[dest] = distances[src] + time
                    self.visited |= {src, dest}
                    updated = True

                    if idx == self.n - 1:
                        return True

            if not updated:
                return False

        return False


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
