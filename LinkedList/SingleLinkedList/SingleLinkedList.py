class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
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
                        if next_node is None:
                            self.tail = new_node
                        return
                    count += 1
                    temp_node = temp_node.next
        print("Index out of bounds")


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
                print("{} number found at position {}".format(data, position))
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


    def delete_all(self, data):
        if self.head is None:
            print("Linked list was empty")
            return
        delete = False
        if self.head.data == data:
            print("Element successfully deleted at head position")
            delete = True
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        prev_node = self.head
        temp_node = self.head.next
        while temp_node:
            if temp_node.data == data:
                if temp_node.next is None:

                    print("Element successfully deleted at tail position")
                    delete = True
                    self.tail = prev_node
                    self.tail.next = None
                    return 
                else:
                    print("Element successfully deleted")
                    delete = True
                    prev_node.next = temp_node.next
                    temp_node = temp_node.next
            else:
                prev_node = temp_node
                temp_node = temp_node.next
        if not delete:
            print("Element not found")

    def delete_pos(self, pos):
        if pos <= 0:
            print("Incorrect position entered")
            print("Position value starts from 1 onwards ...")
            return
        if pos == 1:
            if self.head:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
        else:
            temp_node = self.head
            count = 1
            delete = False
            while temp_node and count < pos:
                if count == pos-1:
                    if temp_node.next:
                        deleted_node = temp_node.next
                        temp_node.next = deleted_node.next
                        del deleted_node
                        delete = True
                        if temp_node.next is None:
                            self.tail = temp_node
                count += 1
                temp_node = temp_node.next
        if pos > 1 and not delete:
            print("Entered position out of bounds")
                        

    def delete_head(self):
        if self.head is None:
            print("Linkedlist was empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def delete_tail(self):
        if self.tail is None:
            print("LinkedList was empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next != self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print("NULL")


    def get_head(self):
        if self.head:
            return self.head.data
        return None


    def get_tail(self):
        if self.tail:
            return self.tail.data
        return None


    def delete(self, data):
        if self.head is None:
            print("Linked list was empty")
            return
        delete = False
        if self.head.data == data:
            print("Element successfully deleted at head position")
            delete = True
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return
        prev_node = self.head
        temp_node = self.head.next
        while temp_node:
            if temp_node.data == data:
                if temp_node.next is None:
                    print("Element successfully deleted at tail position")
                    delete = True
                    self.tail = prev_node
                    self.tail.next = None
                    return 
                else:
                    print("Element successfully deleted")
                    delete = True
                    prev_node.next = temp_node.next
                    temp_node = temp_node.next
                    return
            prev_node = temp_node
            temp_node = temp_node.next
        if not delete:
            print("Element not found")