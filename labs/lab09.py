class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        return
    
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def add_list_item(self, item):
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item
        return

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.prev
            next_node = current_node.next
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.prev = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                return
            current_node = next_node
            current_id = current_id + 1
        return

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        