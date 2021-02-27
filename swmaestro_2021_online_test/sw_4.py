def find(index, data, visited):
    if index not in visited:
        visited.append(index)
        index += data[index]
        return find(index, data, visited)
    else:
        return len(visited) + 1


def main():
    n = int(input())
    data = list(map(int, input().split()))

    length = list()
    for i in range(3):
        length.append(find(i, data, []))
    print(max(length))


if __name__ == "__main__":
    main()