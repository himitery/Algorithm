from collections import deque


def solution(x: int, y: int, n: int) -> int:
    queue, visited = deque([(0, x)]), set()

    while queue:
        step, num = queue.popleft()
        if num in visited or num > y:
            continue

        if num == y:
            return step

        visited.add(num)
        queue.append((step + 1, num + n))
        queue.append((step + 1, num * 2))
        queue.append((step + 1, num * 3))

    return -1
