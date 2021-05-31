numList: list[int] = list()
for i in range(9):
    numList.append(int(input()))

print(max(numList))
print(numList.index(max(numList)) + 1)
