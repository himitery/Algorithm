import sys
from collections import Counter

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.a, self.b, self.c, self.d = [], [], [], []

        for _ in range(self.n):
            a, b, c, d = map(int, read().split())

            self.a.append(a)
            self.b.append(b)
            self.c.append(c)
            self.d.append(d)

    def solve(self) -> None:
        ab = Counter([a + b for a in self.a for b in self.b])
        print(sum(ab[-c - d] for c in self.c for d in self.d))


if __name__ == "__main__":
    Problem().solve()
