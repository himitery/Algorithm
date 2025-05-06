import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.t, self.p = read(), read()
        self.n, self.m = len(self.t), len(self.p)

    def solve(self) -> None:
        result = self.kmp_search(self.get_prefix_table())

        print(len(result))
        print(" ".join(map(str, result)))

    def get_prefix_table(self) -> list[int]:
        prefix_table, y = [0] * self.m, 0

        for x in range(1, self.m):
            while y > 0 and self.p[x] != self.p[y]:
                y = prefix_table[y - 1]

            if self.p[x] == self.p[y]:
                y += 1
                prefix_table[x] = y

        return prefix_table

    def kmp_search(self, prefix_table: list[int]) -> list[int]:
        result, y = [], 0

        for x in range(self.n):
            while y > 0 and self.t[x] != self.p[y]:
                y = prefix_table[y - 1]

            if self.t[x] == self.p[y]:
                y += 1

                if y == self.m:
                    result.append(x - self.m + 2)
                    y = prefix_table[y - 1]

        return result


if __name__ == "__main__":
    Problem().solve()
