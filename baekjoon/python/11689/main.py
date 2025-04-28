import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        result, num = self.n, 2
        while num**2 <= self.n:
            if self.n % num == 0:
                while self.n % num == 0:
                    self.n //= num
                result -= result // num

            num += 1

        if self.n > 1:
            result -= result // self.n

        print(result)


if __name__ == "__main__":
    Problem().solve()
