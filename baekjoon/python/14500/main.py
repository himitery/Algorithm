import itertools
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.matrix = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        maximum = 0
        for x, y in itertools.product(range(self.m), range(self.n)):
            maximum = max(
                maximum,
                self.find_normal_maximum(x, y),
            )

            maximum = max(
                maximum,
                self.find_special_maximum(x, y),
            )

        print(maximum)

    def find_normal_maximum(self, start_x: int, start_y: int) -> int:
        stack, maximum = [((start_x, start_y), 1, self.matrix[start_y][start_x], {(start_x, start_y)})], 0

        while stack:
            (x, y), current_depth, current_sum, visited = stack.pop()
            if current_depth == 4:
                if current_sum > maximum:
                    maximum = current_sum
                continue

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.m and 0 <= ny < self.n and (nx, ny) not in visited:
                    stack.append(
                        (
                            (nx, ny),
                            current_depth + 1,
                            current_sum + self.matrix[ny][nx],
                            visited | {(nx, ny)},
                        )
                    )

        return maximum

    def find_special_maximum(self, start_x: int, start_y: int) -> int:
        candidates = []
        for shape in [
            [(0, 0), (0, 1), (0, 2), (-1, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 1)],
            [(0, 0), (1, 0), (2, 0), (1, 1)],
            [(0, 0), (1, 0), (2, 0), (1, -1)],
        ]:
            total, is_valid = 0, True
            for dy, dx in shape:
                nx, ny = start_x + dx, start_y + dy
                if not (0 <= ny < self.n and 0 <= nx < self.m):
                    is_valid = False
                    break

                total += self.matrix[ny][nx]

            if is_valid:
                candidates.append(total)

        return max(candidates or [0])


if __name__ == "__main__":
    Problem().solve()
