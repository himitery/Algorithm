import sys
from collections import deque
from copy import deepcopy

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.matrix = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        queue, maximum = deque([(0, self.matrix[:])]), 0

        while queue:
            count, matrix = queue.popleft()
            if count == 5:
                for row in matrix:
                    maximum = max(maximum, max(row))
                continue

            queue.append((count + 1, self.move_left((deepcopy(matrix)))))
            queue.append((count + 1, self.move_right((deepcopy(matrix)))))
            queue.append((count + 1, self.move_up((deepcopy(matrix)))))
            queue.append((count + 1, self.move_down((deepcopy(matrix)))))

        print(maximum)

    def move_left(self, matrix: list[list[int]]) -> list[list[int]]:
        for y in range(self.n):
            for x in range(self.n - 1):
                matrix[y] = self.remove_zero(matrix[y][:])

                if matrix[y][x] == matrix[y][x + 1]:
                    matrix[y][x] *= 2
                    matrix[y] = matrix[y][: x + 1] + matrix[y][x + 2 :] + [0]

        return matrix

    def move_right(self, matrix: list[list[int]]) -> list[list[int]]:
        return [row[::-1] for row in self.move_left([row[::-1] for row in matrix])]

    def move_up(self, matrix: list[list[int]]) -> list[list[int]]:
        for x in range(self.n):
            line = [matrix[y][x] for y in range(self.n)]

            for idx in range(self.n - 1):
                line = self.remove_zero(line[:])

                if line[idx] == line[idx + 1]:
                    line[idx] *= 2
                    line = line[: idx + 1] + line[idx + 2 :] + [0]

            for idx in range(self.n):
                matrix[idx][x] = line[idx]

        return matrix

    def move_down(self, matrix: list[list[int]]) -> list[list[int]]:
        return self.move_up(matrix[::-1])[::-1]

    def remove_zero(self, data: list[int]) -> list[int]:
        removed = [value for value in data if value != 0]

        return removed + [0] * (len(data) - len(removed))


if __name__ == "__main__":
    Problem().solve()
