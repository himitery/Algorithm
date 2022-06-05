import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    data: list[int] = list(map(int, fast_input().split()))

    key_dict: dict[int: int] = dict()
    for index, key in enumerate(sorted(set(data))):
        key_dict[key] = index

    for value in data:
        print(key_dict[value], end=" ")
    print()


if __name__ == "__main__":
    app()
