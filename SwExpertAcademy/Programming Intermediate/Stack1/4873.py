case = int(input())

for i in range(case):
    str = input()

    stack = []
    for c in str:
        if len(stack) != 0 and stack[-1] == c:
            del stack[-1]
        else:
            stack.append(c)
    print(f"#{i+1} {len(stack)}")
