import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.known = set(map(int, read().split()[1:]))
        self.parties = [list(map(int, read().split()[1:])) for _ in range(self.m)]

        self.parent, self.rank = list(range(self.n + 1)), [0] * (self.n + 1)

    def solve(self) -> None:
        [self.union(party[0], person) for party in self.parties for person in party[1:]]

        truth = {self.find(person) for person in self.known}
        print(len([party for party in self.parties if all(self.find(person) not in truth for person in party)]))

    def find(self, person: int) -> int:
        if self.parent[person] != person:
            self.parent[person] = self.find(self.parent[person])

        return self.parent[person]

    def union(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root], self.rank[x_root] = x_root, 1


if __name__ == "__main__":
    Problem().solve()
