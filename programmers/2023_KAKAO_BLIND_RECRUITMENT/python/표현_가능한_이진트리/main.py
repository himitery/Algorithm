import math
from collections import deque
from typing import List


def solution(numbers: List[int]) -> List[int]:
    return [int(is_binary(num)) for num in numbers]


def is_binary(num: int) -> bool:
    binary = to_binary(num)
    queue, count = deque([(1, len(binary))]), 0

    while queue:
        left, right = queue.popleft()
        mid = (left + right) // 2

        if binary[mid - 1] == 0:
            continue

        count += 1
        if left < mid:
            queue.append((left, mid - 1))
        if mid < right:
            queue.append((mid + 1, right))

    return count == binary.count(1)


def to_binary(num: int) -> List[int]:
    binary = []
    while num:
        binary.append(num & 1)
        num >>= 1

    size = len(binary)
    for _ in range(size + 1, 2 ** (int(math.log2(size)) + 1)):
        binary.append(0)

    return binary[::-1]
