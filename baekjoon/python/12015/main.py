import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        print(len(self.find_lis()))

    def find_lis(self) -> list[int]:
        lis = [self.data[0]]

        for num in self.data[1:]:
            if num > lis[-1]:
                lis.append(num)
            else:
                lis[self.binary_search(lis, num)] = num

        return lis

    def binary_search(self, lis: list[int], target: int) -> int:
        left, right = 0, len(lis)

        while left < right:
            mid = (left + right) // 2

            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid

        return right


if __name__ == "__main__":
    Problem().solve()
