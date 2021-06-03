M: int = int(input())
N: int = int(input())


def isPrime(num: int) -> bool:
    if num < 2:
        return False
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False
    return True


result: list[int] = list()
for i in range(M, N + 1):
    if isPrime(i):
        result.append(i)

if len(result) != 0:
    print(sum(result), min(result), sep="\n")
else:
    print(-1)
