import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = list(map(int, fast_input().split()))

    data: dict[str:str] = dict()
    for _ in range(N):
        key, value = fast_input().split()
        data[key] = value

    for _ in range(M):
        key = fast_input().strip()
        print(data[key])


if __name__ == "__main__":
    app()
