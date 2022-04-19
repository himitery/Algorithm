import sys
from collections import deque

fast_input = sys.stdin.readline


def app() -> None:
    N, K = list(map(int, fast_input().split()))

    queue: deque = deque([N])
    visited: list[int] = [0 for _ in range(0, 100_000 + 1)]
    visited[N] = 1
    while queue:
        index: int = queue.popleft()
        if index == K:
            print(visited[index] - 1)
            break
        for new_index in (index - 1, index + 1, index * 2):
            if 0 <= new_index <= 100_000 and not visited[new_index]:
                queue.append(new_index)
                visited[new_index] = visited[index] + 1


if __name__ == "__main__":
    app()
