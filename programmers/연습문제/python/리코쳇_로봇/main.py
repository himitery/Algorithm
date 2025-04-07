from collections import deque
from typing import List, Tuple


def solution(board: List[str]) -> int:
    matrix = [list(row) for row in board]
    n, m = len(matrix), len(matrix[0])

    red, green = find_points(matrix)
    queue, visited = deque([(0, red)]), set()

    while queue:
        step, (x, y) = queue.popleft()
        if (x, y) == green:
            return step

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x, y
            while 0 <= nx + dx < m and 0 <= ny + dy < n and matrix[ny + dy][nx + dx] != "D":
                nx, ny = nx + dx, ny + dy

            if (x, y) != (nx, ny):
                queue.append((step + 1, (nx, ny)))

    return -1


def find_points(matrix: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    red, green = (-1, -1), (-1, -1)

    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == "R":
                red = (x, y)
            if value == "G":
                green = (x, y)

    return red, green
