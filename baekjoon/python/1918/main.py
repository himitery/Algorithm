import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.data = read()
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    def solve(self) -> None:
        stack, output = [], ""

        for word in self.data:
            if word.isalpha():
                output += word
                continue

            if word == "(":
                stack.append(word)
            elif word == ")":
                while stack and stack[-1] != "(":
                    output += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != "(" and self.precedence[stack[-1]] >= self.precedence[word]:
                    output += stack.pop()
                stack.append(word)

        while stack:
            output += stack.pop()

        print(output)


if __name__ == "__main__":
    Problem().solve()
