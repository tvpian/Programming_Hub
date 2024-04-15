class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        """
           Member function to check for self loops in a Linked List.
           The algorithm followed is Floyd's Cycle Finding Algorithm
        Returns:
            _type_: _description_
        """
        if self.head == self.tail or self.head == None:
            return False
        fast_ptr = self.head
        slow_ptr = self.head
        while fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            if fast_ptr.next.next != None:
                fast_ptr = fast_ptr.next.next
                if fast_ptr == slow_ptr:
                    return True
            else:
                return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True


my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False


# Importing the Node and LinkedList classes provided in the code snippet

# Test Case 1: Empty linked list
empty_linked_list = LinkedList(None)
print(empty_linked_list.has_loop())  # Expected output: False

# Test Case 2: Linked list with one element
single_element_linked_list = LinkedList(1)
print(single_element_linked_list.has_loop())  # Expected output: False

# Test Case 3: Linked list without a loop
linked_list_without_loop = LinkedList(1)
linked_list_without_loop.append(2)
linked_list_without_loop.append(3)
linked_list_without_loop.append(4)
print(linked_list_without_loop.has_loop())  # Expected output: False

# Test Case 4: Linked list with a loop
linked_list_with_loop = LinkedList(1)
linked_list_with_loop.append(2)
linked_list_with_loop.append(3)
linked_list_with_loop.append(4)
linked_list_with_loop.tail.next = linked_list_with_loop.head
print(linked_list_with_loop.has_loop())  # Expected output: True

# Test Case 5: Large linked list with a loop
large_linked_list_with_loop = LinkedList(1)
for i in range(2, 1001):  # Creating a linked list with 1000 elements
    large_linked_list_with_loop.append(i)
large_linked_list_with_loop.tail.next = large_linked_list_with_loop.head  # Creating a loop
print(large_linked_list_with_loop.has_loop())  # Expected output: True


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
