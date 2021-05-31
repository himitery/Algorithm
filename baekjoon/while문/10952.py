while True:
    num: list() = list(map(int, input().split()))
    if num == [0, 0]:
        break
    print(sum(num))
