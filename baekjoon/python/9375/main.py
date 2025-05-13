import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = defaultdict(set[str])
        for _ in range(self.n):
            name, costume_type = read().split()
            self.data[costume_type].add(name)

    def solve(self) -> None:
        result = 1
        for item in self.data.values():
            result *= len(item) + 1

        print(result - 1)


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
