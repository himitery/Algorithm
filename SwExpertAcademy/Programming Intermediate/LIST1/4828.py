case = int(input())

for i in range(case):
    int(input())

    numList = list(map(int, input().split()))
    print(f"#{i+1}", max(numList) - min(numList))