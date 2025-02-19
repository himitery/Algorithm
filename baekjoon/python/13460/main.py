import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = [list(read()) for _ in range(self.n)]

    def solve(self) -> None:
        print(self.find_escape(*self.find_elements()))

    def find_elements(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        red, blue, whole = (-1, -1), (-1, -1), (-1, -1)

        for y in range(self.n):
            for x in range(self.m):
                if self.data[y][x] == "R":
                    red = (x, y)
                if self.data[y][x] == "B":
                    blue = (x, y)
                if self.data[y][x] == "O":
                    whole = (x, y)

        return red, blue, whole

    def find_escape(self, red: tuple[int, int], blue: tuple[int, int], whole: tuple[int, int]) -> int:
        queue, visited = deque([(0, red, blue)]), {(red, blue)}

        while queue:
            count, red, blue = queue.popleft()
            if count >= 10:
                break

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                d_red, (new_red_x, new_red_y) = self.move(*red, dx, dy)
                d_blue, (new_blue_x, new_blue_y) = self.move(*blue, dx, dy)

                if (new_blue_x, new_blue_y) == whole:
                    continue

                if (new_red_x, new_red_y) == whole:
                    return count + 1

                if (new_red_x, new_red_y) == (new_blue_x, new_blue_y):
                    if d_red > d_blue:
                        new_red_x, new_red_y = new_red_x - dx, new_red_y - dy
                    else:
                        new_blue_x, new_blue_y = new_blue_x - dx, new_blue_y - dy

                if ((new_red_x, new_red_y), (new_blue_x, new_blue_y)) in visited:
                    continue

                queue.append((count + 1, (new_red_x, new_red_y), (new_blue_x, new_blue_y)))
                visited.add(((new_red_x, new_red_y), (new_blue_x, new_blue_y)))

        return -1

    def move(self, x: int, y: int, dx: int, dy: int) -> tuple[int, tuple[int, int]]:
        move_count = 0
        while self.data[y + dy][x + dx] != "#" and self.data[y][x] != "O":
            x, y, move_count = x + dx, y + dy, move_count + 1

        return move_count, (x, y)


if __name__ == "__main__":
    Problem().solve()
