import sys

fast_input = sys.stdin.readline


def app() -> None:
    M: int = int(fast_input())

    data: set[int] = set()
    for _ in range(M):
        command: list[str] = fast_input().split()

        if command[0] == "add":
            data.add(int(command[1]))
        elif command[0] == "remove":
            if int(command[1]) in data:
                data.remove(int(command[1]))
        elif command[0] == "check":
            print(1 if int(command[1]) in data else 0)
        elif command[0] == "toggle":
            data.remove(int(command[1])) if int(
                command[1]
            ) in data else data.add(int(command[1]))
        elif command[0] == "all":
            data = set([x for x in range(1, 20 + 1)])
        elif command[0] == "empty":
            data.clear()


if __name__ == "__main__":
    app()
