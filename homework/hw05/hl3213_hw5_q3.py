from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.stac = ArrayStack()
        self.dque = ArrayDeque()

    def __len__(self):
        return len(self.stac) + len(self.dque)

    def is_empty(self):
        return len(self.stac) == 0 and len(self.dque) == 0

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.dque.last()

    def push(self, val):
        if self.is_empty():
            self.stac.push(val)
        elif len(self) % 2 == 0:
            self.stac.push(self.dque.first())
            self.dque.dequeue_first()
            self.dque.enqueue_last(val)
        elif len(self) % 2 == 1:
            self.dque.enqueue_last(val)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            if len(self.stac) == 1 and len(self.dque) == 0:
                return self.stac.pop()
            elif len(self) % 2 == 0:
                return self.dque.dequeue_last()
            elif len(self) % 2 == 1:
                self.dque.enqueue_first(self.stac.top())
                self.stac.pop()
                return self.dque.dequeue_last()

    def mid_push(self, val):
        if len(self) % 2 == 0:
            self.stac.push(val)
        else:
            self.dque.enqueue_first(val)