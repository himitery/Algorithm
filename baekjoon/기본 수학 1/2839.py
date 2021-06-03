num: int = int(input())

if num % 5 == 0:
    print(num // 5)
elif num % 5 % 3 == 0:
    print(num // 5 + num % 5 // 3)
else:
    count = 1
    while (num - 3 * count) > 0:
        if (num - 3 * count) % 5 == 0 or (num - 3 * count) % 5 % 3 == 0:
            print(count + (num - 3 * count) // 5 + (num - 3 * count) % 5 // 3)
            break
        count += 1
    if (num - 3 * count) < 0:
        print(-1)
