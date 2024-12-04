#implementing a single Node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
a=Node(12)
b=Node(13)

print('a.data=',a.data)
print('b.data=',b.data)

a.next=b
print(a)
print(b)
print(a.next)