import sys

fast_input = sys.stdin.readline


def app() -> None:
    n: int = int(fast_input())

    data: list[int] = [0] * max(n + 1, 3)
    data[1] = 1
    data[2] = 2
    for i in range(3, n + 1):
        data[i] = data[i - 1] + data[i - 2]
    print(data[n] % 10_007)


if __name__ == "__main__":
    app()
