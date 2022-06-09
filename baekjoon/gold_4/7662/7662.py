import heapq
import sys

fast_input = sys.stdin.readline


def app() -> None:
    T: int = int(fast_input())

    for _ in range(T):
        max_priority = list[tuple[int, int]]()
        min_priority = list[tuple[int, int]]()
        status: list[bool] = [False] * 1_000_001

        Q: int = int(fast_input())
        for index in range(Q):
            execute, value = tuple(fast_input().split())
            if execute == "I":
                heapq.heappush(max_priority, (-int(value), index))
                heapq.heappush(min_priority, (int(value), index))
                status[index] = True
            elif execute == "D":
                if value == "1":
                    while max_priority and not status[max_priority[0][1]]:
                        heapq.heappop(max_priority)
                    if max_priority:
                        status[heapq.heappop(max_priority)[1]] = False
                elif value == "-1":
                    while min_priority and not status[min_priority[0][1]]:
                        heapq.heappop(min_priority)
                    if min_priority:
                        status[heapq.heappop(min_priority)[1]] = False

        while max_priority and not status[max_priority[0][1]]:
            heapq.heappop(max_priority)
        while min_priority and not status[min_priority[0][1]]:
            heapq.heappop(min_priority)
        if len(min_priority) == 0 and len(max_priority) == 0:
            print("EMPTY")
        else:
            print(-max_priority[0][0], min_priority[0][0])


if __name__ == "__main__":
    app()
