import sys

fast_input = sys.stdin.readline
fast_print = sys.stdout.write


def app() -> None:
    n, m = list(map(int, fast_input().split()))
    tree: list[int] = sorted(list(map(int, fast_input().split())), reverse=True)
    tree_length = len(tree)
    tree.append(0)

    index: int = 0
    length: int = 0
    while length < m and index < tree_length:
        length += (tree[index] - tree[index + 1]) * (index + 1)
        index += 1

    result: int = tree[index]
    if length > m:
        result += (length - m) // index
    fast_print(str(result))


if __name__ == "__main__":
    app()
