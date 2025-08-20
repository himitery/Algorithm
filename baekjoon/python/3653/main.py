import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.movies = list(map(int, read().split()))

        self.tree = [0] * (self.n + self.m + 1)

    def solve(self) -> None:
        pos = [0] * (self.n + 1)
        for idx in range(1, self.n + 1):
            pos[idx] = self.m + idx - 1
            self.update(pos[idx], 1)

        result, top = [], self.m - 1
        for movie in self.movies:
            current = pos[movie]

            result.append(self.query(current - 1))

            self.update(current, -1)
            self.update(top, 1)

            pos[movie] = top
            top -= 1

        print(*result)

    def update(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        if index < 0:
            return 0

        index, num = index + 1, 0
        while index > 0:
            num += self.tree[index]
            index -= index & -index

        return num


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
