import re as expression
import sys

fast_input = sys.stdin.readline


def app() -> None:
    T: int = int(fast_input())

    for _ in range(T):
        data: str = input()
        reg = expression.compile("(100+1+|01)+")

        if reg.fullmatch(data):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    app()
