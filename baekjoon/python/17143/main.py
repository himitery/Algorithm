import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.r, self.c, self.m = map(int, read().split())
        self.matrix = [[0 for _ in range(self.c)] for _ in range(self.r)]
        self.sharks = {}

        direction = {1: (0, -1), 2: (0, 1), 3: (1, 0), 4: (-1, 0)}
        for _ in range(self.m):
            row, col, speed, direct, size = map(int, read().split())
            speed %= (2 * (self.r - 1)) if direct in [1, 2] else (2 * (self.c - 1))
            self.matrix[row - 1][col - 1] = size
            self.sharks[size] = ((col - 1, row - 1), speed, direction[direct])

    def solve(self) -> None:
        weight = 0
        for time in range(self.c):
            weight += self.fishing(time)
            self.move()

        print(weight)

    def fishing(self, time: int) -> int:
        for row in range(self.r):
            size = self.matrix[row][time]
            if size > 0:
                self.matrix[row][time] = 0
                del self.sharks[size]

                return size

        return 0

    def move(self) -> None:
        new_matrix, new_sharks = [[0 for _ in range(self.c)] for _ in range(self.r)], {}

        for size, ((x, y), speed, (dx, dy)) in self.sharks.items():
            remaining_moves = speed
            while remaining_moves:
                max_move = (self.c - 1 - x if dx > 0 else x) if dx != 0 else (self.r - 1 - y if dy > 0 else y)

                if remaining_moves <= max_move:
                    x, y = x + dx * remaining_moves, y + dy * remaining_moves
                    remaining_moves = 0
                else:
                    x, y = x + dx * max_move, y + dy * max_move
                    dx, dy = -dx, -dy
                    remaining_moves -= max_move

            if new_matrix[y][x] < size:
                if new_matrix[y][x] in new_sharks.keys():
                    del new_sharks[new_matrix[y][x]]
                new_matrix[y][x] = size
                new_sharks[size] = ((x, y), speed, (dx, dy))

        self.matrix, self.sharks = new_matrix, new_sharks


if __name__ == "__main__":
    Problem().solve()
