strList: list[str] = [chr(x) for x in range(ord("a"), ord("z") + 1)]

S: str = input()

result: list[int] = list()
for alphabet in strList:
    result.append(S.find(alphabet))
print(" ".join(list(map(str, result))))
