num: int = int(input())

result: int = 0
while num > 0:
    num -= result * 6 if result != 0 else 1
    result += 1
print(result)
