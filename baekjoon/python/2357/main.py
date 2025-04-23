import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.nums = [int(read()) for _ in range(self.n)]
        self.query = [map(lambda x: int(x) - 1, read().split()) for _ in range(self.m)]

    def solve(self) -> None:
        tree = self.make_tree()

        for start, end in self.query:
            print(*self.find_min_max(tree, start, end), sep=" ")

    def make_tree(self) -> list[tuple[int, int]]:
        tree = [(0, 0) for _ in range(self.n * 2)]

        for idx in range(self.n):
            tree[self.n + idx] = self.nums[idx], self.nums[idx]

        for idx in range(self.n - 1, 0, -1):
            left = tree[idx << 1]
            right = tree[idx << 1 | 1]
            tree[idx] = min(left[0], right[0]), max(left[1], right[1])

        return tree

    def find_min_max(self, tree: list[tuple[int, int]], start: int, end: int) -> tuple[int, int]:
        left, right = self.n + start, self.n + end + 1
        minimum, maximum = math.inf, -math.inf

        while left < right:
            if left & 1:
                minimum = min(minimum, tree[left][0])
                maximum = max(maximum, tree[left][1])
                left += 1
            if right & 1:
                right -= 1
                minimum = min(minimum, tree[right][0])
                maximum = max(maximum, tree[right][1])
            left >>= 1
            right >>= 1

        return int(minimum), int(maximum)


if __name__ == "__main__":
    Problem().solve()
