import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.isbn = list(read())

    def solve(self) -> None:
        total = sum([(1 if idx % 2 == 0 else 3) * int(x) for idx, x in enumerate(self.isbn) if x != "*"])

        print(self.find_unknown(total))

    def find_unknown(self, total: int) -> int:
        weight = 1 if self.isbn.index("*") % 2 == 0 else 3

        for candidate in range(10):
            if (total + weight * candidate) % 10 == 0:
                return candidate

        return 0


if __name__ == "__main__":
    Problem().solve()
