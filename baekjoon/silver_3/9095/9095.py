import sys

fast_input = sys.stdin.readline


def app() -> None:
    T: int = int(fast_input())
    num_list: list[int] = [int(fast_input()) for _ in range(T)]

    data: list[int] = [0, 1, 2, 4]
    for index in range(4, 11):
        data.append(sum(data[index - 3: index]))

    for num in num_list:
        print(data[num])


if __name__ == "__main__":
    app()
