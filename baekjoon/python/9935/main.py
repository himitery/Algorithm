import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.data = read()
        self.bomb = read()

    def solve(self) -> None:
        stack = []
        for char in self.data:
            stack.append(char)
            if (
                len(stack) >= len(self.bomb)
                and "".join(stack[-len(self.bomb) :]) == self.bomb
            ):
                del stack[-len(self.bomb) :]

        print("".join(stack) or "FRULA")


if __name__ == "__main__":
    Problem().solve()
