def app() -> None:
    n: int = int(input())
    data: list[list[int]] = [list(map(int, list(input()))) for _ in range(n)]

    group: list[int] = []
    visited: list[tuple[int:int]] = []
    for row in range(n):
        for col in range(n):
            if (row, col) not in visited and data[row][col] != 0:
                group.append(0)

                queue: list[tuple[int:int]] = [(row, col)]
                while len(queue) != 0:
                    target_row, target_col = queue.pop(0)
                    visited.append((target_row, target_col))
                    group[-1] += 1

                    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if (
                            0 <= target_row + y < n and 0 <= target_col + x < n
                        ) and (
                            data[target_row + y][target_col + x] == 1
                            and (target_row + y, target_col + x) not in visited
                            and (target_row + y, target_col + x) not in queue
                        ):
                            queue.append((target_row + y, target_col + x))

    print(len(group))
    print("\n".join(list(map(str, sorted(group)))))


if __name__ == "__main__":
    app()
