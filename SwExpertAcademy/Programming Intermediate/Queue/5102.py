case = int(input())

for i in range(case):
    v, e = list(map(int, input().split()))

    nodeRelation = dict()
    for _ in range(e):
        k, v = list(map(int, input().split()))
        if k in nodeRelation.keys():
            nodeRelation[k].append(v)
        else:
            nodeRelation[k] = list([v])
        if v in nodeRelation.keys():
            nodeRelation[v].append(k)
        else:
            nodeRelation[v] = list([k])

    start, end = list(map(int, input().split()))

    count = 0
    nodeList = [start]
    nextNodeList = list()
    usedNodeList = list()

    while True:
        for j in nodeList:
            if j in nodeRelation.keys():
                for v in nodeRelation[j]:
                    if v not in usedNodeList:
                        nextNodeList.append(v)
                        usedNodeList.append(v)

        count += 1

        if len(nextNodeList) == 0:
            count = 0
            break
        elif end in nextNodeList:
            break
        else:
            nodeList = nextNodeList.copy()
            nextNodeList = list()

    print(f"#{i+1} {count}")
