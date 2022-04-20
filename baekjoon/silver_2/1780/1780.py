import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    data: list[list[int]] = [
        list(map(int, fast_input().split())) for _ in range(N)
    ]
    paper: dict[int:int] = {-1: 0, 0: 0, 1: 0}

    def isValid(size: int, start_row: int, start_col: int) -> bool:
        for row in data[start_row : start_row + size]:
            for value in row[start_col : start_col + size]:
                if value != data[start_row][start_col]:
                    return False
        return True

    def getPaper(size: int, start_row: int, start_col: int):
        if size == 1 or isValid(size, start_row, start_col):
            paper[data[start_row][start_col]] += 1
        else:
            for row in range(3):
                for col in range(3):
                    getPaper(
                        size // 3,
                        start_row + size // 3 * row,
                        start_col + size // 3 * col,
                    )

    getPaper(N, 0, 0)

    print(paper[-1])
    print(paper[0])
    print(paper[1])


if __name__ == "__main__":
    app()
