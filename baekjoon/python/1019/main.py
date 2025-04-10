import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.count = [0] * 10

    def solve(self) -> None:
        num, digit = self.n, 1

        while num > 0:
            while num % 10 != 9:
                self.count_digits(num, digit)
                num -= 1

            if num < 0:
                break

            for idx in range(10):
                self.count[idx] += (num // 10 + 1) * digit

            self.count[0] -= digit
            num //= 10
            digit *= 10

        print(*self.count)

    def count_digits(self, num: int, digit: int) -> None:
        while num > 0:
            self.count[num % 10] += digit
            num //= 10


if __name__ == "__main__":
    Problem().solve()
