import sys

fast_input = sys.stdin.readline
fast_output = sys.stdout.write


def app() -> None:
    N: int = int(fast_input())
    cards: list[int] = list(map(int, fast_input().split()))
    M: int = int(fast_input())
    numbers: list[int] = list(map(int, fast_input().split()))

    card_dict: dict[int:int] = dict()
    for card in cards:
        if card in card_dict.keys():
            card_dict[card] += 1
        else:
            card_dict[card] = 1

    for number in numbers:
        if number in card_dict.keys():
            fast_output(f"{card_dict[number]} ")
        else:
            fast_output("0 ")
    fast_output("\n")


if __name__ == "__main__":
    app()
