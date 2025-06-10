import itertools

from typing import List, Tuple
from collections import deque

def solution(maps: List[str]) -> int:
    n, m = len(maps), len(maps[0])
    start = [
        (x, y)
        for x, y in itertools.product(range(m), range(n))
        if maps[y][x] == 'S'
    ][0]

    lever, lever_step = find_path(maps, start, "L")
    if lever_step == -1:
        return -1

    end_step = find_path(maps, lever, "E")[1]
    if end_step == -1:
        return -1

    return lever_step + end_step


def find_path(maps: List[str], start: Tuple[int, int], target: str) -> Tuple[Tuple[int, int], int]:
    n, m = len(maps), len(maps[0])
    queue, visited = deque([(0, start)]), set()

    while queue:
        step, (x, y) = queue.popleft()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if maps[ny][nx] == target:
                return (nx, ny), step + 1

            if maps[ny][nx] != 'X':
                queue.append((step + 1, (nx, ny)))

    return (-1, -1), -1
