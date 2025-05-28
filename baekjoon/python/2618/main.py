import itertools
import math
import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.w = int(read()), int(read())
        self.coords = [(0, 0)]
        for _ in range(self.w):
            y, x = map(int, read().split())
            self.coords.append((x - 1, y - 1))

    def solve(self) -> None:
        dp, path, parent = (
            [[math.inf for _ in range(self.w + 1)] for _ in range(self.w + 1)],
            [[0 for _ in range(self.w + 1)] for _ in range(self.w + 1)],
            [[(0, 0)] * (self.w + 1) for _ in range(self.w + 1)],
        )
        dp[0][0] = 0

        for x, y in itertools.product(range(self.w + 1), repeat=2):
            event = max(x, y) + 1
            if event > self.w:
                continue

            cost_x = dp[x][y] + self.calc_distance((0, 0) if x == 0 else self.coords[x], event)
            if cost_x < dp[event][y]:
                dp[event][y], path[event][y], parent[event][y] = cost_x, 1, (x, y)

            cost_y = dp[x][y] + self.calc_distance((self.n - 1, self.n - 1) if y == 0 else self.coords[y], event)
            if cost_y < dp[x][event]:
                dp[x][event], path[x][event], parent[x][event] = cost_y, 2, (x, y)

        minimum, x, y = math.inf, 0, 0
        for idx in range(self.w + 1):
            if dp[idx][self.w] < minimum:
                minimum, x, y = dp[idx][self.w], idx, self.w
            if dp[self.w][idx] < minimum:
                minimum, x, y = dp[self.w][idx], self.w, idx

        sequence = []
        for _ in range(self.w):
            sequence.append(path[x][y])
            x, y = parent[x][y]

        print(minimum)
        print(*reversed(sequence), sep="\n")

    def calc_distance(self, src: tuple[int, int], dist_idx: int) -> int:
        return abs(src[0] - self.coords[dist_idx][0]) + abs(src[1] - self.coords[dist_idx][1])


if __name__ == "__main__":
    Problem().solve()
