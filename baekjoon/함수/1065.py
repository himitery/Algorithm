num: int = int(input())


def isFlag(numList: int) -> bool:
    diff: int = numList[1] - numList[0]
    for i in range(1, len(numList) - 1):
        if diff != numList[i + 1] - numList[i]:
            return False
    return True


if num < 100:
    print(num)
else:
    result = 99
    for i in range(100, num + 1):
        data: list[int] = list()
        while i != 0:
            data.append(i % 10)
            i = i // 10
        if isFlag(data):
            result += 1
    print(result)
