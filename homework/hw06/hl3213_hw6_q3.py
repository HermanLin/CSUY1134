from DoublyLinkedList import DoublyLinkedList

class CompactString:

    def __init__(self, orig_str):
        self.cstring = DoublyLinkedList()
        last = ""
        stor_count = []
        for letter in orig_str:
            if letter == last:
                stor_count[-1] = (letter, stor_count[-1][1] +1)
            else:
                stor_count.append((letter, 1))
                last = letter
        for c in stor_count:
            self.cstring.add_last((c[0], c[1]))                

    def __add__(self, other):
        if not self.cstring.is_empty() and not other.cstring.is_empty():
            node1 = self.cstring.first_node()
            node2 = other.cstring.first_node()
        final = DoublyLinkedList()

        if self.cstring.is_empty():
            node2 = other.cstring.first_node()
            while node2 is not other.cstring.trailer:
                final.add_last(node2.data)
                node2 = node2.next
        elif other.cstring.is_empty():
            node1 = self.cstring.first_node()
            while node1 is not self.cstring.trailer:
                final.add_last(node1.data)
                node1 = node1.next
        else:
            while node1 is not self.cstring.trailer:
                final.add_last(node1.data)
                node1 = node1.next
            last_node = final.last_node()
            if last_node.data[0] == node2.data[0]:
                final.add_before(last_node, (last_node.data[0], last_node.data[1] + node2.data[1]))
                final.delete_node(last_node)
                node2 = node2.next
            while node2 is not other.cstring.trailer:
                final.add_last(node2.data)
                node2 = node2.next

        result = ""
        crsr = final.first_node()
        while crsr is not final.trailer:
            cntr = crsr.data[1]
            while cntr > 0:
                result += crsr.data[0]
                cntr -= 1
            crsr = crsr.next
        return CompactString(result)     
        
    def __lt__(self, other):
        if self.cstring.is_empty():
            if other.cstring.is_empty():
                return False
            else:
                return True
        elif other.cstring.is_empty():
            return False
        else:
            node1 = self.cstring.first_node()
            node2 = other.cstring.first_node()
            while node1 is not self.cstring.trailer and node2 is not other.cstring.trailer:
                if node1.data[0] < node2.data[0]:
                    return True
                elif node1.data[0] == node2.data[0]:
                    if node1.data[1] < node2.data[1]:
                        node1 = node1.next
                    elif node1.data[1] > node2.data[1]:
                        node2 = node2.next
                    else:
                        node1 = node1.next
                        node2 = node2.next
                else:
                    return False
            if node1 is self.cstring.trailer:
                if node2 is other.cstring.trailer:
                    return False
                return True
            else:
                return False

    def __le__(self, other):
        if self.cstring.is_empty():
            return True
        elif other.cstring.is_empty():
            return False
        else:
            node1 = self.cstring.first_node()
            node2 = other.cstring.first_node()
            while node1 is not self.cstring.trailer and node2 is not other.cstring.trailer:
                if node1.data[0] < node2.data[0]:
                    return True
                elif node1.data[0] == node2.data[0]:
                    if node1.data[1] < node2.data[1]:
                        node1 = node1.next
                    elif node1.data[1] > node2.data[1]:
                        node2 = node2.next
                    else:
                        node1 = node1.next
                        node2 = node2.next
                else:
                    return False
            if node1 is self.cstring.trailer:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.cstring.is_empty():
            return False
        elif other.cstring.is_empty():
            return True
        else:
            node1 = self.cstring.first_node()
            node2 = other.cstring.first_node()
            while node1 is not self.cstring.trailer and node2 is not other.cstring.trailer:
                if node1.data[0] > node2.data[0]:
                    return True
                elif node1.data[0] == node2.data[0]:
                    if node1.data[1] < node2.data[1]:
                        node1 = node1.next
                    elif node1.data[1] > node2.data[1]:
                        node2 = node2.next
                    else:
                        node1 = node1.next
                        node2 = node2.next
                else:
                    return False
            if node1 is self.cstring.trailer:
                return False
            else:
                return True

    def __ge__(self, other):
        if self.cstring.is_empty():
            if other.cstring.is_empty():
                return True
            else:
                return False
        elif other.cstring.is_empty():
            return True
        else:
            node1 = self.cstring.first_node()
            node2 = other.cstring.first_node()
            while node1 is not self.cstring.trailer and node2 is not other.cstring.trailer:
                if node1.data[0] > node2.data[0]:
                    return True
                elif node1.data[0] == node2.data[0]:
                    if node1.data[1] < node2.data[1]:
                        node1 = node1.next
                    elif node1.data[1] > node2.data[1]:
                        node2 = node2.next
                    else:
                        node1 = node1.next
                        node2 = node2.next
                else:
                    return False
            if node1 is self.cstring.trailer:
                if node2 is other.cstring.trailer:
                    return True
                return False
            else:
                return True

    def __repr__(self):
        ret = ''
        crsr = self.cstring.first_node()
        while crsr is not self.cstring.trailer:
            cntr = crsr.data[1]
            while cntr > 0:
                ret += crsr.data[0]
                cntr -= 1
            crsr = crsr.next
        return ret
        
