import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, r, c = list(map(int, fast_input().split()))

    size: int = 2 ** (N - 1)
    count: int = 0
    while size >= 1:
        count += (r // size) * 2 * size**2 + (c // size) * size**2
        r -= r // size * size
        c -= c // size * size
        size = size // 2
    print(count)


if __name__ == "__main__":
    app()
