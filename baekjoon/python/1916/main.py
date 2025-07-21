import heapq
import math
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = int(read()), int(read())

        self.graph = defaultdict(list[tuple[int, int]])
        for src, dest, price in [map(int, read().split()) for _ in range(self.m)]:
            self.graph[src].append((dest, price))

        self.start, self.end = map(int, read().split())

    def solve(self) -> None:
        print(self.dijkstra(self.start, self.end))

    def dijkstra(self, start: int, end: int) -> int:
        heap, prices = [(0, start)], [0 if idx == start else math.inf for idx in range(self.n + 1)]

        while heap:
            current_price, current_city = heapq.heappop(heap)
            if current_city == end:
                break

            if current_price > prices[current_city]:
                continue

            for next_city, price in self.graph[current_city]:
                if current_price + price < prices[next_city]:
                    prices[next_city] = current_price + price
                    heapq.heappush(heap, (current_price + price, next_city))

        return int(prices[end])


if __name__ == "__main__":
    Problem().solve()
