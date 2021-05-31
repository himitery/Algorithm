data: str = input().upper()
setData: list() = list(set(data))

result: list[int] = list()
for i in setData:
    result.append(data.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(setData[result.index(max(result))])
