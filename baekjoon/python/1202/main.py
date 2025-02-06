import heapq
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.k = map(int, read().split())
        self.jewels = sorted([tuple(map(int, read().split())) for _ in range(self.n)])
        self.bags = sorted([int(read()) for _ in range(self.k)])

    def solve(self) -> None:
        heap, total, idx = [], 0, 0
        for bag in self.bags:
            while idx < self.n and self.jewels[idx][0] <= bag:
                heapq.heappush(heap, -self.jewels[idx][1])
                idx += 1

            if heap:
                total -= heapq.heappop(heap)

        print(total)


if __name__ == "__main__":
    Problem().solve()
