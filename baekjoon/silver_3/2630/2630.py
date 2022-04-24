import sys

fast_input = sys.stdin.readline


def app() -> None:
    N: int = int(fast_input())
    paper: list[list[int]] = [
        list(map(int, fast_input().split())) for _ in range(N)
    ]

    count: dict[int:int] = {0: 0, 1: 0}

    def getPaper(size: int, start_row: int, start_col):
        color: int = paper[start_row][start_col]
        for row in paper[start_row : start_row + size]:
            for col in row[start_col : start_col + size]:
                if col != color:
                    getPaper(size // 2, start_row, start_col)
                    getPaper(size // 2, start_row, start_col + size // 2)
                    getPaper(size // 2, start_row + size // 2, start_col)
                    getPaper(
                        size // 2, start_row + size // 2, start_col + size // 2
                    )
                    return
        count[color] += 1

    getPaper(N, 0, 0)

    print(count[0], count[1], sep="\n")


if __name__ == "__main__":
    app()
