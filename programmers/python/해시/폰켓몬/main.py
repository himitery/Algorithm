from typing import List


def solution(nums: List[int]) -> int:
    return min(len(nums) // 2, len(set(nums)))
