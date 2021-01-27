case = int(input())

for i in range(case):
    str1 = input()
    str2 = input()

    largest = 0
    for c in str1:
        largest = max(largest, str2.count(c))

    print(f"#{i+1} {largest}")