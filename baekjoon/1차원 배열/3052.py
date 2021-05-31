numList: list[int] = list()
for i in range(10):
    numList.append(int(input()) % 42)
print(len(set(numList)))
