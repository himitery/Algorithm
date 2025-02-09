import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.switches = list(map(int, read().split()))

        self.m = int(read())
        self.students = []

        for _ in range(self.m):
            sex, num = map(int, read().split())
            self.students.append((sex, num - 1))

    def solve(self) -> None:
        switches = self.switches[:]

        for sex, num in self.students:
            if sex == 1:
                for idx in range(num, self.n, num + 1):
                    switches[idx] = 1 - switches[idx]

            if sex == 2:
                left, right = num, num
                while left >= 0 and right < self.n:
                    if switches[left] != switches[right]:
                        break

                    switches[left], switches[right] = 1 - switches[left], 1 - switches[right]
                    left, right = left - 1, right + 1

        for idx in range(0, self.n, 20):
            print(*switches[idx : min(self.n, idx + 20)])


if __name__ == "__main__":
    Problem().solve()
