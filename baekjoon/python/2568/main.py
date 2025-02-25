import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = sorted([tuple(map(int, read().split())) for _ in range(self.n)], key=lambda x: x[0])

    def solve(self) -> None:
        lis = self.find_lis()
        deleted = self.find_deleted(lis)

        print(len(deleted))
        print(*deleted, sep="\n")

    def find_lis(self) -> list[int]:
        lis, indexes, parent = [], [], [-1 for _ in range(self.n)]

        for idx, (_, num) in enumerate(self.data):
            pos = self.binary_search(lis, num)
            if pos == len(lis):
                lis.append(num)
                indexes.append(idx)
            else:
                lis[pos] = num
                indexes[pos] = idx

            if pos != 0:
                parent[idx] = indexes[pos - 1]

        return self.trace(parent, indexes[-1])

    def binary_search(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def trace(self, parent: list[int], idx: int) -> list[int]:
        results = []

        while idx != -1:
            results.append(self.data[idx][0])
            idx = parent[idx]

        return results

    def find_deleted(self, lis: list[int]) -> list[int]:
        return sorted(list(set(map(lambda x: x[0], self.data)) - set(lis)))


if __name__ == "__main__":
    Problem().solve()
