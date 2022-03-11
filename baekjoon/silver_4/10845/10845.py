import sys

fast_input = sys.stdin.readline


class Queue:
    class Node:
        def __init__(self, data: int, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.tail = None

    def push(self, data: int) -> None:
        node = self.Node(data, self.tail)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def pop(self) -> None:
        if self.head is not None:
            print(self.head.data)
            self.head = self.head.next
        else:
            print(-1)

        if self.head is None:
            self.tail = None

    def size(self) -> None:
        count: int = 0
        target_node = self.head
        while target_node is not None:
            target_node = target_node.next
            count += 1
        print(count)

    def empty(self) -> None:
        print(1 if self.head is None else 0)

    def front(self) -> None:
        print(-1 if self.head is None else self.head.data)

    def back(self) -> None:
        print(-1 if self.tail is None else self.tail.data)


def app() -> None:
    N: int = int(fast_input())

    queue = Queue()
    for _ in range(N):
        command: list[str] = fast_input().split()
        if command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()
        elif command[0] == "size":
            queue.size()
        elif command[0] == "empty":
            queue.empty()
        elif command[0] == "front":
            queue.front()
        elif command[0] == "back":
            queue.back()


if __name__ == "__main__":
    app()
