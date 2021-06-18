while True:
    data: str = input()
    if data == "0":
        break

    result: str = "yes"
    dataList: list[int] = list(map(int, list(data)))
    for i in range(len(dataList) // 2):
        if dataList[i] != dataList[-i - 1]:
            result = "no"
            break
    print(result)
