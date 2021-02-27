def findSortest(current, data):
    li = list()
    for d in data:
        if current > d:
            li.append(current - d)
        else:
            li.append(d - current)

    return li.index(min(li))


def main():
    n, m, e = list(map(int, input().split()))

    data = list(map(int, input().split()))
    find = list()
    for _ in range(m):
        index = findSortest(e, data)
        find.append(data[index])
        del data[index]

    print(max(find) - min(find))


if __name__ == "__main__":
    main()