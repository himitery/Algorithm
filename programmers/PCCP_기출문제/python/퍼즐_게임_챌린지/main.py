from typing import List


def solution(diffs: List[int], times: List[int], limit: int) -> int:
    result, left, right = 0, 1, max(diffs)

    while left <= right:
        level = (left + right) // 2
        if level == result:
            break

        total = 0
        for idx, diff in enumerate(diffs):
            total += times[idx] + ((times[idx - 1] + times[idx]) * (diff - level) if level < diff else 0)
            if total > limit:
                break

        if total <= limit:
            result, right = level, level
        else:
            left = level + 1

    return max(1, result)
