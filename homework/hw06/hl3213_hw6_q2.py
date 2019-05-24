from DoublyLinkedList import DoublyLinkedList

class Integer:

    def __init__(self, num_str):
        self.digits = DoublyLinkedList()
        num_str = num_str.lstrip("0")
        for i in num_str:
            #print("adding ", i)
            self.digits.add_last(i)
        
    def  __add__(self, other):
        result = ""
        carry = 0
        
        int1 = self.digits
        digit1 = self.digits.last_node()
        int2 = other.digits
        digit2 = other.digits.last_node()
        
        while digit1 is not int1.header and digit2 is not int2.header:
            sm = int(digit1.data) + int(digit2.data) + carry
            if sm >= 10:
                carry = sm // 10
                sm %= 10
            else:
                carry = 0
            result = str(sm) + result
            digit1 = digit1.prev
            digit2 = digit2.prev
        #if len(int1) == len(int2) and carry != 0:
        #    result = str(carry) + result
        if len(int2) > len(int1):
            int1, int2 = int2, int1
            digit1, digit2 = digit2, digit1
        while digit1 is not int1.header:
            sm = int(digit1.data) + carry
            if sm >= 10:
                carry = sm // 10
                sm %= 10
            else:
                carry = 0
            result = str(sm) + result
            digit1 = digit1.prev
        #print("Carry: ", carry)
        if carry != 0:
            result = str(carry) + result
            
        final = Integer(result)
        return final
            
    #def __mul__(self, other):

    def __repr__(self):
        num = ""
        cursor = self.digits.first_node()
        while cursor is not self.digits.trailer:
            num += cursor.data
            cursor = cursor.next
        return num
