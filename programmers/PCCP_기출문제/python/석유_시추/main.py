from collections import deque
from typing import List, Tuple


def solution(land: List[List[int]]) -> int:
    n, m = len(land), len(land[0])
    graph = find_graph(n, m, land)

    maximum = 0
    for col in range(m):
        amount, visited = 0, set()

        for row in range(n):
            group_id, value = graph[row][col]
            if group_id != 0 and group_id not in visited:
                visited.add(group_id)
                amount += value

        maximum = max(maximum, amount)

    return maximum


def find_graph(n: int, m: int, land: List[List[int]]) -> List[List[Tuple[int, int]]]:
    graph, visited, count = [[(0, 0) for _ in range(m)] for _ in range(n)], set(), 0

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and (x, y) not in visited:
                stack, cached, count = deque([(x, y)]), set(), count + 1

                while stack:
                    c, r = stack.pop()
                    visited.add((c, r))
                    cached.add((c, r))

                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        nx, ny = c + dx, r + dy
                        if (0 <= nx < m) and (0 <= ny < n) and land[ny][nx] == 1 and (nx, ny) not in visited:
                            stack.append((nx, ny))

                group_id, amount = count, len(cached)
                for c, r in cached:
                    graph[r][c] = (group_id, amount)

    return graph
