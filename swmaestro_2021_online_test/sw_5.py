def main():
    n = int(input())

    data = dict()
    maxCount = 0
    for _ in range(n ** 2):
        value = list(map(int, input().split()))
        data[value[0]] = value[2:]
        if max(value[2:]) > maxCount:
            maxCount = max(value[2:])

    score = 0
    for count in range(1, maxCount + 1):
        temp = list()
        for key in data.keys():
            if count in data[key]:
                temp.append(key)
        if len(temp) != 0:
            score += max(temp)
    print(score)


if __name__ == "__main__":
    main()