K: int = int(input())


def move(size: int, current: int, destination: int):
    if size == 1:
        print(current, destination)
    else:
        childDestination: int = list(set([1, 2, 3]) - set([current, destination]))[0]
        move(size - 1, current, childDestination)
        print(current, destination)
        move(size - 1, childDestination, destination)


print(2 ** K - 1)
move(K, 1, 3)
