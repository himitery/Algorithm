import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.n_data = list(map(int, read().split()))

        self.m = int(read())
        self.m_data = list(map(int, read().split()))

    def solve(self) -> None:
        n, m, res = 0, 0, []
        while n < self.n and m < self.m:
            next_n, next_m, maximum = self.n, self.m, -1

            for idx_n in range(n, self.n):
                for idx_m in range(m, self.m):
                    if (
                        self.n_data[idx_n] == self.m_data[idx_m]
                        and self.n_data[idx_n] > maximum
                    ):
                        next_n, next_m, maximum = (
                            idx_n + 1,
                            idx_m + 1,
                            self.n_data[idx_n],
                        )

            if maximum == -1:
                break

            res.append(maximum)
            n, m = next_n, next_m

        print(len(res))
        print(*res)


if __name__ == "__main__":
    Problem().solve()
