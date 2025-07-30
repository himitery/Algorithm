import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.tree = defaultdict(tuple[str, str])

        for node, left, right in [read().split() for _ in range(self.n)]:
            self.tree[node] = (left, right)

    def solve(self) -> None:
        print(self.preorder("A"), self.inorder("A"), self.postorder("A"), sep="\n")

    def preorder(self, node: str) -> str:
        if node == ".":
            return ""

        (left, right) = self.tree[node]

        return node + self.preorder(left) + self.preorder(right)

    def inorder(self, node: str) -> str:
        if node == ".":
            return ""

        (left, right) = self.tree[node]

        return self.inorder(left) + node + self.inorder(right)

    def postorder(self, node: str) -> str:
        if node == ".":
            return ""

        (left, right) = self.tree[node]

        return self.postorder(left) + self.postorder(right) + node


if __name__ == "__main__":
    Problem().solve()
