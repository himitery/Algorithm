import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = list(map(int, fast_input().split()))

    result: list = list(
        set([fast_input().strip() for _ in range(N)])
        & set([fast_input().strip() for _ in range(M)])
    )

    print(len(result))
    for name in sorted(result):
        print(name)


if __name__ == "__main__":
    app()
