def main():
    x = input()
    attack = 0
    defence = 0
    result = None

    for c in x:
        if c == "(":
            attack += 1
        elif c == ")":
            defence += 1

    if attack == defence:
        result = "YES"
    else:
        result = "NO"

    print(result)


if __name__ == "__main__":
    main()
