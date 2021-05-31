num: int = int(input())
numList: list[int] = list(map(int, input().split()))
print(min(numList), max(numList))
