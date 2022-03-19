import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())

    data: list[int] = [0] * (N + 1)
    for num in range(2, N + 1):
        data[num] = data[num - 1] + 1
        if num % 3 == 0:
            data[num] = min(data[num], data[num // 3] + 1)
        if num % 2 == 0:
            data[num] = min(data[num], data[num // 2] + 1)
    print(data[N])


if __name__ == "__main__":
    app()
