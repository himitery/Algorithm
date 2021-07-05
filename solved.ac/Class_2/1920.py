input()
firstNumList: set[int] = set(map(int, input().split()))
input()
secondNumList: list[int] = list(map(int, input().split()))

for s in secondNumList:
    print(1 if s in firstNumList else 0)
