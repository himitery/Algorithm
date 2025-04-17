import itertools
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.s, self.e, self.t = map(int, read().split())
        self.matrix = [list(map(int, list(read()))) for _ in range(self.n)]

        self.mod = 1_000_003
        self.size = self.n * 5

    def solve(self) -> None:
        time, matrix, result = (
            self.t,
            self.build_expanded_matrix(),
            [[int(i == j) for j in range(self.size)] for i in range(self.size)],
        )

        while time > 0:
            if time % 2 == 1:
                result = self.matrix_multiply(result, matrix)
            matrix = self.matrix_multiply(matrix, matrix)
            time //= 2

        print(result[(self.e - 1) * 5][(self.s - 1) * 5] % self.mod)

    def build_expanded_matrix(self) -> list[list[int]]:
        matrix = [[0] * self.size for _ in range(self.size)]

        for idx, time in itertools.product(range(self.n), range(4)):
            matrix[idx * 5 + time + 1][idx * 5 + time] = 1

        for x, y in itertools.product(range(self.n), range(self.n)):
            if (delay := self.matrix[x][y]) and delay > 0:
                matrix[y * 5][x * 5 + (delay - 1)] = 1

        return matrix

    def matrix_multiply(self, matrix_x: list[list[int]], matrix_y: list[list[int]]) -> list[list[int]]:
        result = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for x, y in itertools.product(range(self.size), range(self.size)):
            if matrix_x[x][y] == 0:
                continue

            for z in range(self.size):
                result[x][z] += matrix_x[x][y] * matrix_y[y][z]
                result[x][z] %= self.mod

        return result


if __name__ == "__main__":
    Problem().solve()
