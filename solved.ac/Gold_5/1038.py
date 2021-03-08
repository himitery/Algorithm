def main():
    N = int(input())

    if N < 1023:
        count = 0
        n = [0]
        while count != N:
            if len(n) == 1:
                n[0] += 1
            else:
                n[0] += 1
                for i in range(len(n) - 1):
                    if n[i] >= n[i + 1]:
                        n[i] = 0
                        n[i + 1] += 1
                    else:
                        break
            if 10 in n:
                n[:] = [x for x in range(len(n))]
                n.append(len(n))
            if n.count(0) <= 1:
                count += 1
        n = reversed(n)
        print(int("".join(list(map(str, n)))))
    else:
        print(-1)


if __name__ == "__main__":
    main()
