case = int(input())

for i in range(case):
    v, e = list(map(int, input().split()))

    nodeRelation = dict()
    for j in range(e):
        src, dest = list(map(int, input().split()))

        if src in nodeRelation.keys():
            nodeRelation[src].append(dest)
        else:
            nodeRelation[src] = [dest]
    s, g = list(map(int, input().split()))

    stack = [s]
    while True:
        if len(stack) == 0:
            result = 0
            break
        elif stack[-1] == g:
            result = 1
            break
        if stack[-1] in list(nodeRelation.keys()):
            if len(nodeRelation[stack[-1]]) != 0:
                stack.append(nodeRelation[stack[-1]][0])
                del nodeRelation[stack[-2]][0]
            else:
                del stack[-1]
        else:
            del stack[-1]

    print(f"#{i+1} {result}")

        

 