import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.cases = []

        while True:
            case = list(map(int, read().split()))
            if case[0] == 0:
                break

            self.cases.append(case[1:])

    def solve(self) -> None:
        for case in self.cases:
            stack, case, maximum, index = [], case + [0], 0, 0

            while index < len(case):
                if not stack or case[stack[-1]] <= case[index]:
                    stack.append(index)
                    index += 1
                else:
                    top = stack.pop()
                    width, height = index if not stack else index - stack[-1] - 1, case[top]
                    maximum = max(maximum, width * height)

            print(maximum)


if __name__ == "__main__":
    Problem().solve()
