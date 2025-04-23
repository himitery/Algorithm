def solution(n: int) -> int:
    dp = [0, 1, 3, 10, 23, 62, 170]
    if n < 7:
        return dp[n]

    for _ in range(7, n + 1):
        x = (dp[-1] + 2 * dp[-2] + 6 * dp[-3] + dp[-4] - dp[-6]) % 1_000_000_007
        dp = dp[1:] + [x]

    return dp[-1]
