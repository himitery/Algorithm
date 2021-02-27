def main():
    p, n, h = list(map(int, input().split()))

    pc = dict()
    for i in range(p):
        pc[i + 1] = []

    for _ in range(n):
        num, time = list(map(int, input().split()))
        if time <= h:
            pc[num] += [time]

    for key in pc.keys():
        if len(pc[key]) == 0:
            print(key, 0)
        else:
            count = 0
            combination = list()
            for j in range(1 << len(pc[key])):
                part = list()
                for l in range(len(pc[key])):
                    if j & (1 << l):
                        part.append(pc[key][l])
                if sum(part) <= h:
                    combination.append(sum(part))

            print(key, max(combination) * 1000)


if __name__ == "__main__":
    main()