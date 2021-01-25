case = int(input())

for i in range(case):
    n = int(input())
    numberList = list(map(int, input().split()))
    numberList.sort()
    result = []

    for j in range(min(n, 10)):
        if j % 2 != 0:
            result.append(numberList[0])
            del numberList[0]
        else:
            result.append(numberList[-1])
            del numberList[-1]

    print(f"#{i+1} {' '.join(list(map(str, result)))}")
