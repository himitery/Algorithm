import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())

    meeting: list[tuple[int]] = sorted(
        [tuple(map(int, fast_input().split())) for _ in range(N)],
        key=lambda x: (x[1], x[0]),
    )

    time = count = 0
    for start, end in meeting:
        if start >= time:
            time = end
            count += 1
    print(count)


if __name__ == "__main__":
    app()
