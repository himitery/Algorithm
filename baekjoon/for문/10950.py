num: int = int(input())

for i in range(num):
    print(sum(list(map(int, input().split()))))
