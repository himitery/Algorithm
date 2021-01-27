case = int(input())

for i in range(case):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0
    
    print(f"#{i+1} {result}")