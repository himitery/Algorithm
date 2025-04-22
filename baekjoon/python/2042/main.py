import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.k = map(int, read().split())
        self.nums = [int(read()) for _ in range(self.n)]
        self.query = [list(map(int, read().split())) for _ in range(self.m + self.k)]

        self.size, self.tree = self.make_tree()

    def solve(self) -> None:
        for command, src, dest in self.query:
            if command == 1:
                self.update(src - 1, dest)
            if command == 2:
                print(self.find_sum(src - 1, dest - 1))

    def make_tree(self) -> tuple[int, list[int]]:
        size = 1
        while size < self.n:
            size <<= 1

        tree = [0 for _ in range(size * 2)]
        for idx in range(self.n):
            tree[size + idx] = self.nums[idx]
        for idx in range(size - 1, 0, -1):
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

        return size, tree

    def update(self, index: int, num: int) -> None:
        idx = self.size + index
        self.tree[idx] = num

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def find_sum(self, src: int, dest: int) -> int:
        left, right, value = self.size + src, self.size + dest, 0

        while left <= right:
            if left % 2 == 1:
                value += self.tree[left]
                left += 1
            if right % 2 == 0:
                value += self.tree[right]
                right -= 1

            left, right = left // 2, right // 2

        return value


if __name__ == "__main__":
    Problem().solve()
