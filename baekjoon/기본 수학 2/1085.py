x, y, w, h = list(map(int, input().split()))

print(min(x, w - x, y, h - y))
