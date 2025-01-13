import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.x, self.y = (read(), read())

    def solve(self) -> None:
        lcs = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]

        for row in range(1, len(self.x) + 1):
            for col in range(1, len(self.y) + 1):
                word_x, word_y = self.x[row - 1], self.y[col - 1]
                if word_x == word_y:
                    lcs[row][col] = lcs[row - 1][col - 1] + 1
                else:
                    lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])

        print(lcs[-1][-1])


if __name__ == "__main__":
    Problem().solve()
