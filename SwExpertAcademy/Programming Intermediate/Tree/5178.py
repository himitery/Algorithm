case = int(input())


class Tree:
    def __init__(self, m, n, l):
        self.m = m
        self.n = n
        self.l = l
        self.tree = [0] * (m + 1)

    def main(self):
        self.add(1)
        return self.tree[l]

    def setValue(self, data):
        self.tree[data[0]] = data[1]

    def add(self, index):
        if index <= self.m:
            self.tree[index] = max(
                self.add(index * 2) + self.add(index * 2 + 1), self.tree[index]
            )
            return self.tree[index]
        else:
            return 0


for i in range(case):
    m, n, l = list(map(int, input().split()))

    tree = Tree(m, n, l)

    for _ in range(n):
        tree.setValue(list(map(int, input().split())))

    result = tree.main()

    print(f"#{i+1} {result}")