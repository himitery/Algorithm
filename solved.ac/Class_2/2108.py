import sys
from collections import Counter

N: int = int(sys.stdin.readline())

numList: list[int] = list()
for _ in range(N):
    numList.append(int(sys.stdin.readline()))
numList.sort()

data: list[int] = Counter(numList).most_common()

print(int(round(sum(numList) / N, 0)))
print(numList[N // 2])
print(data[1][0] if data[0][1] == data[1][1] else data[0][0]) if len(
    data
) != 1 else print(data[0][0])
print(max(numList) - min(numList))
