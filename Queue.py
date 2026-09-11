# FIFO - FIRST IN, FIRST OUT
# In queue, we can access element fromo both side front and last.
# there is module for it called deque in collection

from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def add(self, item):
        self.queue.append(item)
    
    def popleft(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def popright(self):
        if self.is_empty():
            return None
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def display(self):
        # deque supprots indexing but not slice so we reversed() to original deque unchanged, 
        # and then converte it into list.
        print(list(reversed(self.queue)))



def check():
    q = Queue()

    q.add("vaibhav")
    q.add("Aryan")
    q.add("Rishabh")
    q.add("Prince")

    q.display()

    print(q.is_empty())

    print(q.popleft())
    print(q.popright())

    q.display()

    print(q.size())


check()


# Piority Queue


import heapq

que = []

# Syntax: heapq.heapush(queue, (piority, item))

heapq.heappush(que, (1, "First piortiy"))
heapq.heappush(que, (3, "Third Piority"))
heapq.heappush(que, (2, "Second piority"))

print(que)

# It will remove the higher piority first
print(heapq.heappop(que))
print(heapq.heappop(que))
print(heapq.heappop(que))

