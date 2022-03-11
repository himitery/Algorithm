import sys

fast_input = sys.stdin.readline


def app() -> None:
    data: list[tuple[int]] = [
        tuple(list(map(int, fast_input().split())))
        for _ in range(int(fast_input()))
    ]

    for value in sorted(data, key=lambda x: (x[0], x[1])):
        print(value[0], value[1])


if __name__ == "__main__":
    app()
