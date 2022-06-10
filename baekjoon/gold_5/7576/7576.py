import sys

fast_input = sys.stdin.readline


def app() -> None:
    M, N = tuple(map(int, fast_input().split()))
    tomato: list[list[int]] = [
        list(map(int, fast_input().split())) for _ in range(N)
    ]

    empty: int = 0
    visited: int = 0
    queue: list[tuple[int, int]] = list()
    for row in range(N):
        for col in range(M):
            if tomato[row][col] == 1:
                queue.append((col, row))
                visited += 1
            elif tomato[row][col] == -1:
                empty += 1

    x_index: list[int] = [-1, 1, 0, 0]
    y_index: list[int] = [0, 0, -1, 1]

    day: int = 0
    while queue and (visited + empty) < M * N:
        new_queue: list[tuple[int, int]] = list()
        for (x, y) in queue:
            for index in range(4):
                plus_x: int = x_index[index]
                plus_y: int = y_index[index]
                if (
                    0 <= x + plus_x < M
                    and 0 <= y + plus_y < N
                    and tomato[y + plus_y][x + plus_x] == 0
                ):
                    tomato[y + plus_y][x + plus_x] = 1
                    new_queue.append((x + plus_x, y + plus_y))
                    visited += 1
        queue = new_queue
        day += 1

    if (visited + empty) != M * N:
        print(-1)
    else:
        print(day)


if __name__ == "__main__":
    app()
