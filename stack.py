# LIFO - LAST IN, FIRST OUT
class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack[::-1])

    
stack = Stack()

stack.add("hello")
stack.add("hello 1")

stack.display()

print(stack.is_empty() )    # Always check the stack is empty or not before pop otherwise, 
                     # it throw error EmptyStackException also called Stack underflow.
print(stack.pop())

stack.display()

print(stack.peek())

print(stack.size())