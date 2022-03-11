import sys

fast_input = sys.stdin.readline


class Stack:
    class Node:
        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.head = None

    def push(self, data) -> None:
        node = self.Node(data, self.head)
        self.head = node

    def pop(self) -> None:
        if self.head is not None:
            print(self.head.data)
            self.head = self.head.prev
        else:
            print(-1)

    def size(self) -> None:
        count: int = 0
        target_node = self.head
        while target_node is not None:
            target_node = target_node.prev
            count += 1
        print(count)

    def empty(self) -> None:
        print("1" if self.head is None else "0")

    def top(self) -> None:
        print(-1 if self.head is None else self.head.data)


def app() -> None:
    N: int = int(fast_input())

    stack = Stack()
    for _ in range(N):
        command: list[str] = fast_input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "size":
            stack.size()
        elif command[0] == "empty":
            stack.empty()
        elif command[0] == "top":
            stack.top()


if __name__ == "__main__":
    app()
