from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.enq = ArrayStack()
        self.deq = ArrayStack()

    def __len__(self):
        return len(self.deq)

    def is_empty(self):
        return len(self.deq) == 0

    def first(self):
        if self.deq.is_empty():
            raise Exception("Queue is Empty")
        else:
            return self.deq.top()

    def enqueue(self, val):
        if self.deq.is_empty():
            self.deq.push(val)
        else:
            for q in range(len(self.deq)):
                self.enq.push(self.deq.pop())
            self.enq.push(val)
            for q in range(len(self.enq)):
                self.deq.push(self.enq.pop())

    def dequeue(self):
        if self.deq.is_empty():
            raise Exception("Queue is Empty")
        else:
            return self.deq.pop()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    #queue.enqueue(3)
    a = queue.dequeue()
    print(a)
    b = queue.dequeue()
    print(b)

    