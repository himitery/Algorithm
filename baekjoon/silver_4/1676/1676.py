import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())

    data: int = 1
    for num in range(2, N + 1):
        data *= num

    count: int = 0
    for num in reversed(list(str(data))):
        if num != "0":
            break
        count += 1
    print(count)


if __name__ == "__main__":
    app()
