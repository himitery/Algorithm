from typing import List


def solution(numbers: List[int]) -> List[int]:
    n = len(numbers)
    stack, results = [], [-1] * n

    for idx in range(n - 1, -1, -1):
        while stack and stack[-1] <= numbers[idx]:
            stack.pop()

        if stack:
            results[idx] = stack[-1]

        stack.append(numbers[idx])

    return results
