import sys

fast_input = sys.stdin.readline


def app() -> None:
    data: list[int] = [int(fast_input()) for _ in range(int(fast_input()))]

    for value in data:
        num_dict: dict[int:int] = {
            0: 0,
            1: 0,
            value: 1,
        }
        while max(num_dict.keys()) > 1:
            for key in list(filter(lambda x: x > 1, num_dict.keys())):
                new_keys: tuple[int, int] = (key - 1, key - 2)
                for new_key in new_keys:
                    if new_key in num_dict.keys():
                        num_dict[new_key] += num_dict[key]
                    else:
                        num_dict[new_key] = num_dict[key]
                del num_dict[key]
        print(num_dict[0], num_dict[1])


if __name__ == "__main__":
    app()
