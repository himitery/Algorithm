case = int(input())

for i in range(case):
    n, m = list(map(int, input().split()))
    numList = list(map(int, input().split()))
    result = numList[m % n]
    print(f"#{i+1} {result}")