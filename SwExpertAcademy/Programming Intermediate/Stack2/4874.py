case = int(input())

for i in range(case):
    str = input().split(".")[0].split()

    stack = list()
    for c in str:
        if c.isdigit():
            stack.append(c)
        elif len(stack) >= 2:
            op1 = int(stack[-2])
            op2 = int(stack[-1])

            result = None
            if c == "+":
                result = op1 + op2
            elif c == "-":
                result = op1 - op2
            elif c == "*":
                result = op1 * op2
            elif c == "/":
                result = int(op1 / op2)


            del stack[-1]
            del stack[-1]
            stack.append(result)
        else:
            stack = []
            break

    print(f"#{i+1}", stack[-1] if len(stack) == 1 else "error")
    

