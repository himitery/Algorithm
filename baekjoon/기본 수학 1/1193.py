num: int = int(input())

line: int = 0
while num - line * (line + 1) // 2 > 0:
    line += 1

num -= line * (line - 1) // 2
if line % 2 == 0:
    print(f"{num}/{line - num + 1}")
else:
    print(f"{line - num + 1}/{num}")
