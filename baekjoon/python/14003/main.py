import bisect
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = list(map(int, read().split()))

    def solve(self) -> None:
        lis = self.find_lis()

        print(len(lis))
        print(*lis)

    def find_lis(self) -> list[int]:
        lis, indices, parent = [], [], [-1] * self.n

        for idx, num in enumerate(self.data):
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
                indices.append(idx)
            else:
                lis[pos] = num
                indices[pos] = idx

            if pos > 0:
                parent[idx] = indices[pos - 1]

        return self.trace(indices[-1], parent)

    def trace(self, last_index: int, parent: list[int]) -> list[int]:
        result, idx = [], last_index

        while idx != -1:
            result.append(self.data[idx])
            idx = parent[idx]

        return result[::-1]


if __name__ == "__main__":
    Problem().solve()
