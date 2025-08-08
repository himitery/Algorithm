import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.src, self.dest = map(int, read().split())

    def solve(self) -> None:
        print(self.bfs())

    def bfs(self) -> int:
        queue, visited = deque([(self.src, 1)]), {self.src}

        while queue:
            current, depth = queue.popleft()
            if current == self.dest:
                return depth

            for next_node in [current * 2, current * 10 + 1]:
                if next_node <= self.dest and next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, depth + 1))

        return -1


if __name__ == "__main__":
    Problem().solve()
