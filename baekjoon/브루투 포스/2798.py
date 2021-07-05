import itertools

N, M = list(map(int, input().split()))
cardList: list[int] = list(map(int, input().split()))

data: list[int] = list(map(sum, itertools.permutations(cardList, 3)))

if M in data:
    print(M)
else:
    value: int = 0
    for d in data:
        if d > value and d < M:
            value = d
    print(value)
