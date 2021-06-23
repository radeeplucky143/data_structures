class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        print("NULL")

    def get_head(self):
        if self.head:
            print("Head of the linked_list : {}".format(self.head.data))
            return
        print("Linked list was Empty")

    def get_tail(self):
        if self.tail:
            print("Tail of the linked list: {}".format(self.tail.data))
            return
        print("Linked list was empty")
