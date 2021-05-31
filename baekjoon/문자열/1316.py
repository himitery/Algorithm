num: int = int(input())

result: int = 0
for _ in range(num):
    data: str = input()
    usedAlpha: list[str] = list()
    for i in data:
        if i in usedAlpha and usedAlpha[-1] != i:
            result -= 1
            break
        usedAlpha.append(i)
    result += 1
print(result)
