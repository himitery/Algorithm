import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.k = map(int, read().split())
        self.times = list(map(int, read().split()))

        self.order, self.depth = defaultdict(list[int]), [0 for _ in range(self.n)]
        for _ in range(self.k):
            src, dest = map(int, read().split())
            self.order[src - 1].append(dest - 1)
            self.depth[dest - 1] += 1

        self.target = int(read()) - 1

    def solve(self) -> None:
        dp, queue = self.times[:], deque(
            list(filter(lambda num: self.depth[num] == 0, range(self.n)))
        )

        while queue:
            node = queue.popleft()

            for next_node in self.order[node]:
                dp[next_node] = max(dp[next_node], dp[node] + self.times[next_node])
                self.depth[next_node] -= 1

                if self.depth[next_node] == 0:
                    queue.append(next_node)

        print(dp[self.target])


if __name__ == "__main__":
    for _ in range(int(read())):
        Problem().solve()
