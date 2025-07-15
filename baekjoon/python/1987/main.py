import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.r, self.c = map(int, read().split())
        self.matrix = [list(read()) for _ in range(self.r)]

    def solve(self) -> None:
        print(self.dfs())

    def dfs(self) -> int:
        stack, cache, max_depth = (
            deque([((0, 0), 1, 1 << ord(self.matrix[0][0]) - ord("A"))]),
            {row: {col: set() for col in range(self.c)} for row in range(self.r)},
            1,
        )
        cache[0][0].add(1 << ord(self.matrix[0][0]) - ord("A"))

        while stack:
            (x, y), depth, visited = stack.pop()
            if depth > max_depth:
                max_depth = depth

            if max_depth == min(self.r * self.c, 26):
                return max_depth

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.c and 0 <= ny < self.r:
                    next_token_code = ord(self.matrix[ny][nx]) - ord("A")

                    if visited & (1 << next_token_code) == 0:
                        mask = visited | (1 << next_token_code)

                        if mask not in cache[ny][nx]:
                            cache[ny][nx].add(mask)
                            stack.append(((nx, ny), depth + 1, mask))

        return max_depth


if __name__ == "__main__":
    Problem().solve()
