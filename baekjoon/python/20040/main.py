import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [tuple(map(int, read().split())) for _ in range(self.m)]
        self.parent = list(range(self.n))

    def solve(self) -> None:
        count = 0
        for idx, (x, y) in enumerate(self.data):
            if self.find_cycle(x, y):
                count = idx + 1
                break

        print(count)

    def find_cycle(self, x: int, y: int) -> bool:
        root_x, root_y = self.find_root(x), self.find_root(y)
        if root_x == root_y:
            return True

        self.parent[root_y] = root_x
        return False

    def find_root(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x


if __name__ == "__main__":
    Problem().solve()
