import heapq
import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    heap: list[int] = list()

    for _ in range(N):
        value: int = int(fast_input())
        if value == 0:
            print(0 if len(heap) == 0 else heapq.heappop(heap))
        else:
            heapq.heappush(heap, value)


if __name__ == "__main__":
    app()
