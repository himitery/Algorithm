import sys

fast_input = sys.stdin.readline
fast_output = sys.stdout.write


def check_data(data: str) -> bool:
    stack: list[str] = list()
    for value in data:
        if value == "(":
            stack.append(value)
        elif value == ")" and (len(stack) == 0 or stack.pop() == value):
            return False
    return len(stack) == 0


def app() -> None:
    T: int = int(fast_input())

    for _ in range(T):
        fast_output(f"{'YES' if check_data(fast_input()) else 'NO'}\n")


if __name__ == "__main__":
    app()
