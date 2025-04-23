import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.queries = [tuple(map(int, read().split())) for _ in range(self.n)]

        self.size = 1
        while self.size <= 1_000_000:
            self.size <<= 1

        self.tree = [0] * self.size * 2

    def solve(self) -> None:
        for query in self.queries:
            if len(query) == 2:
                flavor = self.query(query[1])
                print(flavor)

                self.update(flavor - 1, -1)

            if len(query) == 3:
                flavor, count = query[1:]
                self.update(flavor - 1, count)

    def update(self, flavor: int, count: int):
        node = self.size + flavor
        self.tree[node] += count

        while node > 1:
            node //= 2
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, k: int) -> int:
        node = 1
        while node < self.size:
            left, right = node << 1, (node << 1) | 1

            if self.tree[left] >= k:
                node = left
            else:
                k -= self.tree[left]
                node = right

        return node - self.size + 1


if __name__ == "__main__":
    Problem().solve()
