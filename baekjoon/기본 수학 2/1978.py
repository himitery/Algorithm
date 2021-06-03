num: int = int(input())
numList: list[int] = list(map(int, input().split()))


def isPrime(num: int) -> bool:
    if num < 2:
        return False
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False
    return True


count: int = 0
for n in numList:
    if isPrime(n):
        count += 1
print(count)
