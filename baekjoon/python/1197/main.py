import heapq
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.v, self.e = map(int, read().split())
        self.data = [[] for _ in range(self.v)]

        for _ in range(self.e):
            src, dest, weight = map(int, read().split())
            self.data[src - 1].append((weight, dest - 1))
            self.data[dest - 1].append((weight, src - 1))

    def solve(self) -> None:
        queue, visited, cost = [(0, 0)], set(), 0

        while queue and len(visited) < self.v:
            weight, node = heapq.heappop(queue)
            if node in visited:
                continue

            visited.add(node)
            cost += weight

            for next_weight, next_dest in self.data[node]:
                if next_dest not in visited:
                    heapq.heappush(queue, (next_weight, next_dest))

        print(cost)


if __name__ == "__main__":
    Problem().solve()
