import sys

fast_input = sys.stdin.readline


def app() -> None:
    L: int = int(fast_input())
    data: str = fast_input()

    result: int = 0
    for index in range(L):
        result += (ord(data[index]) - ord("a") + 1) * (31**index)
    print(result % 1234567891)


if __name__ == "__main__":
    app()
