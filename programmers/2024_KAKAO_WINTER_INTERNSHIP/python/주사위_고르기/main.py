import itertools
from collections import defaultdict
from typing import List, Tuple, Dict


def solution(dice: List[List[int]]) -> List[int]:
    n = len(dice)
    cached = {
        to_binary(ids): find_combinations([dice[idx] for idx in ids])
        for ids in itertools.combinations(range(n), n // 2)
    }

    result, visited = (0, []), set()
    for x_key in cached:
        if x_key in visited:
            continue

        y_key = (2**n - 1) - x_key
        visited |= {x_key, y_key}

        win, draw, lose = compare(cached[x_key], cached[y_key])
        if max(win, lose) > result[0]:
            result = (max(win, lose), to_num(x_key if win > lose else y_key))

    return result[1]


def to_binary(nums: Tuple[int, ...]) -> int:
    key = 0
    for idx in nums:
        key |= 1 << idx

    return key


def to_num(binary: int) -> List[int]:
    nums = []
    for idx in range(len(bin(binary)) - 2):
        if (1 << idx) & binary:
            nums.append(idx + 1)

    return nums


def find_combinations(dices: List[List[int]]) -> Dict[int, int]:
    combinations = defaultdict(int)
    for ids in itertools.product(range(6), repeat=len(dices)):
        key = sum([dice[idx] for idx, dice in zip(ids, dices)])
        combinations[key] += 1

    return combinations


def compare(x: Dict[int, int], y: Dict[int, int]) -> Tuple[int, int, int]:
    count = [0, 0, 0]

    for (x_key, x_value), (y_key, y_value) in itertools.product(x.items(), y.items()):
        if x_key > y_key:
            count[0] += x_value * y_value
        elif x_key == y_key:
            count[1] += x_value * y_value
        else:
            count[2] += x_value * y_value

    return count[0], count[1], count[2]
