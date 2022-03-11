import sys

fast_input = sys.stdin.readline


class Deque:
    class Node:
        def __init__(self, data: int, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.tail = None

    def push_front(self, data: int) -> None:
        node = self.Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def push_back(self, data: int) -> None:
        node = self.Node(data, self.tail, None)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def pop_front(self) -> None:
        if self.head is None:
            print(-1)
            return

        print(self.head.data)
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

    def pop_back(self) -> None:
        if self.tail is None:
            print(-1)
            return

        print(self.tail.data)
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

    def size(self) -> None:
        count: int = 0
        target_node = self.head
        while target_node is not None:
            target_node = target_node.next
            count += 1
        print(count)

    def empty(self) -> None:
        print(1 if self.head is None and self.tail is None else 0)

    def front(self) -> None:
        print(-1 if self.head is None else self.head.data)

    def back(self) -> None:
        print(-1 if self.tail is None else self.tail.data)


def app() -> None:
    N: int = int(fast_input())

    deque = Deque()
    for _ in range(N):
        command = fast_input().split()
        if command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            deque.pop_front()
        elif command[0] == "pop_back":
            deque.pop_back()
        elif command[0] == "size":
            deque.size()
        elif command[0] == "empty":
            deque.empty()
        elif command[0] == "front":
            deque.front()
        elif command[0] == "back":
            deque.back()


if __name__ == "__main__":
    app()
