import heapq
import math
import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.m = int(read())
        self.bus = defaultdict(list)

        for _ in range(self.m):
            src, dest, weight = map(int, read().split())
            self.bus[src - 1].append((dest - 1, weight))

        self.src, self.dest = map(lambda x: int(x) - 1, read().split())

    def solve(self) -> None:
        weights = [math.inf] * self.n
        weights[self.src] = 0

        queue, path = [(0.0, self.src)], [-1 for _ in range(self.n)]
        while queue:
            weight, city = heapq.heappop(queue)
            weight = -weight
            if weights[city] < weight:
                continue

            for next_city, next_weight in self.bus[city]:
                if weight + next_weight < weights[next_city]:
                    weights[next_city] = weight + next_weight
                    path[next_city] = city
                    heapq.heappush(queue, (-weights[next_city], next_city))

        res = self.find_path(path)

        print(int(weights[self.dest]))
        print(len(res))
        print(*res)

    def find_path(self, path: list[int]) -> list[int]:
        current, result = self.dest, []
        while current != -1:
            result.append(current + 1)
            current = path[current]

        return list(reversed(result))


if __name__ == "__main__":
    Problem().solve()
