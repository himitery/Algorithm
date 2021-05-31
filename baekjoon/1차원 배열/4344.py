C: int = int(input())

for i in range(C):
    data: list[int] = list(map(int, input().split()))[1:]
    moreThanAvg: int = len([x for x in data if x > sum(data) // len(data)])
    print("{:.3f}%".format(moreThanAvg / len(data) * 100))
