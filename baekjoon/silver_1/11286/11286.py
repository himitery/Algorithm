import heapq
import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    heap: list[tuple[int, int]] = list()

    for _ in range(N):
        value: int = int(fast_input().strip())

        if value == 0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(heap, (abs(value), value))


if __name__ == "__main__":
    app()
