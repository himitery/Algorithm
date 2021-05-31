num: int = int(input())
numList: int = int(input())

result = 0
while numList != 0:
    result += numList % 10
    numList = numList // 10
print(result)
