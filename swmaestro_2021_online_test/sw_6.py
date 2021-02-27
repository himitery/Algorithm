def main():
    n = int(input())
    data = list(map(int, input().split()))

    value = 0
    while len(data) > 1:
        if max(data[: len(data) // 2]) > max(data[len(data) // 2 :]):
            value += max(data[: len(data) // 2])
            data = data[len(data) // 2 :]
        else:
            value += max(data[len(data) // 2 :])
            data = data[: len(data) // 2]
    print(value)


if __name__ == "__main__":
    main()