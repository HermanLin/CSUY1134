from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if (self.data.is_empty()):
            raise Exception("Stack is empty")
        return self.data.top()[0]  

    def push(self, val):
        if self.data.is_empty():
            self.data.push((val, val))
        elif self.data.top()[1] > val:
            self.data.push((val, self.data.top()[1]))
        else:
            self.data.push((val, val))

    def pop(self):
        if self.data.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()[0]

    def max(self):
        if self.data.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[1]