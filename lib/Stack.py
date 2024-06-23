class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return not len(self.items)

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for index in range(len(self.items)):
            if self.items[index] == target:
                return len(self.items)-1 - index
        return -1
