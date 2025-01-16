import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.size, self.exponent = map(int, read().split())
        self.matrix = [list(map(int, read().split())) for _ in range(self.size)]

    def solve(self) -> None:
        for row in self.matrix_pow(self.matrix, self.exponent):
            print(*list(map(lambda x: x % 1_000, row)))

    def matrix_pow(self, matrix: list[list[int]], exponent: int) -> list[list[int]]:
        if exponent == 1:
            return self.matrix

        half = self.matrix_pow(matrix, exponent // 2)
        half = self.mat_mul(half, half)

        if exponent % 2 == 1:
            half = self.mat_mul(matrix, half)

        return half

    def mat_mul(
        self,
        matrix_a: list[list[int]],
        matrix_b: list[list[int]],
    ) -> list[list[int]]:
        matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for idx in range(self.size**2):
            row, col = idx // self.size, idx % self.size
            for index in range(self.size):
                matrix[row][col] += matrix_a[row][index] * matrix_b[index][col]

            matrix[row][col] %= 1_000

        return matrix


if __name__ == "__main__":
    Problem().solve()
