sum: int = 0
for _ in range(4):
    sum += int(input())
print(sum // 60, sum % 60, sep="\n")
