import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        dp = [[[0, 0, 0] for _ in range(self.n)] for _ in range(self.n)]
        dp[0][1][0] = 1

        for y in range(self.n):
            for x in range(1, self.n):
                if self.data[y][x] == 1:
                    continue

                if x > 0:
                    dp[y][x][0] += dp[y][x - 1][0]
                    dp[y][x][0] += dp[y][x - 1][1]

                if y > 0:
                    dp[y][x][2] += dp[y - 1][x][1]
                    dp[y][x][2] += dp[y - 1][x][2]

                if (
                    (x > 0 and y > 0)
                    and self.data[y - 1][x] == 0
                    and self.data[y][x - 1] == 0
                ):
                    dp[y][x][1] += dp[y - 1][x - 1][0]
                    dp[y][x][1] += dp[y - 1][x - 1][1]
                    dp[y][x][1] += dp[y - 1][x - 1][2]

        print(sum(dp[self.n - 1][self.n - 1]))

    def is_available(
        self,
        src: tuple[int, int],
        dest: tuple[int, int],
    ) -> bool:
        if dest[0] >= self.n or dest[1] >= self.n:
            return False

        if (
            src[0] != dest[0]
            and src[1] != dest[1]
            and (self.data[src[0]][dest[1]] == 1 or self.data[dest[0]][src[1]] == 1)
        ):
            return False

        return self.data[dest[0]][dest[1]] == 0


if __name__ == "__main__":
    Problem().solve()
