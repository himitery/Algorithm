import heapq
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.array = tuple(map(int, read().split()))
        self.target = tuple(sorted(self.array))
        self.m = int(read())
        self.graph = {x: [] for x in range(self.n)}

        for _ in range(self.m):
            left, right, weight = map(int, read().split())
            self.graph[left - 1].append((weight, right - 1))
            self.graph[right - 1].append((weight, left - 1))

    def solve(self) -> None:
        print(self.dijkstra())

    def dijkstra(self) -> int:
        heap, visited, costs = [(0, self.array)], set(), {self.array: 0}

        while heap:
            cost, array = heapq.heappop(heap)
            if array == self.target:
                return cost

            if array in visited:
                continue

            visited.add(array)
            for src in range(self.n):
                for weight, dest in self.graph[src]:
                    if src >= dest:
                        continue

                    new_array = list(array)
                    new_array[src], new_array[dest] = new_array[dest], new_array[src]
                    new_array = tuple(new_array)

                    if new_array not in costs or cost + weight < costs[new_array]:
                        costs[new_array] = cost + weight
                        heapq.heappush(heap, (cost + weight, new_array))

        return -1


if __name__ == "__main__":
    Problem().solve()
