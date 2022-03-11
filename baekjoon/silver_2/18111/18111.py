import sys

fast_input = sys.stdin.readline


def app() -> None:
    N, M, B = list(map(int, fast_input().split()))
    blocks: list[list[int]] = []

    block_dict: dict[int:int] = dict()
    for _ in range(N):
        data: list[int] = list(map(int, fast_input().split()))
        for value in data:
            if value in block_dict.keys():
                block_dict[value] += 1
            else:
                block_dict[value] = 1
        blocks.append(data)

    time = height = None
    for target in range(min(block_dict.keys()), max(block_dict.keys()) + 1):
        add = remove = need_time = 0
        for key, value in block_dict.items():
            diff: int = abs(target - key)
            if target > key:
                add += value * diff
                need_time += value * diff
            elif target < key:
                remove += value * diff
                need_time += value * diff * 2

        if remove + B >= add and (time is None or time >= need_time):
            time = need_time
            height = target

    print(time, height)


if __name__ == "__main__":
    app()
