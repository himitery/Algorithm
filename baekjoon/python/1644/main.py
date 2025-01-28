import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.num = int(read())

    def solve(self) -> None:
        decimal = self.find_decimal()

        print(self.find_cases(decimal))

    def find_cases(self, decimal: list[int]) -> int:
        if not decimal:
            return 0

        value, count, left, right = decimal[0], 0, 0, 0
        while left <= right < len(decimal):
            if value == self.num:
                count += 1

            if value > self.num or right + 1 == len(decimal):
                value -= decimal[left]
                left += 1
            else:
                right += 1
                value += decimal[right]

        return count

    def find_decimal(self) -> list[int]:
        if self.num < 2:
            return []

        cached = [num for num in range(self.num + 1)]

        for idx in range(2, self.num + 1):
            if cached[idx] == 0:
                continue

            for next_idx in range(idx * 2, self.num + 1, idx):
                cached[next_idx] = 0

        return list(filter(lambda x: x > 0, cached[2:]))


if __name__ == "__main__":
    Problem().solve()
