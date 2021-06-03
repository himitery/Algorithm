xList: list[int] = list()
yList: list[int] = list()

for _ in range(3):
    x, y = list(map(int, input().split()))
    xList.append(x) if x not in xList else xList.pop(xList.index(x))
    yList.append(y) if y not in yList else yList.pop(yList.index(y))
print(xList[0], yList[0])
