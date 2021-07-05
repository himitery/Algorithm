case: int = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    important: list[int] = list(map(int, input().split()))

    if important.count(important[M]) == 1:
        print(list(map(lambda x: x > important[M], important)).count(True) + 1)
        continue

    index: int = 0
    page: list[bool] = [False if x != M else True for x in range(N)]
    while True:
        maxIndex: int = important.index(max(important))
        if page[maxIndex] is True:
            print(N - len(page) + 1)
            break

        important = important[maxIndex + 1 :] + important[:maxIndex]
        page = page[maxIndex + 1 :] + page[:maxIndex]
