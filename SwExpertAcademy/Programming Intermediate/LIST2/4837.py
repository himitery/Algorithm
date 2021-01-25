case = int(input())
numberList = [x for x in range(1, 13)]

for i in range(case):
    n, k = list(map(int, input().split()))

    count = 0
    for j in range(1 << len(numberList)):
        part = list()
        for l in range(len(numberList)):
            if j & (1 << l):
                part.append(numberList[l])
        if len(part) == n and sum(part) == k:
            count += 1

    print(f"#{i+1} {count}")
