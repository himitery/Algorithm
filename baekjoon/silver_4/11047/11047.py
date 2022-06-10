import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, K = tuple(map(int, fast_input().split()))
    money: list[int] = [int(fast_input()) for _ in range(N)]

    count: int = 0
    while K > 0 and money:
        if K - money[-1] >= 0:
            count += K // money[-1]
            K %= money[-1]
        else:
            money.pop()
    print(count)


if __name__ == "__main__":
    app()
