import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.k = map(int, read().split())
        self.nums = [int(read()) for _ in range(self.n)]
        self.queries = [map(int, read().split()) for _ in range(self.m + self.k)]

        self.mod = 1_000_000_007

    def solve(self) -> None:
        tree = self.make_tree()

        for command, x, y in self.queries:
            if command == 1:
                tree = self.update_tree(tree, x - 1, y)

            if command == 2:
                print(self.query(tree, x - 1, y))

    def make_tree(self) -> list[int]:
        tree = [0] * self.n * 2

        for idx in range(self.n):
            tree[self.n + idx] = self.nums[idx]

        for idx in range(self.n - 1, 0, -1):
            tree[idx] = (tree[idx << 1] * tree[(idx << 1) | 1]) % self.mod

        return tree

    def update_tree(self, tree: list[int], idx: int, value: int) -> list[int]:
        node = self.n + idx
        tree[node] = value

        while node:
            node >>= 1
            tree[node] = (tree[node << 1] * tree[(node << 1) | 1]) % self.mod

        return tree

    def query(self, tree: list[int], start: int, end: int) -> int:
        left, right, value = self.n + start, self.n + end, 1

        while left < right:
            if left & 1:
                value = (value * tree[left]) % self.mod
                left += 1

            if right & 1:
                right -= 1
                value = (value * tree[right]) % self.mod

            left >>= 1
            right >>= 1

        return value


if __name__ == "__main__":
    Problem().solve()
