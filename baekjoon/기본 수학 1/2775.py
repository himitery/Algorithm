num: int = int(input())


for _ in range(num):
    k = int(input())
    n = int(input())

    people: list[int] = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]

    print(people[-1])
