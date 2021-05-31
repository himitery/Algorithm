N: int = int(input())
scoreList: list[int] = list(map(int, input().split()))

maxScore = max(scoreList)
for i in range(N):
    scoreList[i] = scoreList[i] / maxScore * 100
print(sum(scoreList) / N)
