import sys
from collections import deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.board = [list(map(int, read().split())) for _ in range(self.n)]

    def solve(self) -> None:
        white_board, black_board = self.split_board()

        print(self.backtrack(white_board) + self.backtrack(black_board))

    def split_board(self) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        boards = ([], [])
        for y in range(self.n):
            for x in range(self.n):
                if self.board[y][x] == 0:
                    continue

                boards[abs(y - x) % 2].append((x, y))

        return boards

    def backtrack(self, board: list[tuple[int, int]]) -> int:
        stack, maximum = deque([(0, 0, 0, 0)]), 0

        while stack:
            idx, count, left_diag, right_diag = stack.pop()
            maximum = max(maximum, count)

            for next_idx in range(idx, len(board)):
                x, y = board[next_idx]
                left, right = 1 << (x + y), 1 << (y - x + self.n - 1)
                if left_diag & left or right_diag & right:
                    continue

                stack.append((next_idx + 1, count + 1, left_diag | left, right_diag | right))

        return maximum


if __name__ == "__main__":
    Problem().solve()
