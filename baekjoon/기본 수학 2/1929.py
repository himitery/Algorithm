M, N = list(map(int, input().split()))


def isPrime(start: int, end: int) -> None:
    end += 1
    result = [True] * end
    for i in range(2, end // 2 + 1):
        if result[i]:
            for j in range(2 * i, end, i):
                result[j] = False

    for i in range(start, end):
        if i > 1 and result[i]:
            print(i)


isPrime(M, N)
