def main():
    N, M = map(int, input().split())
    MAPS = []
    for i in range(N):
        line = list(map(int, list(input())))
        MAPS.append(line)
    K = int(input())
    cnt = [0] * N

    for i in range(N):
        zero_cnt = MAPS[i].count(0)
        if zero_cnt % 2 == K % 2 and zero_cnt <= K:
            for j in range(N):
                if MAPS[i] == MAPS[j]:
                    cnt[i] += 1

    print(max(cnt))


if __name__ == "__main__":
    main()
