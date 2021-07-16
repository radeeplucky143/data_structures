class Node:
    """     Class used to create Node:
                        : data(param)  ==  used to store data
                        : next(param)  ==  Pointer pointing to next Node

                        : next(type)     ==  Node(class)
                        : data(type)     ==  int,float,str
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """      Class used to create a CircularLinkedList Data Structure
                        : head(param)   ==  Pointing to First Element of CLL
                        : tail(param)     ==  Pointing to Last Element of CLL
                        : data_type(param)  ==  stores the type of data inside Node

                        : head(type)  == Node(class)
                        : tail(type)    ==  Node(class)
                        : data_type(type)  == int,float,str
    """
    def __init__(self):
        """
                created CircularLinkedList and initializes the head and tail to None.
        """
        self.head = None
        self.tail = None
        self.data_type = None


    def set_data_type(self, data):
        """
              This Function is used to set the data_type attribute
              which helps in maintaining the same data type along the LinkedList.
        """
        if isinstance(data, int):
            self.data_type = int
        elif isinstance(data, float):
            self.data_type = float
        elif isinstance(data, str):
            self.data_type = str
        else:
            print("DataTypes should be [int,float,str]")


    def insert_front(self, data):
        """
                This function is used to Insert the Node at front and make sure the inserted Node
                contains the data with same data type.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        new_node = Node(data)
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            new_node.next = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node


    def insert_back(self, data):
        """
                This function is used to Insert the Node at back and make sure the inserted Node
                contains the data with same data type.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        new_node = Node(data)
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            new_node.next = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node


    def insert_pos(self, data, position):
        """
                This function is used to Insert the Node at defined position If possible
                and make sure the inserted Node contains the data with same data type.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        if position >= 1:
            if position == 1:
                new_node = Node(data)
                if self.head is None:
                    self.set_data_type(data)
                    self.head = new_node
                    new_node.next = new_node
                    self.tail = self.head
                else:
                    self.tail.next = new_node
                    new_node.next = self.head
                    self.head = new_node
                return
            else:
                temp_node = self.head
                count = 1
                new_node = Node(data)
                while temp_node:
                    if count == position - 1:
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
        print("Position out of bounds")


    def search(self, data):
        """
             This Function is used to search for the first Instance matched in the LinkedList.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("{} Found at Position: {} ".format(data, position))
                return
            position += 1
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        print("Element Not Found")


    def search_all(self, data):
        """
               This Function is used to search for all Instances matched in the LinkedList.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("{} Found at Position : {} ".format(data, position))
                found = True
            position += 1
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        if not found:
            print("Element Not Found")


    def search_pos(self, position):
        """
                This Function is used to search for the Element in that position  of  LinkedList.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        if position >= 1:
            temp_node = self.head
            count = 1
            while temp_node:
                if count == position:
                    print("Element at {} position : {}".format(position, temp_node.data))
                    return
                count += 1
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
        print("Position  out of Bounds")


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


    def delete(self, data):
        if self.head:
            if self.head.data == data:
                print("Deletion at head Successful")
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                return
            else:
                prev_node = self.head
                temp_node = self.head.next
                while temp_node:
                    if temp_node.data == data:
                        next_node = temp_node.next
                        prev_node.next = next_node
                        del temp_node
                        if next_node == self.head:
                            self.tail = prev_node
                            print("Deletion at tail successful")
                        else:
                            print("Deletion successful")
                        return
                    prev_node = temp_node
                    temp_node = temp_node.next
                    if temp_node == self.head:
                        break
            print("Element not Found")
            return
        print("Linked List was Empty")


    def delete_all(self, data):
        if self.head:
            operation = False
            if self.head.data == data:
                operation = True
                print("Deletion at head Successful")
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            prev_node = self.head
            temp_node = self.head.next
            while temp_node:
                if temp_node.data == data:
                    operation = True
                    next_node = temp_node.next
                    prev_node.next = next_node
                    if next_node == self.head:
                        self.tail = prev_node
                        print("Deletion at tail successful")
                        return
                    else:
                        temp_node = next_node
                        print("Deletion successful")
                else:
                    prev_node = temp_node
                    temp_node = temp_node.next
                if temp_node == self.head:
                    break
            if not operation:
                print("Element not Found")
            return
        print("Linked List was Empty")


    def delete_pos(self, position):
        if position >= 1:
            if position == 1:
                self.delete_head()
                return
            else:
                count = 1
                temp_node = self.head
                while temp_node:
                    if count == position - 1:
                        if temp_node.next != self.head:
                            next_node = temp_node.next.next
                            temp_node.next = next_node
                            if next_node == self.head:
                                self.tail = temp_node
                            return
                        break
                    temp_node = temp_node.next
                    count += 1
            print("Index out of Bounds")
            return
        print("Index out of Bounds")

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