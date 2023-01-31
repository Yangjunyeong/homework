class Stack:
    def __init__(self):
        self.items = []
    
    def empty(self):
        if not self.items:
            return not self.items
        else:
            return False

    def top(self):
        if not self.items:
            return None
        else:
            return self.items[-1]
    def pop(self):
        if not self.items:
            return None
        else:
            return self.items.pop()

    def push(self,item):
        self.items.append(item)

    def __repr__(self):
        print(self.items)
        



stk = Stack()
stk.push("가")
print(stk.top())
stk.repr()
