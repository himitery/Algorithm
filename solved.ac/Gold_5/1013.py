import re as expression


def main():
    T = int(input())

    for _ in range(T):
        data = input()
        compile = expression.compile("(100+1+|01)+")

        if compile.fullmatch(data):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()