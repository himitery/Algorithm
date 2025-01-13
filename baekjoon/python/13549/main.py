import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.x, self.y = map(int, read().split())

    def solve(self) -> None:
        queue, visited = deque([(0, self.x)]), {self.x}

        while queue:
            time, x = queue.popleft()
            if x == self.y:
                print(time)
                return

            for next_time, next_x, condition in [
                (time, x * 2, x < self.y),
                (time + 1, x - 1, x - 1 >= 0),
                (time + 1, x + 1, x < self.y),
            ]:
                if condition and next_x not in visited:
                    queue.append((next_time, next_x))
                    visited.add(next_x)


if __name__ == "__main__":
    Problem().solve()
