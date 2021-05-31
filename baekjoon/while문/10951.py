while True:
    try:
        num: list = list(map(int, input().split()))
        print(sum(num))
    except:
        break
