import heapq
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data, self.cached = defaultdict(set), [0 for _ in range(self.n + 1)]

        for _ in range(self.m):
            src, dest = map(int, read().split())
            self.data[src].add(dest)
            self.cached[dest] += 1

    def solve(self) -> None:
        queue, sequence = self.find_available(), []

        while queue and len(sequence) < self.n:
            if len(queue) == 0:
                queue.extend(self.find_available())

            num = heapq.heappop(queue)
            sequence.append(num)

            for next_num in sorted(self.data[num]):
                self.cached[next_num] -= 1
                if self.cached[next_num] == 0:
                    heapq.heappush(queue, next_num)

        print(*sequence)

    def find_available(self) -> list[int]:
        values = []
        for num in range(1, self.n + 1):
            if self.cached[num] == 0:
                heapq.heappush(values, num)

        return values


if __name__ == "__main__":
    Problem().solve()
