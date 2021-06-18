n: int = int(input())

stack: list[int] = list()
data: list[int] = [int(input()) for _ in range(n)]
result: list[str] = list()

index: int = 1
while index <= n:
    stack.append(index)
    result.append("+")
    while stack[-1] == data[0]:
        stack.pop()
        del data[0]
        result.append("-")
        if len(stack) == 0 or len(data) == 0:
            break
    index += 1

if len(data) == 0:
    print("\n".join(result))
else:
    print("NO")
