import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        count = 0

        stack = deque([(0, 0, 0, 0)])
        while stack:
            row, columns, left_diagonals, right_diagonals = stack.pop()
            if row == self.n:
                count += 1
                continue

            bits = ~(columns | left_diagonals | right_diagonals) & ((1 << self.n) - 1)
            while bits:
                bit = bits & -bits
                bits -= bit

                stack.append(
                    (
                        row + 1,
                        columns | bit,
                        (left_diagonals | bit) << 1,
                        (right_diagonals | bit) >> 1,
                    )
                )

        print(count)


if __name__ == "__main__":
    Problem().solve()
