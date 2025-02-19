import sys
from collections import Counter

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.a_size, self.a = int(read()), list(map(int, read().split()))
        self.b_size, self.b = int(read()), list(map(int, read().split()))

    def solve(self) -> None:
        a_cached, b_cached = Counter(), Counter()

        for left in range(self.a_size):
            for right in range(left, self.a_size):
                a_cached[sum(self.a[left : right + 1])] += 1

        for left in range(self.b_size):
            for right in range(left, self.b_size):
                b_cached[sum(self.b[left : right + 1])] += 1

        count = 0
        for a in a_cached.keys():
            count += a_cached[a] * b_cached[self.n - a]

        print(count)


if __name__ == "__main__":
    Problem().solve()
