import sys
from collections import deque, defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.h, self.w = map(int, read().split())
        self.matrix = [list(read()) for _ in range(self.h)]
        self.keys = (lambda x: set(x) if x[0] != "0" else set())(list(read()))

    def solve(self) -> None:
        count, entrance = 0, self.find_entrance()
        stack, doors, keys, visited = deque(entrance), defaultdict(set[tuple[int, int]]), self.keys, set(entrance)

        while stack:
            x, y = stack.pop()
            value = self.matrix[y][x]
            if value == "$":
                count += 1

            if "A" <= value <= "Z" and value.lower() not in keys:
                doors[value.lower()].add((x, y))
                continue

            if "a" <= value <= "z":
                keys.add(value)

                for door in doors[value]:
                    stack.append(door)
                doors[value] = set()

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy

                if (nx, ny) not in visited and 0 <= nx < self.w and 0 <= ny < self.h and self.matrix[ny][nx] != "*":
                    stack.append((nx, ny))
                    visited.add((nx, ny))

        print(count)

    def find_entrance(self) -> list[tuple[int, int]]:
        entrance = []
        for x in range(self.w):
            if self.matrix[0][x] != "*":
                entrance.append((x, 0))

            if self.matrix[-1][x] != "*":
                entrance.append((x, self.h - 1))

        for y in range(1, self.h - 1):
            if self.matrix[y][0] != "*":
                entrance.append((0, y))

            if self.matrix[y][-1] != "*":
                entrance.append((self.w - 1, y))

        return entrance


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
