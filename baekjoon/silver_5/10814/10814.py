import sys

fast_input = sys.stdin.readline
fast_output = sys.stdout.write


def app() -> None:
    N: int = int(fast_input())

    data: list[dict] = list()
    for index in range(N):
        value = fast_input().split()

        new_data: dict = dict()
        new_data["index"] = index
        new_data["age"] = int(value[0])
        new_data["name"] = value[1]

        data.append(new_data)

    for value in sorted(data, key=lambda x: (x["age"], x["index"])):
        fast_output(f"{value['age']} {value['name']}\n")


if __name__ == "__main__":
    app()
