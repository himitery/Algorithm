import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.a, self.b = list(map(int, read().split())), list(map(int, read().split()))

        self.tree = [0] * (self.n + 1)

    def solve(self) -> None:
        pos_b, crossings = {machine_id: idx for idx, machine_id in enumerate(self.b)}, 0

        for idx in range(self.n):
            b_index = pos_b[self.a[idx]]
            crossings += self.query(self.n - 1) - self.query(b_index)

            self.update(b_index, 1)

        print(crossings)

    def update(self, idx: int, value: int) -> None:
        idx += 1
        while idx <= self.n:
            self.tree[idx] += value
            idx += idx & -idx

    def query(self, idx: int) -> int:
        idx, value = idx + 1, 0
        while idx > 0:
            value += self.tree[idx]
            idx -= idx & -idx

        return value


if __name__ == "__main__":
    Problem().solve()
