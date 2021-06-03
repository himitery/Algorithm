def numberOfPrimes(start: int, end: int) -> int:
    end += 1
    numList: list[int] = [True] * end
    for i in range(2, end // 2 + 1):
        if numList[i]:
            for j in range(i * 2, end, i):
                numList[j] = False

    result: int = 0
    for x in range(max(start + 1, 2), end):
        if numList[x]:
            result += 1
    return result


while True:
    num: int = int(input())
    if num == 0:
        break
    print(numberOfPrimes(num, num * 2))
