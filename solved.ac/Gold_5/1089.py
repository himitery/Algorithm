def main():
    nums = [[] for _ in range(10)]
    nums[0] = [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14]
    nums[1] = [2, 5, 8, 11, 14]
    nums[2] = [0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14]
    nums[3] = [0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14]
    nums[4] = [0, 2, 3, 5, 6, 7, 8, 11, 14]
    nums[5] = [0, 1, 2, 3, 6, 7, 8, 11, 12, 13, 14]
    nums[6] = [0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14]
    nums[7] = [0, 1, 2, 5, 8, 11, 14]
    nums[8] = [0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    nums[9] = [0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14]

    N = int(input())
    if N <= 9:
        numList = list()
        for _ in range(5):
            numList.append(list(input()))

        data = list()
        for n in range(N):
            value = [x[4 * n : 4 * n + 3] for x in numList]

            num = list()
            for i in range(5):
                for j in range(3):
                    if value[i][j] == "#":
                        num.append(i * 3 + j)

            temp = list()
            for index, i in enumerate(nums):
                if list(set(num) - set(i)) == []:
                    temp.append(index)
            data.append(temp)
        data.reverse()

        if [] not in data:
            countOfCases = 1
            for i in data:
                countOfCases *= len(i)

            total = 0
            for i, v in enumerate(data):
                total += sum(v) * countOfCases / len(v) * 10 ** i

            print(total / countOfCases)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
