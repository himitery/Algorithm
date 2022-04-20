import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = list(map(int, fast_input().split()))
    data: list[int] = list(map(int, fast_input().split()))

    for index in range(1, N):
        data[index] += data[index - 1]

    for _ in range(M):
        start, end = list(map(int, fast_input().split()))
        print(data[end - 1] - (data[start - 2] if start != 1 else 0))


if __name__ == "__main__":
    app()
