case = int(input())

for i in range(case):
    n = int(input())
    maze = list()

    start = None
    end = None

    for j in range(n):
        maze.append(list(map(int, list(input()))))
        if 2 in maze[-1]:
            start = [j, maze[-1].index(2)]
        if 3 in maze[-1]:
            end = [j, maze[-1].index(3)]

    count = 0
    flag = False

    queue = list([start])
    nextQueue = list()
    while True:
        current = queue.pop(0)

        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for d in direction:
            if (
                current[0] + d[0] in range(n) and current[1] + d[1] in range(n)
            ) and maze[current[0] + d[0]][current[1] + d[1]] == 0:
                nextQueue.append([current[0] + d[0], current[1] + d[1]])
                maze[current[0] + d[0]][current[1] + d[1]] = -1
            elif (
                current[0] + d[0] in range(n) and current[1] + d[1] in range(n)
            ) and maze[current[0] + d[0]][current[1] + d[1]] == 3:
                flag = True
                break

        if flag:
            break

        if len(queue) == 0 and len(nextQueue) != 0:
            queue = nextQueue.copy()
            nextQueue = []
            count += 1
        elif len(queue) == 0 and len(nextQueue) == 0:
            count = 0
            break

    print(f"#{i+1} {count}")
