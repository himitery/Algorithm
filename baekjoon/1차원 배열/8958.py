N: int = int(input())

for i in range(N):
    data = input().split("X")
    score = 0
    for d in data:
        score += len(d) * (len(d) + 1) // 2
    print(score)
