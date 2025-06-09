import itertools

from collections import deque
from typing import List


def solution(maps: List[str]) -> List[int]:
    n, m = len(maps), len(maps[0])
    areas, visited = [], set()

    for x, y in itertools.product(range(m), range(n)):
        if maps[y][x] == "X" or (x, y) in visited:
            continue

        queue, area = deque([(x, y)]), 0

        while queue:
            px, py = queue.popleft()
            if (px, py) in visited:
                continue

            visited.add((px, py))
            area += int(maps[py][px])

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = px + dx, py + dy
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != "X":
                    queue.append((nx, ny))

        areas.append(area)

    return [-1] if not areas else sorted(areas)
