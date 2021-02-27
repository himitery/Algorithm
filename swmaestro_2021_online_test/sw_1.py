def main():
    skill = input().split()
    count = int(input())

    skillDict = dict()
    distList = list()
    for _ in range(count):
        src, dist = tuple(input().split())
        distList.append(dist)
        if src in skillDict.keys():
            skillDict[src] += dist
        else:
            skillDict[src] = [dist]

    def findValue(key, stack):
        data = stack + [key]
        if key in skillDict.keys():
            for value in skillDict[key]:
                findValue(value, data)
        else:
            if data[0] not in distList:
                print(" ".join(data)) if len(data) > 1 else None

    for s in skill:
        findValue(s, [])


if __name__ == "__main__":
    main()