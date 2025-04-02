from typing import List, Set


def solution(coin: int, cards: List[int]) -> int:
    n, count = len(cards), 1
    init, picked, remained = set(cards[: n // 3]), set(), cards[n // 3 :][::-1]

    while remained:
        picked |= {remained.pop(), remained.pop()}

        found = False
        for x, y, amount in [(init, init, 0), (init, picked, 1), (picked, picked, 2)]:
            if amount > coin:
                break

            if (pair := find_pair(n + 1, x, y)) and pair:
                found = True
                init, picked = init - pair, picked - pair
                count, coin = count + 1, coin - amount
                break

        if not found:
            break

    return count


def find_pair(target: int, x: Set[int], y: Set[int]) -> Set[int]:
    for card in x:
        if target - card in y:
            return {card, target - card}

    return set()
