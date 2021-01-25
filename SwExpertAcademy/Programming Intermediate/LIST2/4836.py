case = int(input())

for i in range(case):
    pallet = [[0 for _ in range(10)] for _ in range(10)]
    count = 0

    n = int(input())

    for j in range(n):
        num = list(map(int, input().split()))
        r1, c1 = num[:2]
        r2, c2 = num[2:4]
        color = num[-1]

        for col in range(c1, c2+1):
            for row in range(r1, r2+1):
                pallet[row][col] += color
                if pallet[row][col] == 3:
                    count += 1

    print(f"#{i+1} {count}")
