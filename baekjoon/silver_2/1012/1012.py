import sys

fast_input = sys.stdin.readline


def app() -> None:
    T: int = int(fast_input())

    for _ in range(T):
        M, N, K = list(map(int, fast_input().split()))
        data = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            x, y = list(map(int, fast_input().split()))
            data[y][x] = 1

        count: int = 0
        for row in range(N):
            for col in range(M):
                if data[row][col] == 1:
                    data[row][col] = 0

                    queue: list[list[int]] = [[col, row]]
                    while queue:
                        x, y = queue.pop(0)

                        if data[y][min(x + 1, M - 1)] == 1:
                            queue.append([x + 1, y])
                            data[y][min(x + 1, M - 1)] = 0
                        if data[y][max(x - 1, 0)] == 1:
                            queue.append([x - 1, y])
                            data[y][max(x - 1, 0)] = 0
                        if data[min(y + 1, N - 1)][x] == 1:
                            queue.append([x, y + 1])
                            data[min(y + 1, N - 1)][x] = 0
                        if data[max(y - 1, 0)][x] == 1:
                            queue.append([x, y - 1])
                            data[max(y - 1, 0)][x] = 0
                    count += 1

        print(count)


if __name__ == "__main__":
    app()
