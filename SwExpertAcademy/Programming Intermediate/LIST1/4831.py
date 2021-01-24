case = int(input())

for i in range(case):
    k, n, m = list(map(int, input().split()))
    charger = list(map(int, input().split()))
    station = [x for x in range(0, n+1)]

    count = 0
    current = 0
    while True:
        if n in station[current + 1: current + k + 1]:
            break
        elif len(set(station[current + 1: current + k + 1]) & set(charger)) == 0:
            count = 0
            break
        current = max(list(
            set(station[current + 1: current + k + 1]) & set(charger)))
        count += 1

    print(f"#{i+1} {count}")
