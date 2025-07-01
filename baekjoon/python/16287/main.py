import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self) -> None:
        self.w, self.n = map(int, read().split())
        self.a = list(map(int, read().split()))

    def solve(self) -> None:
        sums_possible = [False] * (self.w + 1)

        for x in range(self.n):
            for y in range(x + 1, self.n):
                if self.w - self.a[x] - self.a[y] > 0 and sums_possible[self.w - self.a[x] - self.a[y]]:
                    print("YES")
                    return

            for y in range(x):
                if self.a[y] + self.a[x] < self.w:
                    sums_possible[self.a[y] + self.a[x]] = True

        print("NO")


if __name__ == "__main__":
    Problem().solve()
