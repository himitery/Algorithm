case = int(input())

for i in range(case):
    p, a, b = list(map(int, input().split()))

    count = [a, b]
    for j in range(2):
        l, r = (1, p)
        target = count[j]
        count[j] = 0
        while True:
            c = int((l+r)/2)
            if c == target:
                break
            elif c < target:
                l = c
            else:
                r = c
            count[j] += 1

    if count[0] == count[1]:
        result = 0
    elif count[0] < count[1]:
        result = "A"
    else:
        result = "B"

    print(f"#{i+1} {result}")
