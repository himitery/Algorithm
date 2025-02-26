import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.k = map(int, read().split())
        self.cards = sorted(map(int, read().split()))
        self.sequence = list(map(int, read().split()))

        self.roots = {x: x for x in self.cards}

    def solve(self) -> None:
        for num in self.sequence:
            print(self.find_card(num))

    def find_card(self, num: int) -> int:
        idx = self.binary_search(num)
        if self.cards[idx] == num:
            idx += 1

        root = self.roots[self.cards[idx]]
        next_root = self.binary_search(root) + 1
        if next_root < self.m:
            self.roots[self.cards[idx]] = self.roots[self.cards[next_root]]

        return root

    def binary_search(self, num: int) -> int:
        left, right = 0, self.m - 1

        while left <= right:
            mid = (left + right) // 2

            if self.cards[mid] == num:
                return mid
            elif self.cards[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    Problem().solve()
