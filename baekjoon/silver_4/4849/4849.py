import sys

fast_input = sys.stdin.readline
fast_output = sys.stdout.write


def check_data(data: str) -> bool:
    stack: list[str] = list()
    for value in data:
        if value == "[" or value == "(":
            stack.append(value)
        elif value == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return False
        elif value == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False
    return len(stack) == 0


def app() -> None:
    while True:
        data: str = input()
        if data == ".":
            return

        fast_output(f"{'yes' if check_data(data) else 'no'}\n")


if __name__ == "__main__":
    app()
