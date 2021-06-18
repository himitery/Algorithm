N: int = int(input())

result: list = ["" for _ in range(N)]


def draw(size: int, line: int = 0, isEmpty: bool = False) -> None:
    if size == 3:
        result[line] += "***" if isEmpty is False else " " * 3
        result[line + 1] += "* *" if isEmpty is False else " " * 3
        result[line + 2] += "***" if isEmpty is False else " " * 3
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1 or isEmpty is True:
                    draw(size // 3, 3 * (line + i), True)
                else:
                    draw(size // 3, 3 * (line + i), False)


draw(N)
print("\n".join(result))
