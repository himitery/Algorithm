import sys
from collections import defaultdict, deque
from typing import cast

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.data = [read().split()[1:] for _ in range(self.n)]

    def solve(self) -> None:
        tree, root = self.make_tree()
        stack, visited = deque([cast(tuple[str, ...], (x,)) for x in sorted(root, reverse=True)]), set()

        while stack:
            key = stack.pop()
            if key in visited:
                continue

            visited.add(key)
            print("--" * (len(key) - 1), key[-1], sep="")

            for child in sorted(tree[key], reverse=True):
                stack.append(key + (child,))

    def make_tree(self) -> tuple[dict[tuple[str, ...], list[str]], set[str]]:
        tree, root = defaultdict(list[str]), set()

        for line in self.data:
            root.add(line[0])
            for idx in range(len(line) - 1):
                tree[tuple(line[: idx + 1])].append(line[idx + 1])

        return tree, root


if __name__ == "__main__":
    Problem().solve()
