bracket = ["(", "{", "[", "]", "}", ")"]
case = int(input())

for i in range(case):
    str = input()

    stack = []
    for c in str:
        if c in bracket[:3]:
            stack.append(c)
        elif c in bracket[3:]:
            if len(stack) != 0 and c == bracket[5 - bracket.index(stack[-1])]:
                del stack[-1]
            else:
                stack = [False]
                break
    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f"#{i+1} {result}")

