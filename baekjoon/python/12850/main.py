import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.minutes = int(read())
        self.matrix = [
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
        ]

        self.size = 8
        self.mod = 1_000_000_007

    def solve(self) -> None:
        time, matrix, result = (
            self.minutes,
            self.matrix,
            [[int(row == col) for col in range(self.size)] for row in range(self.size)],
        )

        while time > 0:
            if time % 2 == 1:
                result = self.matrix_multiply(result, matrix)
            matrix = self.matrix_multiply(matrix, matrix)
            time //= 2

        print(result[0][0] % self.mod)

    def matrix_multiply(self, matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
        result = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    result[x][y] += matrix_a[x][z] * matrix_b[z][y]
                    result[x][y] %= self.mod

        return result


if __name__ == "__main__":
    Problem().solve()
