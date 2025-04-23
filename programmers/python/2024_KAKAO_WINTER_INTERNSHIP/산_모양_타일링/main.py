from typing import List


def solution(n: int, tops: List[int]) -> int:
    dp, mod = [[0, 0, 0, 0] for _ in range(n)], 10_007
    dp[0] = [1, tops[0], 1, 1]

    for idx in range(1, n):
        none, top, left, right = (
            sum(dp[idx - 1]),
            sum(dp[idx - 1]) * tops[idx],
            sum(dp[idx - 1][:3]),
            sum(dp[idx - 1]),
        )

        dp[idx] = [none % mod, top % mod, left % mod, right % mod]

    return sum(dp[-1]) % mod
