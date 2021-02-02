case = int(input())

for i in range(case):
    size = int(input())
    maze = list()

    start = end = None
    for j in range(size):
        maze.append(list(map(int, list(input()))))
        if 2 in maze[j]:
            start = [j, maze[j].index(2)]
        if 3 in maze[j]:
            end = [j, maze[j].index(3)]

    track = list([start])
    current = start
    flag = False
    while flag == False:
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        next = None
        for d in direction:
            if current[0] + d[0] in range(size) and current[1] + d[1] in range(size):    
                if maze[current[0] + d[0]][current[1] + d[1]] == 0:
                    next = [current[0]+d[0], current[1]+d[1]]
                    break
                elif [current[0]+d[0], current[1]+d[1]] == end:
                    flag = 1
                    break

        if flag != False:
            break
        
        if next is not None:
            maze[current[0]][current[1]] = -1
            track.append(next)
            current = next
        elif len(track) == 1:
            flag = 0
            break
        else:
            maze[current[0]][current[1]] = -1
            del track[-1]
            current = track[-1]

    
    print(f"#{i+1} {flag}")

        