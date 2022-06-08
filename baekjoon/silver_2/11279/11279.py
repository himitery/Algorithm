import heapq
import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())

    data: list[int] = list()
    for _ in range(N):
        key: int = int(fast_input())
        if key == 0:
            if len(data) == 0:
                print(0)
            else:
                print(-heapq.heappop(data))
        else:
            heapq.heappush(data, -key)


if __name__ == "__main__":
    app()
