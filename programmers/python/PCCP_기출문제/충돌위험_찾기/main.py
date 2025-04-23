from collections import Counter
from typing import List


def solution(points: List[List[int]], routes: List[List[int]]) -> int:
    points = [(y - 1, x - 1) for y, x in points]
    queue, count = [(0, points[route[0] - 1], [r - 1 for r in route]) for route in routes], 0

    while queue:
        new_queue, counter = [], Counter([point for idx, point, path in queue])
        count += len([key for key, count in counter.items() if count > 1])

        for idx, (y, x), path in queue:
            if (y, x) == points[path[idx]]:
                idx += 1

            if idx == len(path):
                continue

            target_y, target_x = points[path[idx]]
            if y != target_y:
                dy = 1 if y < target_y else -1
                new_queue.append((idx, (y + dy, x), path))
            else:
                dx = 1 if x < target_x else -1
                new_queue.append((idx, (y, x + dx), path))

        queue = new_queue

    return count
