N: int = int(input())

data: list[list[int, int]] = list()
for _ in range(N):
    data.append(list(map(int, input().split())))

for user in data:
    count: int = list(map(lambda x: x[0] > user[0] and x[1] > user[1], data)).count(
        True
    )
    print(count + 1, end=" ")
print()
