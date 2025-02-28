import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m, self.k = map(int, read().split())
        self.candies = {idx: candy for idx, candy in enumerate(map(int, read().split()))}
        self.friends = {idx: [] for idx in range(self.n)}

        for _ in range(self.m):
            x, y = map(int, read().split())
            self.friends[x - 1].append(y - 1)
            self.friends[y - 1].append(x - 1)

    def solve(self) -> None:
        print(self.backtrack(self.find_group()))

    def find_group(self) -> list[tuple[int, int]]:
        groups, visited = [], set()

        for person in range(self.n):
            if person in visited:
                continue

            visited.add(person)

            queue, group, candies = deque([person]), 1, self.candies[person]
            while queue:
                for friend in self.friends[queue.popleft()]:
                    if not friend in visited:
                        queue.append(friend)
                        visited.add(friend)
                        group, candies = group + 1, candies + self.candies[friend]

            groups.append((group, candies))

        return sorted(groups)

    def backtrack(self, group: list[tuple[int, int]]) -> int:
        dp = [0] * self.k

        for members, candies in group:
            if members >= self.k:
                continue

            for idx in range(self.k - 1, members - 1, -1):
                dp[idx] = max(dp[idx], dp[idx - members] + candies)

        return dp[-1]


if __name__ == "__main__":
    Problem().solve()
