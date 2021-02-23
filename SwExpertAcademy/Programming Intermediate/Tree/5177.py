case = int(input())


class Tree:
    def __init__(self, numList):
        self.numList = numList
        self.tree = [0]
        self.sum = 0

    def main(self):
        for num in self.numList:
            self.add(num)
        self.getSum(len(self.tree) - 1)
        return self.sum

    def add(self, num):
        self.tree.append(num)
        self.sort(len(self.tree) - 1)

    def sort(self, index):
        if index >= 2 and self.tree[index] < self.tree[index // 2]:
            self.tree[index], self.tree[index // 2] = (
                self.tree[index // 2],
                self.tree[index],
            )
            self.sort(index // 2)

    def getSum(self, index):
        if index >= 2:
            self.sum += self.tree[index // 2]
            self.getSum(index // 2)


for i in range(case):
    n = int(input())
    numList = list(map(int, input().split()))

    tree = Tree(numList)
    result = tree.main()

    print(f"#{i+1} {result}")
