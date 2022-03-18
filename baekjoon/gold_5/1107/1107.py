import sys

fast_input = sys.stdin.readline


def check(target: int, button: set[int]) -> bool:
    for num in str(target):
        if int(num) not in button:
            return False
    return True


def app() -> None:
    N: int = int(fast_input())
    M: int = int(fast_input())
    button: set[int] = set([x for x in range(0, 10)])
    if M != 0:
        broken: list[int] = list(map(int, fast_input().split()))
        button = set([x for x in range(0, 10) if x not in broken])

    result: int = abs(N - 100)
    for num in range(500000 * 2 + 1):
        if check(num, button):
            result = min(result, len(str(num)) + abs(N - num))
    print(result)


if __name__ == "__main__":
    app()
