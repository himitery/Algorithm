while True:
    try:
        num: int = int(input())
        newNum = num % 10 * 10 + (num // 10 + num % 10) % 10

        count = 1
        while newNum != num:
            newNum = newNum % 10 * 10 + (newNum // 10 + newNum % 10) % 10
            count += 1
        print(count)
    except:
        break
