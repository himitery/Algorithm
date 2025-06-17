import itertools

from typing import List, Tuple


def solution(board: List[str]) -> int:
    o, x = [], []
    for c, r in itertools.product(range(3), range(3)):
        if board[r][c] == "O":
            o.append((c, r))
        if board[r][c] == "X":
            x.append((c, r))

    o_complete, x_complete = complete(o), complete(x)
    return 1 - int(
        not (0 <= len(o) - len(x) <= 1)
        or (o_complete > 0 and x_complete > 0)
        or (o_complete and len(o) <= len(x))
        or (x_complete and len(o) > len(x))
    )


def complete(coords: List[Tuple[int, int]]) -> int:
    count, find_sign = 0, lambda num: 0 if num == 0 else (2 * int(num == abs(num)) - 1)

    for x, y, z in itertools.combinations(coords, 3):
        if find_sign(x[0] - y[0]) == find_sign(y[0] - z[0]) and find_sign(x[1] - y[1]) == find_sign(y[1] - z[1]):
            count += 1

    return count
