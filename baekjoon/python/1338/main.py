import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.min_value, self.max_value = map(int, read().split())
        self.min_value, self.max_value = min(self.min_value, self.max_value), max(self.min_value, self.max_value)

        self.x, self.y = map(int, read().split())
        self.x = abs(self.x)

    def solve(self) -> None:
        value = self.find_value()

        if (
            not (0 <= self.y < self.x)
            or not (self.min_value <= value <= self.max_value)
            or value + self.x <= self.max_value
        ):
            print("Unknwon Number")
        else:
            print(value)

    def find_value(self) -> int:
        remind = self.min_value % self.x
        if remind <= self.y:
            return self.min_value + (self.y - remind)

        return self.min_value + (self.x - remind + self.y)


if __name__ == "__main__":
    Problem().solve()
