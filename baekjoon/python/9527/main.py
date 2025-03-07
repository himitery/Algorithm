import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.x, self.y = map(int, read().split())

    def solve(self) -> None:
        print(self.count_one(self.y) - self.count_one(self.x - 1))

    def count_one(self, num: int) -> int:
        count, bit = 0, 1
        while bit <= num:
            count += (num + 1) // (bit * 2) * bit + max(0, (num + 1) % (bit * 2) - bit)
            bit *= 2

        return count


if __name__ == "__main__":
    Problem().solve()
