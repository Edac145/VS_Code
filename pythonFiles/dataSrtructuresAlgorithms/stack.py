from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

stack = deque()
stack.append("com")
stack.append("world")
stack.append("india")
stack.append("china")

print(stack)

s = Stack()
s.push(5)
print(s.peek())
s.pop()
print(s)
print(s.is_empty())
s.push(67)
s.push(7)
s.push(9)
print(s.size()) 
