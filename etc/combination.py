def combination(length):
    comb = list()

    for i in range(1 << length):
        arr = list()
        for j in range(length):
            if i & (1 << j):
                arr.append(j)
        comb.append(arr)

    return comb
