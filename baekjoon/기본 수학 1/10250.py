num: int = int(input())

for _ in range(num):
    H, W, N = list(map(int, input().split()))
    if N % H != 0:
        print("%d%02d" % (N % H, (N // H) + 1))
    else:
        print("%d%02d" % (H, N // H))
