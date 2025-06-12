from collections import Counter
from typing import List


def solution(weights: List[int]) -> int:
    counter, answer = Counter(weights), 0

    for weight in sorted(counter.keys()):
        count = counter[weight]
        answer += count * (count - 1) // 2

        for ratio in [3 / 2, 4 / 3, 2]:
            if (target := float(weight * ratio)) and target.is_integer() and target in counter:
                answer += count * counter[int(target)]

    return answer
