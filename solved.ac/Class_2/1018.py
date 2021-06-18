N, M = list(map(int, input().split()))
board: list[list[str]] = list()

line_1: list[str] = list(map(lambda x: "W" if x % 2 == 0 else "B", range(M)))
line_2: list[str] = list(map(lambda x: "W" if x % 2 != 0 else "B", range(M)))

case_1: list[list[str]] = list(
    map(lambda x: line_1 if x % 2 == 0 else line_2, range(N))
)
case_2: list[list[str]] = list(
    map(lambda x: line_1 if x % 2 != 0 else line_2, range(N))
)


def getSubBoard(board: list[list[str]], xStart: int, yStart: int) -> list[list[str]]:
    subBoard: list[list[str]] = list()
    for i in range(yStart, yStart + 8):
        subBoard.append([])
        for j in range(xStart, xStart + 8):
            subBoard[-1].append(board[i][j])
    return subBoard


def getMinCount(board: list[list[str]]) -> int:
    count_1: int = 0
    count_2: int = 0

    for i in range(8):
        for j in range(8):
            if case_1[i][j] != board[i][j]:
                count_1 += 1
            if case_2[i][j] != board[i][j]:
                count_2 += 1
    return min(count_1, count_2)


for _ in range(N):
    board.append(list(input()))

minCount: int = None
for i in range(N - 7):
    for j in range(M - 7):
        subBoard: list[list[str]] = getSubBoard(board, j, i)
        count = getMinCount(subBoard)
        if minCount is None or count < minCount:
            minCount = count


print(minCount)
