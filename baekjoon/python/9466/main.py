import sys
from collections import deque, defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(lambda x: int(x) - 1, read().split()))

        self.visited = [False for _ in range(self.n)]
        self.cycle = self.n

    def solve(self) -> None:
        for num in range(self.n):
            if not self.visited[num]:
                self.find_cycle(num)

        print(self.cycle)

    def find_cycle(self, num: int) -> None:
        stack, history, cached = deque([num]), {num}, defaultdict(lambda: -1)

        while stack:
            current = stack.pop()
            cached[current], self.visited[current] = len(history) - 1, True

            if self.data[current] in history:
                self.cycle -= len(history) - cached[self.data[current]]
                return

            if not self.visited[self.data[current]]:
                stack.append(self.data[current])
                history.add(self.data[current])


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
