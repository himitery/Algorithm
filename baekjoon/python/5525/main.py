import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = int(read()), int(read())
        self.data = list(map(lambda x: 0 if x == "O" else 1, list(input())))

    def solve(self) -> None:
        count, left, right = 0, 0, 0

        while left < self.m:
            if self.data[left] != 1:
                left += 1
                continue

            right = left
            while right < self.m and self.data[right] == 1 - (right - left) % 2:
                right += 1

            if right - left > self.n * 2:
                count += ((right - left - (right - left - 1) % 2) - (self.n * 2) + 1) // 2

            left = right

        print(count)


if __name__ == "__main__":
    Problem().solve()
