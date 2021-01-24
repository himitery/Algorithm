case = int(input())

for i in range(case):
    n, m = list(map(int, input().split()))
    numberList = list(map(int, input().split()))

    sumList = list()
    for j in range(n-m+1):
        sumList.append(sum(numberList[j:j+m]))

    print(f"#{i+1} {max(sumList) - min(sumList)}")
