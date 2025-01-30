import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.data = [list(map(int, list(read()))) for _ in range(9)]
        self.empties, self.rows, self.cols, self.tiles = (
            [],
            [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)],
            [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)],
            [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)],
        )

        for y in range(9):
            for x in range(9):
                if self.data[y][x] == 0:
                    self.empties.append((y, x))
                    continue

                self.rows[y] -= {self.data[y][x]}
                self.cols[x] -= {self.data[y][x]}
                self.tiles[(y // 3) * 3 + x // 3] -= {self.data[y][x]}

    def solve(self) -> None:
        self.backtrack(0)

        for row in self.data:
            print(*row, sep="")

    def backtrack(self, index: int) -> bool:
        if index == len(self.empties):
            return True

        y, x = self.empties[index]

        for value in sorted(
            self.rows[y] & self.cols[x] & self.tiles[(y // 3) * 3 + x // 3]
        ):
            self.data[y][x] = value
            self.rows[y].remove(value)
            self.cols[x].remove(value)
            self.tiles[(y // 3) * 3 + x // 3].remove(value)
            if self.backtrack(index + 1):
                return True

            self.data[y][x] = 0
            self.rows[y].add(value)
            self.cols[x].add(value)
            self.tiles[(y // 3) * 3 + x // 3].add(value)

        return False


if __name__ == "__main__":
    Problem().solve()
