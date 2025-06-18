from collections import Counter
from typing import List


def solution(participant: List[str], completion: List[str]) -> str:
    counter = Counter(participant)

    for name in completion:
        counter[name] -= 1

    return counter.most_common()[0][0]
