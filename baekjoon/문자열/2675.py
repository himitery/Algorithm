num: int = int(input())

for _ in range(num):
    repeat, data = input().split()
    for d in data:
        print(f"{d}" * int(repeat), end="")
    print()
