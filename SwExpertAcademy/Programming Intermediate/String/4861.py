case = int(input())

for i in range(case):
    n, m = list(map(int, input().split()))

    str = list()
    for _ in range(n):
        inputStr = input()
        str.append([x for x in inputStr])

    subStrList = list()
    for j in range(n):
        for k in range(n-m+1):
            subStrList.append(str[j][k:k+m])
            verticality = []
            for l in range(m):
                verticality.append(str[k+l][j])
            subStrList.append(verticality)

    result = None
    for subStr in subStrList:
        for j in range(int(m/2)):
            if subStr[j] != subStr[-1-j]:
                break
            if j == int(m/2) - 1:
                result = "".join(subStr)
        if result is not None:
            break

    print(f"#{i+1} {result}")

