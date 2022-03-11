import sys

fast_input = sys.stdin.readline


class Node:
    def __init__(self, data: int, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


def app() -> None:
    N, K = list(map(int, fast_input().split()))

    head = target = Node(1, None, None)
    for value in range(2, N + 1):
        node = Node(value, target, None)
        target.next = node
        target = node
    target.next = head
    head.prev = target
    target = head

    result: list[str] = list()
    for _ in range(N):
        for _ in range(K - 1):
            target = target.next
        result.append(str(target.data))
        target.prev.next = target.next
        target.next.prev = target.prev
        target = target.next
    print(f"<{', '.join(result)}>")


if __name__ == "__main__":
    app()
