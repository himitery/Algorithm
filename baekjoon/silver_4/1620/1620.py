import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = list(map(int, fast_input().split()))

    data: dict[str : list[tuple[int, str]]] = dict()
    for index in range(1, N + 1):
        target: str = fast_input().split("\n")[0]
        data[target] = index
        data[str(index)] = target

    for _ in range(M):
        print(data[fast_input().split("\n")[0]])


if __name__ == "__main__":
    app()
