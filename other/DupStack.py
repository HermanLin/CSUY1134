import ArrayStack

class DupStack:
    def __init__(self):
        self.stack = ArrayStack.ArrayStack()
        self.size = 0

    def __len__(self):
        return self.size
            

    def is_empty(self):
        return self.size == 0
    
    def push(self, e):
        if self.is_empty():
            self.stack.push((e,1))
            self.size += 1
        else:
            temp = self.stack.pop()
            if temp[0] == e:
                self.stack.push((e,temp[1]+1))
            else:
                self.stack.push(temp)
                self.stack.push((e, 1))
            self.size += 1

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        else:
            temp = self.stack.pop()
            top_val = temp[0]
            self.stack.push(temp)
            return top_val

    def top_dups_count(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        else:
            temp = self.stack.pop()
            top_val_dup = temp[1]
            self.stack.push(temp)
            return top_val_dup

    def pop(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        else:
            self.size -= 1
            temp = self.stack.pop()
            if temp[1] > 1:
                self.stack.push((temp[0],temp[1] -2))
            return temp[0]

    def pop_dups(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        else:
            temp = self.stack.pop()
            self.size -= temp[1]
            return temp[0]


