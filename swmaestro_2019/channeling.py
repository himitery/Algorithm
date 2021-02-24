n = int(input())

userList = list()
for _ in range(n):
    userList.append(list(map(int, input().split())))

for user in userList:
    enemyList = userList.copy()
    enemyList.remove(user)
    count = 0
    for enemy in enemyList:
        if enemy[0] <= user[0] and user[0] <= enemy[1]:
            count += 1
    print(count)