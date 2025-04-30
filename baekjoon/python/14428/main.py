import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.nums = list(map(int, read().split()))

        self.m = int(read())
        self.queries = [map(int, read().split()) for _ in range(self.m)]

    def solve(self) -> None:
        tree = self.make_tree()

        for command, x, y in self.queries:
            if command == 1:
                tree = self.update_tree(tree, x - 1, y)

            if command == 2:
                print(self.query(tree, x - 1, y))

    def make_tree(self) -> list[tuple[int, int]]:
        tree = [(0, 0)] * self.n * 2

        for idx in range(self.n):
            tree[self.n + idx] = (idx + 1, self.nums[idx])

        for idx in range(self.n - 1, 0, -1):
            tree[idx] = self.select(tree[idx << 1], tree[(idx << 1) | 1])

        return tree

    def update_tree(self, tree: list[tuple[int, int]], idx: int, value: int) -> list[tuple[int, int]]:
        node = self.n + idx
        tree[node] = (tree[node][0], value)

        while node:
            node >>= 1
            tree[node] = self.select(tree[node << 1], tree[(node << 1) | 1])

        return tree

    def query(self, tree: list[tuple[int, int]], start: int, end: int) -> int:
        left, right, value = self.n + start, self.n + end, (math.inf, math.inf)

        while left < right:
            if left & 1:
                value = self.select(value, tree[left])
                left += 1

            if right & 1:
                right -= 1
                value = self.select(value, tree[right])

            left >>= 1
            right >>= 1

        return value[0]

    def select(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        x_idx, x_value = x
        y_idx, y_value = y

        if x_value != y_value:
            return x if x_value < y_value else y

        return x if x_idx < y_idx else y


if __name__ == "__main__":
    Problem().solve()
