case = int(input())


class BinaryTree:
    def __init__(self, n):
        self.n = n
        self.count = 1
        self.sequence = [0] * (n + 1)
        self.setSequence(1)

    def setSequence(self, num):
        if num <= self.n:
            self.setSequence(num * 2)
            self.sequence[num] = self.count
            self.count += 1
            self.setSequence(num * 2 + 1)

    def getResult(self):
        return [self.sequence[1], self.sequence[self.n // 2]]


for i in range(case):
    n = int(input())

    tree = BinaryTree(n)
    result = tree.getResult()

    print(f"#{i+1} {result[0]} {result[1]}")
