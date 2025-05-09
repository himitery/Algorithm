import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = sorted(list(map(int, read().split())))

        self.mod = 1_000_000_007

    def solve(self) -> None:
        cached = [1 for _ in range(self.n)]
        for idx in range(1, self.n):
            cached[idx] = (cached[idx - 1] * 2) % self.mod

        answer = 0
        for idx in range(self.n):
            answer += self.data[idx] * (cached[idx] - cached[self.n - idx - 1])
            answer %= self.mod

        print(answer)


if __name__ == "__main__":
    Problem().solve()
