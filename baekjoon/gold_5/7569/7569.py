import sys

fast_input = sys.stdin.readline


def app() -> None:
    M, N, H = tuple(map(int, fast_input().split()))
    tomato: list[list[list[int]]] = list()

    queue: list[tuple[int, int, int]] = list()
    visited: int = 0
    empty: int = 0
    for z in range(H):
        box: list[list[int]] = list()
        for y in range(N):
            line: list[int] = list(map(int, fast_input().split()))
            for x in range(len(line)):
                if line[x] == 1:
                    queue.append((x, y, z))
                    visited += 1
                elif line[x] == -1:
                    empty += 1
            box.append(line)
        tomato.append(box)

    x_index: list[int] = [-1, 1, 0, 0, 0, 0]
    y_index: list[int] = [0, 0, -1, 1, 0, 0]
    z_index: list[int] = [0, 0, 0, 0, -1, 1]
    count: int = 0
    while queue and visited < M * N * H - empty:
        new_queue: list[tuple[int, int, int]] = list()
        for x, y, z in queue:
            for index in range(6):
                plus_x: int = x_index[index]
                plus_y: int = y_index[index]
                plus_z: int = z_index[index]

                if (
                    0 <= x + plus_x < M
                    and 0 <= y + plus_y < N
                    and 0 <= z + plus_z < H
                    and tomato[z + plus_z][y + plus_y][x + plus_x] == 0
                ):
                    tomato[z + plus_z][y + plus_y][x + plus_x] = 1
                    new_queue.append((x + plus_x, y + plus_y, z + plus_z))
                    visited += 1

        queue = new_queue
        count += 1

    if visited != M * N * H - empty:
        print(-1)
    else:
        print(count)


if __name__ == "__main__":
    app()
