N: int = int(input())

count: int = 1
result: list[int] = [666]
data: int = result[-1]
while count < N:
    data += 1
    if "666" in str(data):
        result.append(data)
        count += 1
print(result[-1])
