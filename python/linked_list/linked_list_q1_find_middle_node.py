class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    # WRITE FIND_MIDDLE_NODE METHOD HERE #

    def find_middle_node(self):
        """
            Member function to find the middle element in the list
            using the 2 pointer approach.
        Returns:
            Node: The middle element in the linked list
        """
        if self.head == self.tail:
            return self.head
        slow_ptr = self.head
        fast_ptr = slow_ptr.next
        while fast_ptr != None:
            slow_ptr = slow_ptr.next
            if fast_ptr.next == None:
                return slow_ptr
            else:
                if fast_ptr.next.next != None:
                    fast_ptr = fast_ptr.next.next
                else:
                    fast_ptr = None
                    return slow_ptr


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)


print(my_linked_list.find_middle_node().value)


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
