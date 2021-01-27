case = int(input())

def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def func(n):
    if n == 10:
        return 1
    else:
        return func(n - 20)*4+1

def combination(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r)) if n != r else 1

for i in range(case):
    n = int(input())

    result = 0
    if n % 20 != 0:
        result = func(n)
    else:
        for r in  range(1, n//20 + 1):
            result += int(combination(n//10-r, r)*2**r)
        result += 1

    print(f"#{i+1} {result}")