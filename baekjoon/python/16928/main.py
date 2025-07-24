import sys
from collections import deque, defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())

        self.moves = defaultdict(int)
        for start, end in [map(int, read().split()) for _ in range(self.n + self.m)]:
            self.moves[start] = end

    def solve(self) -> None:
        print(self.bfs())

    def bfs(self) -> int:
        queue, board = deque([1]), [0] * 101

        while queue:
            pos = queue.popleft()
            if pos == 100:
                return board[pos]

            for dice in range(1, 7):
                next_pos = pos + dice
                if next_pos > 100:
                    continue

                if next_pos in self.moves:
                    next_pos = self.moves[next_pos]

                if board[next_pos] == 0:
                    board[next_pos] = board[pos] + 1
                    queue.append(next_pos)

        return -1


if __name__ == "__main__":
    Problem().solve()
