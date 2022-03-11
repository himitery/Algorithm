import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())

    data: dict[int:int] = dict()
    for _ in range(N):
        value: int = int(fast_input())
        if value in data.keys():
            data[value] += 1
        else:
            data[value] = 1

    for key in sorted(data.keys()):
        for _ in range(data[key]):
            print(key)


if __name__ == "__main__":
    app()
