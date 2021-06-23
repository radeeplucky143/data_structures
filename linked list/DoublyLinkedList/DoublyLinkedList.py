class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def get_head(self):
        if self.head:
            print("Head of the Doubly Linked List: {}".format(self.head.data))
            return
        print("Doubly Linked List was Empty")


    def get_tail(self):
        if self.tail:
            print("Tail of the Doubly Linked List : {}".format(self.tail.data))
            return
        print("Doubly Linked List was Empty")


    def insert_front(self, data):
        new_node = Node(data)
        if self.head:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
            temp_node.next = new_node
            new_node.prev =temp_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node


    def print_list(self):
        if self.head:
            temp_node = self.head
            print("NULL",end="<->")
            while temp_node:
                print(temp_node.data,end='<->')
                temp_node = temp_node.next
            print("NULL")
        else:
            print("Double Linked List was Empty")


    def print_list_reverse(self):
        if self.tail:
            temp_node = self.tail
            print("NULL",end="<->")
            while temp_node:
                print(temp_node.data,end='<->')
                temp_node = temp_node.prev
            print("NULL")
        else:
            print("Double Linked List was Empty")
                
