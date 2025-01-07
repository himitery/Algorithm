import sys
from collections import defaultdict

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.case: list[dict[str, list[str]]] = []
        for _ in range(int(read())):
            data: dict[str, list[str]] = defaultdict(list[str])
            for _ in range(int(read())):
                name, costume_type = read().split()
                data[costume_type].append(name)
            self.case.append(data)

    def solve(self) -> None:
        for case in self.case:
            result: int = 1
            number_of_items: list[int] = [len(case[key]) for key in case.keys()]

            for num in number_of_items:
                result *= num + 1

            print(result - 1)


if __name__ == "__main__":
    Problem().solve()
