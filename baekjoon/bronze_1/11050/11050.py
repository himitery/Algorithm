import sys

fast_input = sys.stdin.readline
fast_output = sys.stdout.write


def factorial(num: int) -> int:
    result = 1
    for value in range(2, num + 1):
        result *= value
    return result


def app() -> None:
    N, K = list(map(int, fast_input().split()))

    fast_output(f"{factorial(N) // (factorial(K) * factorial(N - K))}\n")


if __name__ == "__main__":
    app()
