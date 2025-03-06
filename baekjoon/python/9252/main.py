import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.x, self.y = read(), read()

    def solve(self) -> None:
        lcs = self.find_lcs()
        print(lcs[-1][-1])
        if lcs[-1][-1] != 0:
            print(self.backtrack(lcs))

    def find_lcs(self) -> list[list[int]]:
        lcs = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]

        for row in range(len(self.x)):
            for col in range(len(self.y)):
                word_x, word_y = self.x[row], self.y[col]
                if word_x == word_y:
                    lcs[row + 1][col + 1] = lcs[row][col] + 1
                else:
                    lcs[row + 1][col + 1] = max(lcs[row + 1][col], lcs[row][col + 1])

        return lcs

    def backtrack(self, lcs: list[list[int]]) -> str:
        result, x, y = "", len(self.x), len(self.y)
        while x > 0 and y > 0:
            if self.x[x - 1] == self.y[y - 1]:
                result = self.x[x - 1] + result
                x -= 1
                y -= 1
            elif lcs[x - 1][y] > lcs[x][y - 1]:
                x -= 1
            else:
                y -= 1

        return result


if __name__ == "__main__":
    Problem().solve()
