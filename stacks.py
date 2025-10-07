# You don't need to understand this code.
# It provides the necessary queue and stack operations

from collections import deque

class Stack:
    def __init__(self):
        self._d = []
    def push(self, x):
        self._d.append(x)
    def pop(self):
        if not self._d:
            raise IndexError('pop from empty stack')
        return self._d.pop()
    def peek(self):
        if not self._d:
            raise IndexError('peek from empty stack')
        return self._d[-1]
    def is_empty(self):
        return len(self._d) == 0
    def __repr__(self):
        return f"Stack({self._d!r})"

class Queue:
    def __init__(self):
        self._d = deque()
    def enqueue(self, x):
        self._d.append(x)
    def dequeue(self):
        if not self._d:
            raise IndexError('dequeue from empty queue')
        return self._d.popleft()
    def front(self):
        if not self._d:
            raise IndexError('front from empty queue')
        return self._d[0]
    def is_empty(self):
        return len(self._d) == 0
    def __repr__(self):
        return f"Queue({list(self._d)!r})"




s = Stack()
s.push('A'); s.push('B'); s.push('C')
print(s.pop())    # ?
print(s.peek())   # ?
print(s.is_empty()) # ?