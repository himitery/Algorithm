numList: list[int] = range(1, 10000)


def d(n: int) -> int:
    result: int = n
    while n != 0:
        result += n % 10
        n = n // 10
    return result


removeList: set[int] = set()
for num in numList:
    removeList.add(d(num))

print("\n".join(list(map(str, sorted(list(set(numList) - removeList))))))
