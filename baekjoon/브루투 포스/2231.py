N: int = int(input())

value: int = 0
for i in range(max(0, N - 9 * (len(str(N)))), N + 1):
    data: list = list(str(i))
    if (i + sum(list(map(int, data)))) == N:
        value = i
        break
print(value)
