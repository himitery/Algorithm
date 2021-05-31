x, y = input().split()

x = list(x)
y = list(y)

x.reverse()
y.reverse()

x = int("".join(x))
y = int("".join(y))

print(x if x > y else y)
