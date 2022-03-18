import sys

fast_input = sys.stdin.readline


def findFriend(root: int, data: dict[int : list[int]]) -> int:
    depth: int = 0
    for destination in list(filter(lambda x: x != root, sorted(data.keys()))):
        queue: list[tuple[int, int]] = [(0, root)]
        visited: list[tuple[int, int]] = [(0, root)]

        while len(queue) != 0:
            target: tuple[int, int] = queue.pop(0)

            if target[1] in data.keys():
                for num in data[target[1]]:
                    if num not in list(map(lambda x: x[1], visited)):
                        queue.append((target[0] + 1, num))
                        visited.append((target[0] + 1, num))

            if destination in list(map(lambda x: x[1], visited)) and target[
                0
            ] not in list(map(lambda x: x[0], queue)):
                depth += min(
                    list(
                        map(
                            lambda x: x[0],
                            list(
                                filter(lambda x: x[1] == destination, visited)
                            ),
                        )
                    )
                )
                break
    return depth


def app() -> None:
    N, M = list(map(int, fast_input().split()))

    data: dict[int : list[int]] = dict()
    for _ in range(M):
        x, y = list(map(int, fast_input().split()))

        if x in data.keys():
            data[x] = sorted(data[x] + [y]) if y not in data[x] else data[x]
        else:
            data[x] = [y]

        if y in data.keys():
            data[y] = sorted(data[y] + [x]) if x not in data[y] else data[y]
        else:
            data[y] = [x]

    result: list[int] = list()
    for num in range(1, N + 1):
        result.append(findFriend(num, data))
    print(result.index(min(result)) + 1)


if __name__ == "__main__":
    app()
