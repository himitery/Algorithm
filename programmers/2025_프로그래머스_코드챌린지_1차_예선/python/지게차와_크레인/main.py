import itertools
from collections import deque
from typing import List, Tuple, Set


def solution(storage: List[str], requests: List[str]):
    rows, cols = len(storage), len(storage[0])

    sides, visited = init_sides(rows, cols), set()

    for request in requests:
        selected = {
            (x, y)
            for x, y in (sides if len(request) == 1 else set(itertools.product(range(cols), range(rows)))) - visited
            if storage[y][x] == request[0]
        }
        visited |= selected
        sides |= find_nested_sides(rows, cols, selected if len(request) == 0 else selected & sides, sides, visited)

    return rows * cols - len(visited)


def init_sides(rows: int, cols: int) -> Set[Tuple[int, int]]:
    return (
        {(x, 0) for x in range(cols)}
        | {(x, rows - 1) for x in range(cols)}
        | {(0, y) for y in range(rows)}
        | {(cols - 1, y) for y in range(rows)}
    )


def find_nested_sides(
    rows: int,
    cols: int,
    selected: Set[Tuple[int, int]],
    sides: Set[Tuple[int, int]],
    visited: Set[Tuple[int, int]],
) -> Set[Tuple[int, int]]:
    stack, nested = deque(list(selected)), set()

    while stack:
        x, y = stack.pop()

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if 0 <= x + dx < cols and 0 <= y + dy < rows and (x + dx, y + dy) not in sides | nested:
                nested.add((x + dx, y + dy))
                if (x + dx, y + dy) in visited:
                    stack.append((x + dx, y + dy))

    return nested
