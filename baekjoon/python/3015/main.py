import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.people = [int(read()) for _ in range(self.n)]

    def solve(self) -> None:
        stack, count = deque([]), 0

        for height in self.people:
            same_height_count = 1

            while stack and stack[-1][0] <= height:
                top_h, top_count = stack.pop()

                count += top_count
                if top_h == height:
                    same_height_count += top_count

            if stack:
                count += 1

            stack.append((height, same_height_count))

        print(count)


if __name__ == "__main__":
    Problem().solve()
