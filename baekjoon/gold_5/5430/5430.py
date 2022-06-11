import sys
from collections import deque

fast_input = sys.stdin.readline


def app() -> None:
    T: int = int(fast_input())

    for _ in range(T):
        execute: list[str] = list(fast_input().strip("\n"))
        n: int = int(fast_input())
        _data: list[str] = fast_input().strip("\n")[1:-1].split(",")
        data: deque[int] = deque(map(int, _data)) if n != 0 else deque()

        is_reversed: bool = False
        is_error: bool = False
        for cmd in execute:
            if cmd == "R":
                is_reversed = not is_reversed
            elif cmd == "D":
                if len(data) > 0:
                    if not is_reversed:
                        data.popleft()
                    else:
                        data.pop()
                else:
                    print("error")
                    is_error = True
                    break

        if not is_error:
            if is_reversed:
                data.reverse()
            print(f"[{','.join(list(map(str, data)))}]")


if __name__ == "__main__":
    app()
