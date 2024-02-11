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
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head == self.tail:
            temp = self.head
            temp.next = new_node
            self.tail = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        self.length += 1
          
    def delete_node(self, value):
        if self.head == self.tail:
            self.head.next = None
            self.tail.next = None
            print("{} is deleted from the list".format(value))
        elif self.head.value == value:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            print("{} is deleted from the list".format(value))
        else:
            temp = self.head
            while temp != self.tail:
                if temp.next.value == value:
                    temp.next = temp.next.next
                    print("{} is deleted from the list".format(value))
                    break
                temp = temp.next
            
            
            
new_list = LinkedList(6)
new_list.append(10)
new_list.append(3)
new_list.append(5)
new_list.print_list()
new_list.delete_node(5)
new_list.print_list()

