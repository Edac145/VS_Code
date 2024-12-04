#insertion in singly Linked Lists
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None

    def insertHead(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


LL=linkedList()
LL.insertHead(3)
LL.insertHead(2)
LL.insertHead(5)
LL.traverse()
LL.insertHead(9)
LL.traverse()