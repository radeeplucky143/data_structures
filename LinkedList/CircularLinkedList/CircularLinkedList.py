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
            self.head = new_node


    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node


    def insert_pos(self, data, pos):
        if pos >= 1:
            if pos == 1:
                self.insert_front(data)
                return
            else:
                temp_node = self.head
                count = 1
                new_node = Node(data)
                while temp_node:
                    if count == pos - 1:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.next = next_node
                        if next_node == self.head:
                            self.tail = new_node
                        return
                    count += 1
                    temp_node = temp_node.next
                    if temp_node == self.head:
                        break
        print("Index out of bounds")


    def search(self, data):
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("{} number  found at {} position ".format(data, position))
                return
            position += 1
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        print("Element not found")


    def search_all(self, data):
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("Element found at {} position ".format(position))
                found = True
            position += 1
            temp_node = temp_node.next
            if temp_node == self.head:
                break
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
                if temp_node == self.head:
                    break
        print("Index out of Bounds")


    def delete_head(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return
        print("Linked List is Empty")


    def delete_tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp_node = self.head
                while temp_node.next != self.tail:
                    temp_node = temp_node.next
                self.tail = temp_node
                self.tail.next = self.head
            return
        print("Linked List is Empty")


    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        if self.head:
            print("HEAD")
        else:
            print("NULL")


    def get_head(self):
        if self.head:
            return self.head.data
        return None


    def get_tail(self):
        if self.tail:
            return self.tail.data
        return None