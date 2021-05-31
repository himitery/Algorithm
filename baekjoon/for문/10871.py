N, X = list(map(int, input().split()))

numList = list(map(int, input().split()))
result = [str(num) for num in numList if num < X]

print(" ".join(result))
