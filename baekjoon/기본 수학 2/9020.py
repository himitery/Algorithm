num: int = int(input())


def getPrimeNumbers(end: int) -> list[int]:
    end += 1
    numList: list[int] = [True] * end
    for i in range(2, end // 2 + 1):
        if numList[i]:
            for j in range(i * 2, end, i):
                numList[j] = False
    return [i for i in range(2, end) if numList[i] is True]


def getFlag(target: int) -> list[int, int]:
    numList: list[int] = getPrimeNumbers(target)
    for i in range(
        numList.index(max([x for x in numList if x <= target // 2])), -1, -1
    ):
        if target - numList[i] in numList:
            return [
                min(target - numList[i], numList[i]),
                max(target - numList[i], numList[i]),
            ]


for _ in range(num):
    target: int = int(input())
    print(" ".join(list(map(str, getFlag(target)))))
