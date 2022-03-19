import sys

fast_input = sys.stdin.readline


def app() -> None:
    string: str = fast_input().split("\n")[0]

    data: list[str] = [""]
    for value in string:
        if value in ["+", "-"]:
            data.append("" if value == "+" else value)
            continue
        data[-1] += value

    result: int = 0
    sign: int = 1
    for num in list(map(int, data)):
        if num < 0:
            sign = -1
        result += abs(num) * sign
    print(result)


if __name__ == "__main__":
    app()
