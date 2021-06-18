K, N = list(map(int, input().split()))

length: list[int] = [int(input()) for _ in range(K)]
result: list[int] = [1, min(sum(length) // N, max(length))]
while result[0] <= result[1]:
    cut: int = sum(result) // 2
    if sum(list(map(lambda x: x // cut, length))) >= N:
        result[0] = cut + 1
    else:
        result[1] = cut - 1
print(result[1])
