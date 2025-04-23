from collections import deque
from typing import List


def solution(maze: List[List[int]]) -> int:
    n, m = len(maze), len(maze[0])

    red, blue = None, None
    for y in range(n):
        for x in range(m):
            if maze[y][x] == 1:
                red = (x, y)
            elif maze[y][x] == 2:
                blue = (x, y)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue, visited = deque([(0, red, blue, frozenset({red}), frozenset({blue}))]), {
        red,
        blue,
        frozenset({red}),
        frozenset({blue}),
    }

    while queue:
        count, (rx, ry), (bx, by), rv, bv = queue.popleft()
        if maze[ry][rx] == 3 and maze[by][bx] == 4:
            return count

        red_moves = (
            [(rx, ry)]
            if maze[ry][rx] == 3
            else [
                (rx + dx, ry + dy)
                for dx, dy in directions
                if (0 <= rx + dx < m and 0 <= ry + dy < n)
                and maze[ry + dy][rx + dx] != 5
                and (rx + dx, ry + dy) not in rv
            ]
        )

        blue_moves = (
            [(bx, by)]
            if maze[by][bx] == 4
            else [
                (bx + dx, by + dy)
                for dx, dy in directions
                if (0 <= bx + dx < m and 0 <= by + dy < n)
                and maze[by + dy][bx + dx] != 5
                and (bx + dx, by + dy) not in bv
            ]
        )

        if not red_moves or not blue_moves:
            continue

        for nr in red_moves:
            for nb in blue_moves:
                if nr == nb or (nr == (bx, by) and nb == (rx, ry)):
                    continue

                nrv, nbv = rv | frozenset({nr}), bv | frozenset({nb})
                if (nr, nb, nrv, nbv) not in visited:
                    visited.add((nr, nb, nr, nb, nrv, nbv))
                    queue.append((count + 1, nr, nb, nrv, nbv))

    return 0
