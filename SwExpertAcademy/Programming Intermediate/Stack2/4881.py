case = int(input())

def permutation(cube, n):
    num = [i for i in range(n)]
    used = [False for _ in range(n)]

    def generate(chosen, used, sum, minimum):
        if len(chosen) == n and sum < minimum:
            minimum = sum
        else:
            for i in range(n):
                if used[i] is False:
                    chosen.append(num[i])
                    sum += cube[len(chosen) - 1][i]
                    used[i] = True
                    minimum = generate(chosen, used, sum, minimum) if sum < minimum else minimum
                    sum -= cube[len(chosen) - 1][i]
                    chosen.pop()
                    used[i] = False
        return minimum

    return generate([], used, 0, 100)

for i in range(case):
    n = int(input())

    cube = list()
    for _ in range(n):
        cube.append(list(map(int, input().split())))
    
    minimum = permutation(cube, n)
    print(f"#{i+1} {minimum}")
    