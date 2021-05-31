alpha: list[str] = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

data: str = input()

result: int = 0
for i in data:
    for a in alpha:
        if i in a:
            result += alpha.index(a) + 3
            break
print(result)
