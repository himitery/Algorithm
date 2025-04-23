import itertools
from collections import deque
from typing import List


def solution(n: int, q: List[List[int]], ans: List[int]) -> int:
    questions = [set(question) for question in q]
    stack, count = deque([(0, set(), set())]), 0

    while stack:
        idx, secrets, ignored = stack.pop()
        if len(secrets) > 5:
            continue

        if idx == len(questions):
            if n - len(ignored) >= 5:
                count += len(
                    list(
                        itertools.combinations(
                            {x + 1 for x in range(n)} - (secrets | ignored),
                            5 - len(secrets),
                        )
                    )
                )
            continue

        matched, available = questions[idx] & secrets, questions[idx] - (secrets | ignored)
        if len(matched) == ans[idx]:
            stack.append((idx + 1, secrets, ignored | available))
            continue
        if len(matched) > ans[idx] or len(available) < ans[idx] - len(matched):
            continue

        for new_secret in itertools.combinations(available, ans[idx] - len(matched)):
            stack.append(
                (
                    idx + 1,
                    secrets | set(new_secret),
                    ignored | (available - set(new_secret)),
                )
            )

    return count
