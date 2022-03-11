import sys

fast_input = sys.stdin.readline


def app() -> None:
    K: int = int(fast_input())

    data: list[int] = list()
    for _ in range(K):
        value: int = int(fast_input())
        if value == 0:
            data.pop()
        else:
            data.append(value)
    print(sum(data))


if __name__ == "__main__":
    app()
