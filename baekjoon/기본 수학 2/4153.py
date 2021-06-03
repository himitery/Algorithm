while True:
    numList: list[int] = list(map(int, input().split()))
    if numList == [0, 0, 0]:
        break

    maxNum: int = numList.pop(numList.index(max(numList)))
    if maxNum ** 2 == sum([x ** 2 for x in numList]):
        print("right")
    else:
        print("wrong")
