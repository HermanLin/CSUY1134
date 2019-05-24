from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(nodeA, nodeB, result):
        if nodeA.data == None and nodeB.data == None:
            return result
        else:
            if nodeA.data == None:
                result.add_last(nodeB.data)
                return merge_sublists(nodeA, nodeB.next, result)
            elif nodeB.data == None:
                result.add_last(nodeA.data)
                return merge_sublists(nodeA.next, nodeB, result)
            elif nodeA.data <= nodeB.data:
                result.add_last(nodeA.data)
                return merge_sublists(nodeA.next, nodeB, result)
            elif nodeA.data > nodeB.data:
                result.add_last(nodeB.data)
                return merge_sublists(nodeA, nodeB.next, result)

    merged = DoublyLinkedList()
    if srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    if srt_lnk_lst2.is_empty():
        return srt_lnk_lst1
    return merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node(), merged)
