import math
import sys
from collections import deque, defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.k = map(int, read().split())

    def solve(self) -> None:
        queue, visited, minimum = (
            deque([(self.n, 0)]),
            defaultdict(lambda: -1),
            (math.inf, 0),
        )

        while queue:
            x, time = queue.popleft()
            if time > minimum[0]:
                break
            if x == self.k and time <= minimum[0]:
                minimum = (time, minimum[1] + 1)

            for next_x, condition in [
                (x - 1, x - 1 >= 0),
                (x + 1, x < self.k),
                (x * 2, 0 < x < self.k),
            ]:
                if condition and visited[next_x] == -1 or visited[next_x] == time + 1:
                    visited[next_x] = time + 1
                    queue.append((next_x, time + 1))

        print(*minimum, sep="\n")


if __name__ == "__main__":
    Problem().solve()
