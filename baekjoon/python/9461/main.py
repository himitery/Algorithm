import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())

    def solve(self) -> None:
        nums = [1, 1, 1, 2, 2]

        for num in range(5, self.n):
            nums.append(nums[num - 1] + nums[num - 5])

        print(nums[self.n - 1])


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
