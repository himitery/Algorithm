import sys

num: int = int(sys.stdin.readline().rstrip())

for i in range(num):
    print(sum(list(map(int, sys.stdin.readline().rstrip().split()))))
