case = int(input())


class Tree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.current = None

    def add(self, src, data):
        newNode = self.Node(data)

        if src is None:
            self.root = newNode
        else:
            self.findNode(src, self.root)
            if self.current.left is None:
                self.current.left = newNode
            elif self.current.right is None:
                self.current.right = newNode

    def findNode(self, data, node):
        if node is None:
            return
        else:
            if node.data == data:
                self.current = node
                return True
            else:
                if self.findNode(data, node.left):
                    return True
                if self.findNode(data, node.right):
                    return True
            return False

    def countNodes(self, node=None, data=None):
        if data is not None:
            self.findNode(data, self.root)
            node = self.current

        count = 0
        if node is not None:
            count += 1
            count += self.countNodes(node.left)
            count += self.countNodes(node.right)
        return count


for i in range(case):
    e, n = list(map(int, input().split()))

    tree = Tree()
    numList = list(map(int, input().split()))
    tree.add(None, numList[0])
    for j in range(e):
        num = numList[2 * j : 2 * (j + 1)]
        tree.add(num[0], num[1])

    result = tree.countNodes(None, n)
    print(f"#{i+1} {result}")
