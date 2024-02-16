class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        if self.length != 0:
            print("The following are the elements in the list:")
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next
            print("------------------------------------------")
        else:
            print("The list is empty")

    def append(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            if self.head != None:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.head = new_node
                self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        self.length += 1
        print("{} is appended to the list".format(value))
        print("Head is pointing to {}".format(self.head.value))
        print("Tail is pointing to {}".format(self.tail.value))
        print("------------------------------------------")

    def delete_node(self, value):
        # Only one item in the list
        if self.head == self.tail:
            if self.head.value == value:
                self.head.next = None
                self.tail.next = None
                print("{} is deleted from the list".format(value))
                print("Head is pointing to {}".format(self.head.value))
                print("Tail is pointing to {}".format(self.tail.value))
                self.length -= 1
                print("------------------------------------------")
            else:
                print("Item not found in the list")
        elif self.head.value == value:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            print("{} is deleted from the list".format(value))
            print("Head is pointing to {}".format(self.head.value))
            print("Tail is pointing to {}".format(self.tail.value))
            self.length -= 1
            print("------------------------------------------")
        else:
            temp = self.head
            del_check = False
            while temp != self.tail:
                if temp.next.value == value:
                    temp.next = temp.next.next
                    print("{} is deleted from the list".format(value))
                    print("Head is pointing to {}".format(self.head.value))
                    print("Tail is pointing to {}".format(self.tail.value))
                    del_check = True
                    self.length -= 1
                    print("------------------------------------------")
                    break
                temp = temp.next
            if not del_check:
                print("Item not found in the list")

    def pop_node(self):
        # If the list is empty
        if self.head == None:
            print("No elements in the list to pop")
        # If there is only element in the list
        elif self.head == self.tail:
            # Popping the last element from the list
            temp = self.head
            print("Remaining Last element {} is popped from the list".format(
                self.tail.value))
            self.head = None
            self.tail = None
            print("Head is pointing to None")
            print("Tail is pointing to None")
            self.length -= 1
            print("------------------------------------------")
            return temp
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            print("Last element {} is popped from the list".format(self.tail.value))
            self.tail = temp
            temp = self.tail.next
            self.tail.next = None
            print("Head is pointing to {}".format(self.head.value))
            print("Tail is pointing to {}".format(self.tail.value))
            self.length -= 1
            print("------------------------------------------")
            return temp

    def prepend(self, value):
        """ Member function to append items to the beginning of the list
        Args:
            value (int): The value of the new item to be added to the  list
        """
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1
        print("New node with value {} added to the list".format(value))
        print("Head is pointing to {}".format(self.head.value))
        print("Tail is pointing to {}".format(self.tail.value))
        return True

    def pop_first(self):
        if self.length == 0:
            print("The list is empty")
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            print("{} is popped from the list".format(temp.value))
            print("Head is pointing to None")
            print("Tail is pointing to None")
            print("------------------------------------------")
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            print("{} is popped from the list".format(temp.value))
            print("Head is pointing to {}".format(self.head.value))
            print("Tail is pointing to {}".format(self.tail.value))
            print("------------------------------------------")
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index. Index out of bounds")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            print("Invalid index. Index out of bounds")
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            print("Value at index {} updated to {}".format(index, value))
            return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Invalid index. Index out of bounds")
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.get(index-1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length+1:
            print("Invalid index. Index out of bounds.")
        elif index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop_node()
        else:
            temp = self.get(index-1)
            del_node = temp.next
            temp.next = temp.next.next
            del_node.next = None
            self.length -= 1
            print("Element at the index {} is deleted.".format(index))


if __name__ == "__main__":
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    # print(my_linked_list.get(0))
    # print(my_linked_list.get(1))
    # print(my_linked_list.get(2))
    # print(my_linked_list.get(3))
    # my_linked_list.set_value(1, 9)
    # my_linked_list.print_list()
    # my_linked_list.set_value(1, 6)
    # my_linked_list.print_list()
    my_linked_list.insert(2, 10)
    print(my_linked_list.length)
    my_linked_list.print_list()
    my_linked_list.remove(0)
    print(my_linked_list.length)
    my_linked_list.print_list()
    my_linked_list.remove(1)
    print(my_linked_list.length)
    my_linked_list.print_list()
    my_linked_list.remove(2)
    print(my_linked_list.length)
    my_linked_list.print_list()
