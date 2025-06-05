import math

from typing import List


def solution(temperature: int, t1: int, t2: int, a: int, b: int, onboard: List[int]) -> int:
    dp = [[math.inf for _ in range(-11, 42)] for _ in range(len(onboard))]
    dp[0][temperature] = 0

    for time, customer in enumerate(onboard):
        for temp in range(-10, 41):
            if customer and not t1 <= temp <= t2:
                dp[time][temp] = math.inf
                continue

            dp[time][temp] = min(
                dp[time][temp],
                dp[time - 1][temp] + b,
                dp[time - 1][temp - 1] + a,
                dp[time - 1][temp + 1] + a,
                dp[time - 1][temp] if temp == temperature else math.inf,
                dp[time - 1][temp - 1] if temp - 1 < temperature else math.inf,
                dp[time - 1][temp + 1] if temp + 1 > temperature else math.inf,
            )

    return int(min(dp[-1]))
