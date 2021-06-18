N: int = int(input())

alphaList: list[str] = list()
for _ in range(N):
    alphaList.append(input())

alphaList = list(set(alphaList))
alphaList.sort()
alphaList.sort(key=len)

print("\n".join(alphaList))
