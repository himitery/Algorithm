import sys
from collections import defaultdict, deque

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n, self.m = map(int, read().split())
        self.data = defaultdict(list)
        self.weights = [0 for _ in range(self.n + 1)]

        for _ in range(self.m):
            values = list(map(int, read().split()))
            for idx in range(2, values[0] + 1):
                self.data[values[idx]].append(values[idx - 1])
                self.weights[values[idx - 1]] += 1

    def solve(self) -> None:
        print(*self.topology_sort(), sep="\n")

    def topology_sort(self) -> list[int]:
        queue, sequence = (
            deque(filter(lambda x: self.weights[x] == 0, range(1, self.n + 1))),
            [],
        )

        while queue:
            num = queue.popleft()
            if num in sequence:
                continue

            sequence.append(num)

            for next_num in self.data[num][-1::-1]:
                self.weights[next_num] -= 1
                if self.weights[next_num] == 0:
                    queue.append(next_num)

        return sequence[-1::-1] if len(sequence) == self.n else [0]


if __name__ == "__main__":
    Problem().solve()
