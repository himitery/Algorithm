case = int(input())


class NodeList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.start = None
        self.current = None

    def add(self, data):
        newNode = self.Node(data)

        if self.start is None:
            self.start = newNode
            self.current = newNode
        else:
            self.current.next = newNode
            self.current = newNode

    def setCurrentNodeToStart(self):
        self.current = self.start

    def setNextNode(self):
        self.current = (
            self.current.next if self.current.next is not None else self.start
        )

    def insert(self):
        currentNodeData = self.current.data
        nextNodeData = (
            self.current.next.data if self.current.next is not None else self.start.data
        )
        newData = currentNodeData + nextNodeData
        newNode = self.Node(newData)

        newNode.next = self.current.next
        self.current.next = newNode
        self.current = newNode

    def getNodeList(self):
        currentNode = self.start
        nodeList = list()
        while currentNode is not None:
            nodeList.append(currentNode.data)
            currentNode = currentNode.next

        return nodeList


for i in range(case):
    n, m, k = list(map(int, input().split()))

    nodeList = NodeList()
    numList = list(map(int, input().split()))
    for num in numList:
        nodeList.add(num)
    nodeList.setCurrentNodeToStart()

    for j in range(k):
        for _ in range(m - 1):
            nodeList.setNextNode()
        nodeList.insert()

    nodeList = nodeList.getNodeList()
    nodeList.reverse()
    nodeList = list(map(str, nodeList))[:10]

    result = " ".join(nodeList)
    print(f"#{i+1} {result}")