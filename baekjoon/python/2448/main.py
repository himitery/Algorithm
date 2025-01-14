import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        for line in self.draw(self.n):
            print(line)

    def draw(self, size: int) -> list[str]:
        if size == 3:
            return ["  *  ", " * * ", "*****"]

        stars = self.draw(size // 2)
        top = [" " * (size // 2) + line + " " * (size // 2) for line in stars]
        bottom = [line + " " + line for line in stars]

        return top + bottom


if __name__ == "__main__":
    Problem().solve()
