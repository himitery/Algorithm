import math

num: int = int(input())

for _ in range(num):
    start, end = list(map(int, input().split()))

    if end - start == 1:
        print(1)
    else:
        count: int = 1
        while not (
            count ** 2 + 1 <= end - start and end - start < (count + 1) ** 2 + 1
        ):
            count += 1
        if count * (count + 1) + 1 > end - start:
            print(count * 2)
        else:
            print(count * 2 + 1)
