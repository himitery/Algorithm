case = int(input())


class NodeList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.current = None

    def add(self, data):
        newNode = self.Node(data)

        if self.head is None:
            self.head = newNode
        else:
            self.current.next = newNode
        self.current = newNode

    def insert(self, index, data):
        self.setCurrentNode(index)

        newNode = self.Node(data)
        newNode.next = self.current.next
        self.current.next = newNode

    def setCurrentNode(self, index):
        self.current = self.head
        for _ in range(index - 1):
            self.current = self.current.next

    def delete(self, index):
        self.setCurrentNode(index)

        self.current.next = self.current.next.next

    def change(self, index, data):
        self.setCurrentNode(index)
        self.current = self.current.next

        self.current.data = data

    def getDataFromIndex(self, index):
        self.current = self.head
        for _ in range(index):
            self.current = self.current.next
            if self.current is None:
                return -1
        return self.current.data


for i in range(case):
    n, m, l = list(map(int, input().split()))

    nodeList = NodeList()
    numList = list(map(int, input().split()))
    for num in numList:
        nodeList.add(num)

    for _ in range(m):
        inputValue = input().split()
        if inputValue[0] == "I":
            index, data = list(map(int, inputValue[1:]))
            nodeList.insert(index, data)
        elif inputValue[0] == "D":
            index = list(map(int, inputValue[1:]))[0]
            nodeList.delete(index)
        elif inputValue[0] == "C":
            index, data = list(map(int, inputValue[1:]))
            nodeList.change(index, data)

    result = nodeList.getDataFromIndex(l)
    print(f"#{i+1} {result}")
