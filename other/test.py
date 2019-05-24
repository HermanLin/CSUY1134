from DoublyLinkedList import DoublyLinkedList

def insert_sorted(srt_lnk_lst, elem):
    stor = DoublyLinkedList.Node(elem)
    curr = srt_lnk_lst.first_node()
    print("curr: ", curr.data)
    while elem > curr.data:
        curr = curr.next
        print("curr: ", curr.data)
    stor.prev = curr.prev
    curr.prev.next = stor
    curr.prev = stor
    stor.next = curr
    srt_lnk_lst.size += 1
    print("stor: ", stor.data, stor.prev.data, stor.next.data)  

lst = DoublyLinkedList()
lst.add_last(1)
lst.add_last(3)
lst.add_last(5)
lst.add_last(7)
lst.add_last(12)
print("lst: ", lst)
print("===insert_sorted===")
insert_sorted(lst, 6)
print("lst: ", lst)
