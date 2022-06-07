import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    time: list[int] = sorted(map(int, fast_input().split()))

    wait_time: list[int] = [0]
    for value in time:
        wait_time.append(wait_time[-1] + value)
    print(sum(wait_time))


if __name__ == "__main__":
    app()
