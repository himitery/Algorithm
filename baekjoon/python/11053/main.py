import bisect
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        lis = []
        for value in self.data:
            pos = bisect.bisect_left(lis, value)
            if pos == len(lis):
                lis.append(value)
            else:
                lis[pos] = value

        print(len(lis))


if __name__ == "__main__":
    Problem().solve()
