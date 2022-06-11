import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    data: list[list[int]] = [
        list(map(int, list(fast_input().strip("\n")))) for _ in range(N)
    ]

    def is_same(
        data: list[list[int]], size: int, start_row: int, start_col: int
    ) -> bool:
        for row in data[start_row : start_row + size]:
            for col in row[start_col : start_col + size]:
                if data[start_row][start_col] != col:
                    return False
        return True

    def compress(
        data: list[list[int]], size: int, start_row: int, start_col: int
    ) -> None:
        if is_same(data, size, start_row, start_col):
            print(data[start_row][start_col], end="")
        else:
            print("(", end="")
            compress(data, size // 2, start_row, start_col)
            compress(data, size // 2, start_row, start_col + size // 2)
            compress(data, size // 2, start_row + size // 2, start_col)
            compress(
                data, size // 2, start_row + size // 2, start_col + size // 2
            )
            print(")", end="")

    compress(data, N, 0, 0)
    print()


if __name__ == "__main__":
    app()
