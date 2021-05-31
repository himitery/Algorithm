import math

A, B, V = list(map(int, input().split()))
print(math.ceil((V - A) / (A - B)) + 1)
