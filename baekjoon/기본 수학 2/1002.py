import math

num: int = int(input())

for _ in range(num):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif (x2 - x1) ** 2 + (y2 - y1) ** 2 == (r1 + r2) ** 2:
        print(1)
    elif (x2 - x1) ** 2 + (y2 - y1) ** 2 > (r1 + r2) ** 2:
        print(0)
    else:
        if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + min(r1, r2) > max(r1, r2):
            print(2)
        elif math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + min(r1, r2) == max(r1, r2):
            print(1)
        else:
            print(0)
