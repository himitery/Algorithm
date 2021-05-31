numList: list[int] = list()
for i in range(3):
    numList.append(int(input()))

mul: int = 1
for num in numList:
    mul *= num

result: list[any] = [0 for x in range(10)]
while mul != 0:
    r: int = mul % 10
    mul = mul // 10
    result[r] += 1

result = list(map(str, result))
print("\n".join(result))
