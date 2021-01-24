case = int(input())

for i in range(case):
    length = int(input())
    number = int(input())

    numberList = list()
    for j in range(length):
        numberList.append(number % 10)
        number = number // 10

    numberList.sort()
    countOfNumbers = dict()
    largestCount = 1
    mostValue = numberList[0]
    for j in range(length):
        if countOfNumbers.get(numberList[j]) is None:
            countOfNumbers[numberList[j]] = 1
        else:
            countOfNumbers[numberList[j]] += 1

        if countOfNumbers[numberList[j]] > largestCount or countOfNumbers[numberList[j]] == largestCount and mostValue < numberList[j]:
            mostValue = numberList[j]
            largestCount = countOfNumbers[numberList[j]]

    print(f"#{i+1} {mostValue} {largestCount}")
