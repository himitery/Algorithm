import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.in_order = list(map(int, read().split()))
        self.post_order = list(map(int, read().split()))

        self.in_order_index = {num: idx for idx, num in enumerate(self.in_order)}
        self.post_order_index = {num: idx for idx, num in enumerate(self.post_order)}

    def solve(self) -> None:
        print(*self.pre_order())

    def pre_order(self) -> list[int]:
        stack, sequence = deque([self.post_order[-1]]), []

        while stack:
            num = stack.pop()
            sequence.append(num)

            right_root = self.find_right_root(num)
            if right_root:
                stack.append(right_root)

            left_root = self.find_left_root(num)
            if left_root:
                stack.append(left_root)

        return sequence

    def find_left_root(self, num: int) -> int | None:
        if (
            self.in_order_index[num] == 0
            or self.post_order_index[self.in_order[self.in_order_index[num] - 1]] > self.post_order_index[num]
        ):
            return None

        left = self.in_order[self.in_order_index[num] - 1]
        while self.in_order_index[self.post_order[self.post_order_index[left] + 1]] < self.in_order_index[num]:
            left = self.post_order[self.post_order_index[left] + 1]

        return left

    def find_right_root(self, num: int) -> int | None:
        if self.post_order_index[num] == 0:
            return None

        right = self.post_order[self.post_order_index[num] - 1]
        if self.in_order_index[right] > self.in_order_index[num]:
            return right

        return None


if __name__ == "__main__":
    Problem().solve()
