case = int(input())


class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, num):
        self.numList = [x + 1 for x in range(num)]
        self.sequence = list()
        self.main()

    def main(self):
        self.setSequence(self.numList, 0)

        sequence = list()
        for layerList in self.sequence:
            for data in layerList:
                sequence.append(data)
        self.sequence = sequence
        self.sequence += sorted(
            list(set(self.numList) - (set(self.numList) & set(self.sequence)))
        )

    def getRootNode(self, length, start=None):
        layer = 1
        while True:
            if 2 ** layer - 1 <= length and 2 ** (layer + 1) - 1 > length:
                layer += 1
                break
            layer += 1

        return self.Node(
            (
                (length - (2 ** (layer - 1) - 1))
                if 2 ** (layer - 1) // 2 > (length - (2 ** (layer - 1) - 1))
                else (2 ** (layer - 1) // 2)
            )
            + (2 ** (layer - 1) - 2) // 2
            + 1
            + (start - 1 if start is not None else 0)
        )

    def setSequence(self, numList, layer):
        rootNode = self.getRootNode(len(numList), numList[0])
        rootNodeIndex = numList.index(rootNode.data)
        self.sequence[layer].append(rootNode.data) if len(
            self.sequence
        ) > layer else self.sequence.append([rootNode.data])

        leftSubTree = numList[:rootNodeIndex]
        rightSubTree = numList[rootNodeIndex + 1 :]

        if len(numList) > 3:
            self.setSequence(leftSubTree, layer + 1)
            self.setSequence(rightSubTree, layer + 1)
        elif len(numList) == 3:
            self.sequence[layer + 1].append(leftSubTree[0]) if len(
                self.sequence
            ) > layer + 1 else self.sequence.append([leftSubTree[0]])
            self.sequence[layer + 1].append(rightSubTree[0]) if len(
                self.sequence
            ) > layer + 1 else self.sequence.append([rightSubTree[0]])

    def getSequence(self):
        return self.sequence


for i in range(case):
    n = int(input())

    tree = BinaryTree(n)
    sequence = tree.getSequence()

    rootNode = sequence[0]
    specificNode = sequence[n // 2 - 1]

    print(f"#{i+1} {rootNode} {specificNode}")
