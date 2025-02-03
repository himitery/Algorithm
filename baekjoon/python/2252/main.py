import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.graph = defaultdict(list[int])
        self.weight = [0 for _ in range(self.n + 1)]

        for _ in range(self.m):
            x, y = map(int, read().split())

            self.graph[y].append(x)
            self.weight[x] += 1

    def solve(self) -> None:
        print(*self.topological_sort())

    def topological_sort(self) -> list[int]:
        queue, sequence = (
            deque(
                list(filter(lambda num: self.weight[num] == 0, range(1, self.n + 1)))
            ),
            [],
        )
        while queue:
            target = queue.popleft()
            sequence.append(target)

            for next_target in reversed(self.graph[target]):
                self.weight[next_target] -= 1
                if self.weight[next_target] == 0:
                    queue.append(next_target)

        return sequence[-1::-1]


if __name__ == "__main__":
    Problem().solve()
