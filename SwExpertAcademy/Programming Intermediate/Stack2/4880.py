case = int(input())


def findWinner(users):
    users = [user for user in users if user[1] != 0]

    if len(users) == 1:
        return users
    elif len(users) == 2:
        return [winnerOfRSP(users)]
    else:
        left = findWinner(users[: (len(users) - 1) // 2 + 1])
        right = findWinner(users[(len(users) - 1) // 2 + 1 :])
        return findWinner(left + right)


def winnerOfRSP(users):
    userA, userB = users
    if userA[1] == userB[1]:
        return userA
    elif userB[1] - userA[1] in [1, -2]:
        return userB
    else:
        return userA


for i in range(case):
    n = int(input())
    users = list(enumerate(map(int, input().split())))
    print(f"#{i+1} {findWinner(users)[0][0]+1}")
