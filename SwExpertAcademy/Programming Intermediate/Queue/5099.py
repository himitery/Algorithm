case = int(input())

for i in range(case):
    n, m = list(map(int, input().split()))
    pizza = list(map(list, enumerate(map(int, input().split()))))

    oven = pizza[:n]
    pizza = pizza[n:]
    complete = list()
    current = 0
    while True:
        try:
            oven[current][1] = oven[current][1] // 2
            if oven[current][1] == 0:
                complete.append(oven.pop(current))
                oven.insert(current, pizza.pop(0)) if len(pizza) != 0 else oven.insert(
                    current, [0, -1]
                )
            if len(complete) == m:
                result = complete.pop()[0] + 1
                break
        except:
            pass
        current = (current + 1) % n % len(oven)

    print(f"#{i+1} {result}")
