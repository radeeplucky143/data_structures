class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def insert_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node


    def insert_back(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node


    def insert_pos(self, data, pos):
        if pos >= 1:
            if pos == 1:
                self.insert_front(data)
                return
            else:
                count = 1
                temp_node = self.head
                new_node = Node(data)
                while temp_node:
                    if count == pos - 1:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.prev = temp_node
                        new_node.next = next_node
                        if next_node is None:
                            self.tail = new_node
                        else:
                            next_node.prev = new_node
                        return
                    count += 1
                    temp_node = temp_node.next
        print("Index out of Bounds")

    def search(self, data):
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("{} number  found at position {}".format(data, position))
                return
            position += 1
            temp_node = temp_node.next
        print("Element not found")


    def search_all(self, data):
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("{} number  found at position {}".format(data, position))
                found = True
            position += 1
            temp_node = temp_node.next
        if not found:
            print("Element not found")


    def search_pos(self, pos):
        if pos >= 1:
            temp_node = self.head
            count = 1
            while temp_node:
                if count == pos:
                    print("Element at {} position : {}".format(pos, temp_node.data))
                    return
                count += 1
                temp_node = temp_node.next
        print("Index out of Bounds")


    def print_list(self):
        if self.head:
            temp_node = self.head
            print("NULL", end='<->')
            while temp_node:
                print(temp_node.data, end='<->')
                temp_node = temp_node.next
            print("NULL")
            return
        print("NULL")


    def print_reverse(self):
        if self.tail:
            temp_node = self.tail
            print("NULL", end="<->")
            while temp_node:
                print(temp_node.data, end='<->')
                temp_node = temp_node.prev
            print("NULL")
            return
        print("NULL")


    def get_head(self):
        if self.head:
            return self.head.data
        return None

    def get_tail(self):
        if self.tail:
            return self.tail.data
        return None
