import math
from typing import List


def solution(m: int, n: int, start_x: int, start_y: int, balls: List[List[int]]) -> List[int]:
    return [
        min(
            map(
                lambda x: math.inf if x is None else (start_x - x[0]) ** 2 + (start_y - x[1]) ** 2,
                [
                    None if (start_y == target_y and start_x > target_x) else (-target_x, target_y),
                    None if (start_y == target_y and start_x < target_x) else (2 * m - target_x, target_y),
                    None if (start_x == target_x and start_y > target_y) else (target_x, -target_y),
                    None if (start_x == target_x and start_y < target_y) else (target_x, 2 * n - target_y),
                ],
            )
        )
        for target_x, target_y in balls
    ]
