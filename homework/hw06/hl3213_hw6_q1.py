from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    
    def __init__(self):
        self.data = DoublyLinkedList()
        self.num_elem = 0

    def __len__(self):
        return self.num_elem

    def is_empty(self):
        return self.num_elem == 0

    def enqueue(self, e):
        self.data.add_last(e)

    def dequeue(self):   
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data

def main():
    lq = LinkedQueue()
    for x in range(10):
        lq.enqueue(x)
    print(lq.data)
    for x in range(10):
        dq = lq.dequeue()
        print(dq)
    print(lq.data, len(lq))

#main()