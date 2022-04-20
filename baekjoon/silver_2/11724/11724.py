import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M = list(map(int, fast_input().split()))
    data: list[set[int]] = [{x + 1} for x in range(N)]

    def isSameSet(src: int, dist: int) -> bool:
        for index in range(len(data)):
            if src in data[index]:
                return dist in data[index]

    def findDataIndex(target: int) -> int:
        for index in range(len(data)):
            if target in data[index]:
                return index

    for _ in range(M):
        src_node, dist_node = list(map(int, fast_input().split()))

        if not isSameSet(src_node, dist_node):
            data.append(
                (data.pop(findDataIndex(src_node))).union(
                    data.pop(findDataIndex(dist_node))
                )
            )

    print(len(data))


if __name__ == "__main__":
    app()
