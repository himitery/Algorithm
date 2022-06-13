import sys

fast_input = sys.stdin.readline


def app() -> None:
    n: int = int(fast_input())
    data: list[int] = [0] + [int(fast_input()) for _ in range(n)] + [0]

    dp: list[int] = [0] * (n + 2)
    dp[1] = data[1]
    dp[2] = data[1] + data[2]
    for index in range(3, n + 1):
        dp[index] = (
            max(
                dp[index - 3] + data[index - 1],
                dp[index - 2],
            )
            + data[index]
        )
    print(dp[n])


if __name__ == "__main__":
    app()
