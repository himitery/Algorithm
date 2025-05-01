import heapq
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = []
        for _ in range(self.n):
            start, end = map(int, read().split())
            self.data.append((min(start, end), max(start, end)))

        self.d = int(read())

    def solve(self) -> None:
        heap, maximum = [], 0

        for start, end in sorted(self.data, key=lambda x: x[1]):
            if end - start > self.d:
                continue

            heapq.heappush(heap, start)
            while heap and heap[0] < end - self.d:
                heapq.heappop(heap)

            maximum = max(maximum, len(heap))

        print(maximum)


if __name__ == "__main__":
    Problem().solve()
