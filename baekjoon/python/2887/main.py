import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.planets = []

        for idx in range(self.n):
            x, y, z = map(int, read().split())
            self.planets.append((idx, x, y, z))

        self.roots = [x for x in range(self.n)]

    def solve(self) -> None:
        print(self.find_minimum_cost())

    def find_minimum_cost(self) -> int:
        edges, weight = self.find_edges(), 0

        for distance, src, dest in edges:
            if self.union(src, dest):
                weight += distance

        return weight

    def find_edges(self) -> list[tuple[int, int, int]]:
        edges = []
        for axis in range(1, 4):
            self.planets.sort(key=lambda planet: planet[axis])

            for idx in range(self.n - 1):
                edges.append(
                    (
                        abs(self.planets[idx][axis] - self.planets[idx + 1][axis]),
                        self.planets[idx][0],
                        self.planets[idx + 1][0],
                    )
                )

        return sorted(edges)

    def union(self, src: int, dest: int) -> bool:
        src_root, dest_root = self.find_root(src), self.find_root(dest)
        if src_root == dest_root:
            return False

        self.roots[src_root] = dest_root
        return True

    def find_root(self, num: int) -> int:
        while num != self.roots[num]:
            self.roots[num] = self.roots[self.roots[num]]
            num = self.roots[num]

        return num


if __name__ == "__main__":
    Problem().solve()
