A, B, C = list(map(int, input().split()))
print(A // (C - B) + 1 if C > B else -1)
