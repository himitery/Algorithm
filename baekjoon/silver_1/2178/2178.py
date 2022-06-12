import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = tuple(map(int, fast_input().split()))
    data: list[list[int]] = [
        list(map(int, list(fast_input().rstrip("\n")))) for _ in range(N)
    ]

    queue: list[tuple[int, int]] = [(0, 0)]
    visited: list[tuple[int, int]] = [(0, 0)]
    depth: int = 0

    x_index: list[int] = [-1, 1, 0, 0]
    y_index: list[int] = [0, 0, -1, 1]
    while queue:
        depth += 1
        new_queue: list[tuple[int, int]] = list()
        for x, y in queue:
            if x + 1 == M and y + 1 == N:
                new_queue = list()
                break
            for index in range(4):
                plus_x, plus_y = x_index[index], y_index[index]
                if (
                    0 <= x + plus_x < M
                    and 0 <= y + plus_y < N
                    and data[y + plus_y][x + plus_x] == 1
                    and (x + plus_x, y + plus_y) not in visited
                ):
                    new_queue.append((x + plus_x, y + plus_y))
                    visited.append((x + plus_x, y + plus_y))
        queue = new_queue
    print(depth)


if __name__ == "__main__":
    app()
