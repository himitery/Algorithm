import sys
from collections import deque

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    M: int = int(fast_input())

    computer: dict[int : list[int]] = dict()
    for _ in range(M):
        src, dist = list(map(int, input().split()))

        if src in computer.keys():
            computer[src].append(dist)
        else:
            computer[src] = [dist]

        if dist in computer.keys():
            computer[dist].append(src)
        else:
            computer[dist] = [src]

    queue: deque = deque([1])
    visited: list[int] = [1]
    while queue:
        target: int = queue.popleft()

        for next_computer in computer[target]:
            if next_computer not in visited:
                queue.append(next_computer)
                visited.append(next_computer)

    print(len(visited) - 1)


if __name__ == "__main__":
    app()
