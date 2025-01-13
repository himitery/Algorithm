import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.num = int(read())
        self.divide = 1_000_000_007

    def solve(self) -> None:
        if self.num == 0 or self.num == 1:
            print(self.num)
            return

        num, matrix, result = self.num - 1, [[1, 1], [1, 0]], [[1, 0], [0, 1]]
        while num > 0:
            if num % 2 != 0:
                result = self.mat_mul(result, matrix)
            matrix = self.mat_mul(matrix, matrix)
            num //= 2

        print(result[0][0])

    def mat_mul(
        self,
        matrix_a: list[list[int]],
        matrix_b: list[list[int]],
    ) -> list[list[int]]:
        return [
            [
                (matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0])
                % self.divide,
                (matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1])
                % self.divide,
            ],
            [
                (matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0])
                % self.divide,
                (matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1])
                % self.divide,
            ],
        ]


if __name__ == "__main__":
    Problem().solve()
