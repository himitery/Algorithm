import sys

fast_input = sys.stdin.readline


def dfs(root: int, max_count: int, data: dict[int : list[int]]) -> list[int]:
    stack: list[int] = [root]
    visited: list[int] = [root]
    while len(visited) < max_count:
        if len(stack) == 0:
            return visited

        target: int = stack[-1]
        if target not in data.keys():
            stack.pop()
        else:
            for index in range(len(data[target])):
                if data[target][index] not in visited:
                    stack.append(data[target][index])
                    visited.append(data[target][index])
                    break
                elif index == len(data[target]) - 1:
                    stack.pop()
    return visited


def bfs(root: int, max_count: int, data: dict[int : list[int]]) -> list[int]:
    queue: list[int] = [root]
    visited: list[int] = [root]
    while len(visited) < max_count:
        if len(queue) == 0:
            return visited

        target: int = queue.pop(0)
        if target in data.keys():
            for num in data[target]:
                if num not in visited:
                    queue.append(num)
                    visited.append(num)
    return visited


def app() -> None:
    N, M, V = list(map(int, fast_input().split()))

    data: dict[int : list[int]] = dict()
    for _ in range(M):
        x, y = list(map(int, fast_input().split()))

        if x in data.keys():
            data[x] = sorted(data[x] + [y])
        else:
            data[x] = [y]

        if y in data.keys():
            data[y] = sorted(data[y] + [x])
        else:
            data[y] = [x]

    print(" ".join(list(map(str, dfs(V, N, data)))))
    print(" ".join(list(map(str, bfs(V, N, data)))))


if __name__ == "__main__":
    app()
