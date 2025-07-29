import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.tree = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        weights = [[0] * (len(self.tree[-1]))]
        for row in self.tree[-1:0:-1]:
            weights.append(
                [max(row[idx] + weights[-1][idx], row[idx + 1] + weights[-1][idx + 1]) for idx in range(len(row) - 1)]
            )

        print(weights[-1][0] + self.tree[0][0])


if __name__ == "__main__":
    Problem().solve()
