alpha: list[str] = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

data: str = input()

result: int = len(data)
for a in alpha:
    if a in data:
        result -= data.count(a)
print(result)
