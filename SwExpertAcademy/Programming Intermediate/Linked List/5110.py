case = int(input())


class NodeList:
    class Node:
        def __init__(self, data, pre=None, next=None):
            self.data = data
            self.pre = pre
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = self.Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

            newNode.next = None
        else:
            self.tail.next = newNode
            newNode.pre = self.tail
            self.tail = newNode

    def insertNode(self, nodeList):
        currentNode = self.head
        while True:
            if currentNode.data > nodeList.head.data:
                if currentNode.pre is None:
                    self.head = nodeList.head
                else:
                    preNode = currentNode.pre
                    preNode.next = nodeList.head
                    nodeList.head.pre = preNode
                nodeList.tail.next = currentNode
                currentNode.pre = nodeList.tail
                break
            elif currentNode.next is None:
                nodeList.head.pre = currentNode
                currentNode.next = self.head
                self.tail = nodeList.tail
                break
            currentNode = currentNode.next

    def getNodesFromBack(self, count):
        nodeList = list()

        currentNode = self.tail
        for _ in range(count):
            nodeList.append(currentNode.data)
            if currentNode.pre is None:
                break
            currentNode = currentNode.pre

        return nodeList


for i in range(case):
    n, m = list(map(int, input().split()))

    nodeList = NodeList()

    numberList = list(map(int, input().split()))
    for number in numberList:
        nodeList.add(number)

    for _ in range(m - 1):
        temporaryNodeList = NodeList()
        numberList = list(map(int, input().split()))

        for number in numberList:
            temporaryNodeList.add(number)

        nodeList.insertNode(temporaryNodeList)

    result = " ".join(list(map(str, nodeList.getNodesFromBack(10))))
    print(f"#{i+1} {result}")
