from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        result.add_last(cursor.data)
        cursor = cursor.next
    return result

def deep_copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    cursor = lnk_lst.first_node()
    while cursor is not lnk_lst.trailer:
        if isinstance(cursor.data, DoublyLinkedList):
            result.add_last(deep_copy_linked_list(cursor.data))
        else:
            result.add_last(cursor.data)
        cursor = cursor.next
    return result
