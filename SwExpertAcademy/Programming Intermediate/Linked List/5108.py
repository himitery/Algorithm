case = int(input())


class NodeList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = self.Node(data)

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def insert(self, data, index):
        newNode = self.Node(data)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode

    def getData(self, index):
        if index == 0:
            return self.head.data
        else:
            currentNode = self.head.next
            for _ in range(index - 1):
                currentNode = currentNode.next
            return currentNode.data


for i in range(case):
    nodeList = NodeList()

    n, m, l = list(map(int, input().split()))

    initialNumber = list(map(int, input().split()))
    for num in initialNumber:
        nodeList.add(num)

    for _ in range(m):
        index, data = list(map(int, input().split()))
        nodeList.insert(data, index)

    print(f"#{i+1} {nodeList.getData(l)}")