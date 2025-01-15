import sys

read = lambda: sys.stdin.readline().rstrip()


class Node:
    def __init__(
        self,
        value: int,
        left=None,
        right=None,
    ):
        self.value = value
        self.left = left
        self.right = right


class Problem:
    def __init__(self):
        self.data = []

        while True:
            try:
                self.data.append(int(read()))
            except StopIteration:
                break
            except ValueError:
                break

    def solve(self) -> None:
        self.print_postorder_tree(self.make_preorder_tree())

    def make_preorder_tree(self) -> Node:
        head = Node(self.data[0])

        stack = [head]
        for value in self.data[1:]:
            node = Node(value)

            if value < stack[-1].value:
                stack[-1].left = node

            if value > stack[-1].value:
                parent = None
                while stack and stack[-1].value < value:
                    parent = stack.pop()
                parent.right = node

            stack.append(node)

        return head

    def print_postorder_tree(self, node: Node) -> None:
        stack, result = [node], []
        while stack:
            target = stack.pop()
            result.append(target.value)

            if target.left:
                stack.append(target.left)
            if target.right:
                stack.append(target.right)

        for value in reversed(result):
            print(value)


if __name__ == "__main__":
    Problem().solve()
