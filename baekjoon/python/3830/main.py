import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.queries = []
        for line in [read().split() for _ in range(self.m)]:
            self.queries.append((line[0] == "?", list(map(int, line[1:]))))

        self.parent, self.weight = list(range(self.n + 1)), [0] * (self.n + 1)

    def solve(self) -> None:
        for is_query, args in self.queries:
            if not is_query:
                self.union(*args)
                continue

            x, y = args
            print("UNKNOWN" if self.find(x) != self.find(y) else self.weight[y] - self.weight[x])

    def find(self, num: int) -> int:
        path = []
        while self.parent[num] != num:
            path.append(num)
            num = self.parent[num]

        for node in reversed(path):
            self.weight[node] += self.weight[self.parent[node]]
            self.parent[node] = num

        return num

    def union(self, x: int, y: int, weight: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.weight[root_y] = self.weight[x] - self.weight[y] + weight


if __name__ == "__main__":
    while True:
        try:
            Problem().solve()
        except StopIteration:
            break
        except (EOFError, ValueError):
            break
